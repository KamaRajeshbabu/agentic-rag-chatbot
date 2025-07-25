import requests
import json

API_TOKEN = "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" 

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

model = "mistralai/Mistral-7B-Instruct-v0.1"  # or any other available model
url = f"https://api-inference.huggingface.co/models/{model}"

payload = {
    "inputs": "What is customer retention?",
    "parameters": {"max_new_tokens": 50}
}

response = requests.post(url, headers=headers, json=payload)

print("Status Code:", response.status_code)
print("Response:", response.text)


