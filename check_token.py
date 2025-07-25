from huggingface_hub import HfApi

HF_TOKEN = "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"  # 🔁 Replace with your real token

api = HfApi()
user = api.whoami(token=HF_TOKEN)

print("✅ Authenticated as:", user["name"])
