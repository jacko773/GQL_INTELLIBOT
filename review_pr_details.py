import faiss
import json
import requests

from constant import embedding_model, MISTRAL_API_BASE, headers

def find_relevant_guidelines(query, top_k=3):
    print("query ===============", query[0])
    query_embedding = embedding_model.encode([query[0]], convert_to_numpy=True)
    print("query_embedding ===============", query_embedding)
    index = faiss.read_index("guidelines.index")
    distances, indices = index.search(query_embedding, top_k)

    # Load metadata
    with open("guidelines_metadata.json", "r") as f:
        chunks = json.load(f)

    return [chunks[i] for i in indices[0] if i < len(chunks)]


def review_pr(pr_data):
    """Generate AI review comments for a PR based on guidelines."""
    # query = pr_data["files_changed"]
    query = pr_data
    guidelines = find_relevant_guidelines(query)


    print("Data to review", query)

    prompt = f"Review this PR based on these guidelines:\n\n{guidelines}\n\n Pr details :\n{query}, and , provide the review comments in json format which should include accurate line_number , review_comment, suggested changes, file_path only if there is a issue according to guidelines"
    
    # data = {
    #     "model": "open-mistral-7b",
    #     "messages": [{"role": "user", "content": prompt}]
    # }
    data = {
        "model": "open-mistral-7b",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(f"{MISTRAL_API_BASE}/chat/completions", headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print("Review Error:", response.json())
        return None