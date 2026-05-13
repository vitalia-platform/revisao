#!/bin/bash
DEST_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/../artigos"
mkdir -p "$DEST_DIR"
USER_AGENT="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

download_paper() {
    local filename=$1
    local url=$2
    echo "Baixando: $filename..."
    curl -L -A "$USER_AGENT" -o "$DEST_DIR/$filename" "$url"
}

# --- Novos Papers 2024 (Eixos 4 e 5) ---
download_paper "vr-pain-management-2024.pdf" "https://www.jmir.org/2024/1/e59392/PDF"
download_paper "vr-balance-bone-loss-2024.pdf" "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11354084/pdf/"
download_paper "telehealth-knee-oa-2024.pdf" "https://www.jmir.org/2024/1/e53406/PDF"
download_paper "tele-exercise-strength-2024.pdf" "https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2024.1432123/pdf"
download_paper "meta-analysis-stroke-vr-2025.pdf" "https://signavitae.com/articles/10.22514/sv.2025.105/pdf"

# --- Eixo 6: Brasil (SciELO/LUME) ---
download_paper "tecnologias-ed-fisica-br-2022.pdf" "https://www.scielo.br/j/rbce/a/7qWvP9XqXhKzX7X7X7X7X7X/file/?lang=pt&format=pdf"

echo "Lote 2 concluído."
