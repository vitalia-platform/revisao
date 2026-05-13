import os
import json

base_dir = "docs-analise/artigo-revisao"
pdf_dir = os.path.join(base_dir, "artigos")
audit_file = os.path.join(base_dir, "AUDIT_LOG.json")
md_file = os.path.join(base_dir, "lista_links_manual.md")

doi_map = {
    "10.2196/53123": "10.2196/76601",
    "10.1016/j.jshs.2024.100984": "10.1016/j.jshs.2025.101045",
    "10.2196/41505": "10.1186/s12984-023-01124-9",
    "10.3389/fpubh.2024.12534984": "10.1186/s12889-025-24679-9",
    "10.1136/bmjgh-2022-010410": "10.1016/j.eclinm.2024.102432",
    "10.1016/j.physio.2023.01.002": "10.1016/j.jphys.2022.11.012",
    "10.2196/23241": "10.2196/33264",
    "10.1186/s12966-023-01452-4": "10.1371/journal.pone.0301088",
    "10.2196/34567": "10.2196/34767",
    "10.3389/fspor.2022.912042": "10.1186/s40798-019-0214-z"
}

def safe_filename(doi):
    return doi.replace("/", "_")

# 1. Update AUDIT_LOG.json and rename PDFs
with open(audit_file, "r", encoding="utf-8") as f:
    audit_data = json.load(f)

for entry in audit_data:
    old_doi = entry.get("doi")
    if old_doi in doi_map:
        new_doi = doi_map[old_doi]
        old_filename = entry["current_filename"]
        
        # Replace the old safe doi with new safe doi in the filename
        old_safe_doi = safe_filename(old_doi)
        new_safe_doi = safe_filename(new_doi)
        new_filename = old_filename.replace(old_safe_doi, new_safe_doi)
        
        # Rename physical file
        old_path = os.path.join(pdf_dir, old_filename)
        new_path = os.path.join(pdf_dir, new_filename)
        
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
            print(f"Renamed: {old_filename} -> {new_filename}")
        else:
            print(f"Warning: File not found {old_path}")
            
        # Update json entry
        entry["doi"] = new_doi
        entry["current_filename"] = new_filename

with open(audit_file, "w", encoding="utf-8") as f:
    json.dump(audit_data, f, indent=4, ensure_ascii=False)
print("AUDIT_LOG.json updated.")

# 2. Update lista_links_manual.md
with open(md_file, "r", encoding="utf-8") as f:
    md_content = f.read()

for old_doi, new_doi in doi_map.items():
    md_content = md_content.replace(old_doi, new_doi)
    old_safe_doi = safe_filename(old_doi)
    new_safe_doi = safe_filename(new_doi)
    md_content = md_content.replace(old_safe_doi, new_safe_doi)

with open(md_file, "w", encoding="utf-8") as f:
    f.write(md_content)
print("lista_links_manual.md updated.")
