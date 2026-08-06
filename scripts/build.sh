#!/usr/bin/env bash
# Gera o site completo em docs/: português na raiz e inglês em docs/en/.
set -euo pipefail
cd "$(dirname "$0")/.."

# Monta a galeria do Sobre a partir das fotos em about/images/galeria
# (precisa rodar antes do Quarto, que expande os includes ao ler os fontes)
python3 scripts/gen_gallery.py

quarto render --profile pt
quarto render --profile en

# As páginas com sufixo de idioma só existem para o "quarto preview";
# a versão publicada usa apenas os nomes finais (sem .pt/.en)
find docs -name '*.pt.html' -delete -o -name '*.en.html' -delete

# Impede o processamento Jekyll no GitHub Pages
touch docs/.nojekyll
