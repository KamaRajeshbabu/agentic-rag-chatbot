import os

def parse_documents(file_path: str) -> dict:
    with open(file_path, "r") as f:
        content = f.read()
    return {"file": file_path, "content": content}

