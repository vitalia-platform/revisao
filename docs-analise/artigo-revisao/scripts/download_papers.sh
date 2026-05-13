#!/bin/bash

# Script de Download - Revisão Integrativa Vitalia (2018-2026)
# Este script tenta baixar os artigos selecionados para a pasta local.

DEST_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/../artigos"
mkdir -p "$DEST_DIR"

USER_AGENT="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

download_paper() {
    local filename=$1
    local url=$2
    echo "Baixando: $filename..."
    curl -L -A "$USER_AGENT" -o "$DEST_DIR/$filename" "$url"
}

# --- Eixo 1: IA e Machine Learning ---
download_paper "generative-ai-exercise-prescription-2024.pdf" "https://www.mdpi.com/2075-4663/12/3/77/pdf"
download_paper "ml-persuasive-mhealth-2024.pdf" "https://www.jmir.org/2024/1/e53406/PDF"
download_paper "ai-social-robots-older-adults-2024.pdf" "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11019864/pdf/"
download_paper "ai-physical-education-2024.pdf" "https://revista-apunts.com/wp-content/uploads/2024/04/Apunts-156_71-86_EN.pdf"

# --- Eixo 2: Wearables e Sensores ---
download_paper "accuracy-hr-monitoring-2023.pdf" "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10103233/pdf/"
download_paper "polar-h10-validation-2019.pdf" "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6732081/pdf/sensors-19-03517.pdf"
download_paper "polar-h10-rr-interval-2020.pdf" "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7312154/pdf/sensors-20-03223.pdf"
download_paper "deep-learning-har-sensors-2022.pdf" "https://www.mdpi.com/1424-8220/22/11/4214/pdf"

# --- Eixo 3: Apps e Gamificação ---
download_paper "mhealth-apps-children-2024.pdf" "https://www.jmir.org/2024/1/e45678/PDF" # Exemplo
download_paper "digital-tech-interventions-prisma-2021.pdf" "https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0251674&type=printable"

# --- Eixo 4: Telemetria e Contexto Local ---
download_paper "revisao-integrativa-br-2022.pdf" "https://www.researchgate.net/publication/361841312_TECNOLOGIAS_DIGITAIS_E_A_EDUCACAO_FISICA_UMA_REVISAO_INTEGRATIVA/fulltext/62c82f9d659e4b778747f3b1/TECNOLOGIAS-DIGITAIS-E-A-EDUCACAO-FISICA-UMA-REVISAO-INTEGRATIVA.pdf"

echo "Processo concluído. Verifique o tamanho dos arquivos em $DEST_DIR"
