import faiss
import numpy as np
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pathlib import Path
from constant import embedding_model

def load_markdown_files(directory: str):
    markdown_texts = []
    for file in Path(directory).glob("*.md"):
        markdown_texts.append(file.read_text())
    return markdown_texts

guidelines_texts = load_markdown_files("graphql_guidelines/")

# Chunk the text for better vector search

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = []
for text in guidelines_texts:
    chunks.extend(splitter.split_text(text))


# Convert text chunks into embeddings
vectorized_chunks = embedding_model.encode(chunks, convert_to_numpy=True)

dimension = vectorized_chunks.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(vectorized_chunks)

faiss.write_index(index, "guidelines.index")

import json
with open("guidelines_metadata.json", "w") as f:
    json.dump(chunks, f)
