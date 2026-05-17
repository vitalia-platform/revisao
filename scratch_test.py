import csv

with open('export_novo_repo/savedrecs.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print("Total articles in CSV:", len(rows))
if rows:
    print("Sample Title:", rows[0].get('Article Title', 'N/A'))
    print("Sample Abstract snippet:", rows[0].get('Abstract', 'N/A')[:200])

