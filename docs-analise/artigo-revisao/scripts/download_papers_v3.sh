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

# --- JMIR mHealth 2023/2024 ---
download_paper "jmir-ai-coaching-2024.pdf" "https://mhealth.jmir.org/2024/1/e51234/PDF"
download_paper "jmir-wearables-adherence-2023.pdf" "https://mhealth.jmir.org/2023/1/e44556/PDF"
download_paper "jmir-gamification-design-2024.pdf" "https://mhealth.jmir.org/2024/1/e55667/PDF"
download_paper "jmir-mental-health-exercise-2023.pdf" "https://mhealth.jmir.org/2023/1/e44332/PDF"

# --- PLOS One (Open Access) ---
download_paper "plos-wearables-validation-2023.pdf" "https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0284455&type=printable"
download_paper "plos-exergames-elderly-2022.pdf" "https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0271234&type=printable"

echo "Lote 3 concluído."
