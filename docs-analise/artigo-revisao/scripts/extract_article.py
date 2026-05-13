import sys
import os
try:
    import pypdf
except ImportError:
    print("pypdf not found. Please install it using 'pip install pypdf'")
    sys.exit(1)

if len(sys.argv) < 2:
    print("Usage: python extract_article.py <pdf_filename>")
    sys.exit(1)

pdf_filename = sys.argv[1]
base_dir = "/Users/andre/projetos/assistidos/revisao/docs-analise/artigo-revisao"
pdf_path = os.path.join(base_dir, "artigos", pdf_filename)
scratch_path = "/Users/andre/.gemini/antigravity/brain/826c6503-5831-4939-b09f-06501ff76778/scratch/current_article.txt"

if not os.path.exists(pdf_path):
    print(f"Error: File not found {pdf_path}")
    sys.exit(1)

try:
    with open(pdf_path, "rb") as f:
        reader = pypdf.PdfReader(f)
        extracted_text = f"--- EXTRACTED TEXT FROM: {pdf_filename} ---\n\n"
        for i, page in enumerate(reader.pages):
            extracted_text += f"\n[PAGE {i+1}]\n"
            text = page.extract_text()
            if text:
                extracted_text += text
                
    with open(scratch_path, "w", encoding="utf-8") as out:
        out.write(extracted_text)
    print(f"Extraction successful. Saved to {scratch_path}")
except Exception as e:
    print(f"Error: {e}")
