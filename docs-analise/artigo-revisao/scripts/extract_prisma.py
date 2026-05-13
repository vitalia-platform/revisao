import sys
try:
    import pypdf
except ImportError:
    print("pypdf not found")
    sys.exit(1)

pdf_path = "docs-analise/artigo-revisao/artigos/2020 - Marcondes - PRISMA Protocol.pdf"

try:
    with open(pdf_path, "rb") as f:
        reader = pypdf.PdfReader(f)
        num_pages = len(reader.pages)
        
        extracted_text = ""
        for i in range(num_pages):
            page = reader.pages[i]
            extracted_text += f"\n--- Página {i+1} ---\n"
            extracted_text += page.extract_text()
            
        with open("/Users/andre/.gemini/antigravity/brain/826c6503-5831-4939-b09f-06501ff76778/scratch/prisma_text.txt", "w", encoding="utf-8") as out:
            out.write(extracted_text)
        print("Texto extraído com sucesso.")
except Exception as e:
    print(f"Erro: {e}")
