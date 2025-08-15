
# Colab Cell 1: Database Setup and Document Processing

from google.colab import userdata
import os
import lancedb
from lancedb.pydantic import LanceModel, Vector
from lancedb.embeddings import get_registry
from docling.chunking import HybridChunker
from docling.document_converter import DocumentConverter
from docling_core.transforms.chunker.tokenizer.huggingface import HuggingFaceTokenizer
from transformers import AutoTokenizer


from google.colab import userdata
import os
# Set API keys
os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")
os.environ["HF_TOKEN"] = userdata.get("HF_Token")

# Create LanceDB database
db = lancedb.connect("data/lancedb")

# Get Gemini embedding function
func = get_registry().get("gemini-text").create(
    name="models/embedding-001"
)

# Define schemas
class ChunkMetadata(LanceModel):
    filename: str | None
    page_numbers: list[int] | None
    title: str | None


class Chunks(LanceModel):
    text: str = func.SourceField()
    vector: Vector(func.ndims()) = func.VectorField()
    metadata: ChunkMetadata

# Create table
table = db.create_table("docling", schema=Chunks, mode="overwrite")

# Extract and chunk documents
EMBED_MODEL_ID = "google/gemma-2b"
MAX_TOKENS = 8192

tokenizer = HuggingFaceTokenizer(
    tokenizer=AutoTokenizer.from_pretrained(EMBED_MODEL_ID),
    max_tokens=MAX_TOKENS,
)

converter = DocumentConverter()
chunker = HybridChunker(
    tokenizer=tokenizer,
    merge_peers=True,
)

# List of documents to process (PDF and HTML)
document_urls = [
    "https://modelcontextprotocol.io/examples", # Example HTML
    "https://research.google.com/colaboratory/faq.html", # Example HTML
    #example pdf(copy paste the file path)

]

all_processed_chunks = []

for url in document_urls:
    print(f"Processing: {url}")
    result = converter.convert(url)

    if result.document:
        chunks = list(chunker.chunk(dl_doc=result.document))


        # Prepare chunks for the table
        processed_chunks = [
            {
                "text": chunk.text,
                "metadata": {
                    "filename": chunk.meta.origin.filename,
                    # Ensure page_numbers is always a list of integers or None
                    "page_numbers": sorted(
                        list(set(
                            prov.page_no
                            for item in chunk.meta.doc_items
                            for prov in item.prov
                        ))
                    ) if chunk.meta.doc_items else None, # Explicitly set to None if no doc_items
                    "title": chunk.meta.headings[0] if chunk.meta.headings else None,

                },
            }
            for chunk in chunks
        ]
        all_processed_chunks.extend(processed_chunks)
    else:
        print(f"Could not process document from {url}")


# Add all processed chunks to the table
if all_processed_chunks:
    table.add(all_processed_chunks)
    print(f"Added {len(all_processed_chunks)} chunks to the database.")
else:
    print("No chunks were processed or added to the database.")


print("Database created and populated successfully.")
