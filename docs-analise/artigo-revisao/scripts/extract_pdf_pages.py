import sys
try:
    import pypdf
except ImportError:
    import os
    os.system("pip install pypdf")
    import pypdf

pdf_path = "docs-analise/artigo-revisao/artigos/2022 - BJSM - 10.1136_bjsports-2021-105118.pdf"

try:
    with open(pdf_path, "rb") as f:
        reader = pypdf.PdfReader(f)
        num_pages = len(reader.pages)
        print(f"Total de páginas: {num_pages}")
        
        # Paginação é 0-indexed. Página 14 é o índice 13.
        start_page = 13
        extracted_text = ""
        for i in range(start_page, num_pages):
            page = reader.pages[i]
            extracted_text += f"\n--- Página {i+1} ---\n"
            extracted_text += page.extract_text()
            
        with open("/Users/andre/.gemini/antigravity/brain/826c6503-5831-4939-b09f-06501ff76778/scratch/artigo19_supp.txt", "w", encoding="utf-8") as out:
            out.write(extracted_text)
        print("Texto extraído com sucesso.")
except Exception as e:
    print(f"Erro: {e}")
