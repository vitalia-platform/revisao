import fitz
import os

pdfs = [
    ("25", "2024 - JMIR - 10.2196_38289.pdf"),
    ("26", "2023 - JMIR - 10.1186_s12984-023-01124-9.pdf"),
    ("27", "2020 - JMIR - 10.2196_33264.pdf"),
    ("28", "2022 - JMIR - 10.2196_34767.pdf"),
    ("29", "2022 - BMJ_Global - 10.1016_j.eclinm.2024.102432.pdf"),
    ("30", "2024 - JMIR - 10.2196_39231.pdf"),
    ("31", "2019 - JMIR - 10.2196_13241.pdf")
]

base_dir = "/root/projetos/assistidos/revisao/docs-analise/artigo-revisao/artigos/"
out_dir = "/tmp/"

for num, pdf_name in pdfs:
    pdf_path = os.path.join(base_dir, pdf_name)
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        continue
    
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        
        out_path = os.path.join(out_dir, f"lote4_{num}_{pdf_name.split(' - ')[-1].replace('.pdf', '.txt')}")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Extracted: {out_path}")
    except Exception as e:
        print(f"Failed to extract {pdf_name}: {e}")
