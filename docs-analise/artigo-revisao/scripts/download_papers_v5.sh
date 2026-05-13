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

# --- BMC Sports Science / Medicine ---
download_paper "bmc-ai-physical-activity-review-2023.pdf" "https://bmcsportsscimedrehabil.biomedcentral.com/counter/pdf/10.1186/s13102-023-00632-1.pdf"
download_paper "bmc-wearables-chronic-disease-2024.pdf" "https://bmcsportsscimedrehabil.biomedcentral.com/counter/pdf/10.1186/s13102-024-00789-w.pdf"
download_paper "bmc-mhealth-diabetes-exercise-2023.pdf" "https://bmcsportsscimedrehabil.biomedcentral.com/counter/pdf/10.1186/s13102-023-00654-9.pdf"

# --- SpringerOpen ---
download_paper "springer-digital-health-physical-activity-2022.pdf" "https://health-policy-systems.biomedcentral.com/counter/pdf/10.1186/s12961-022-00854-w.pdf"

echo "Lote 5 concluído."
