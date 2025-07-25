import os
from core.parsers import parse_pdf, parse_docx, parse_csv, parse_pptx, parse_txt

def parse_file(file_path):
    if file_path.endswith(".pdf"):
        return parse_pdf(file_path)
    elif file_path.endswith(".csv"):
        return parse_csv(file_path)
    elif file_path.endswith(".docx"):
        return parse_docx(file_path)
    elif file_path.endswith(".pptx"):
        return parse_pptx(file_path)
    elif file_path.endswith(".md") or file_path.endswith(".txt"):
        return parse_txt(file_path)
    elif file_path.endswith(".md") or file_path.endswith(".txt"):
        content = parse_txt(file_path)
    else:
        return ""

def ingest_files(filenames):
    base_path = "data"
    all_chunks = []

    for file in filenames:
        full_path = os.path.join(base_path, file)
        print(f"[IngestionAgent] 📄 Parsing: {full_path}")
        try:
            text = parse_file(full_path)
            if text:
                all_chunks.append(text)
                print(f"[IngestionAgent] ✅ Parsed chunk.")
            else:
                print(f"[IngestionAgent] ⚠️ Empty or unsupported file.")
        except Exception as e:
            print(f"[IngestionAgent] ❌ Error parsing {file}: {e}")

    return all_chunks
