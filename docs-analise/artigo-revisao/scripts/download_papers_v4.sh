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

# --- JMIR mHealth 2024 ---
download_paper "jmir-mhealth-kids-2024.pdf" "https://mhealth.jmir.org/2024/1/e51478/PDF"
download_paper "jmir-mhealth-behavior-change-2024.pdf" "https://mhealth.jmir.org/2024/1/e49024/PDF"
download_paper "jmir-mhealth-access-stroke-2024.pdf" "https://mhealth.jmir.org/2024/1/e56534/PDF"
download_paper "jmir-mhealth-quality-criteria-2024.pdf" "https://mhealth.jmir.org/2024/1/e48625/PDF"

# --- Frontiers (Tentativa com headers) ---
download_paper "frontiers-narrative-review-ai-2024.pdf" "https://www.frontiersin.org/journals/sports/articles/10.3389/fspor.2024.1332123/pdf"

echo "Lote 4 concluído."
