#!/usr/bin/env python3
"""Publica as páginas geradas sem o sufixo de idioma (index.pt.html -> index.html).

Cada perfil do Quarto renderiza arquivos *.pt.qmd ou *.en.qmd, mas as URLs
publicadas não devem carregar o sufixo: o idioma já é dado pelo diretório
(português na raiz, inglês em /en). Executado como post-render (_quarto.yml),
corrige os links internos e grava uma cópia de cada página com o nome final.

O arquivo com sufixo é mantido porque o "quarto preview" depende dele; no build
de publicação, o scripts/build.sh remove essas cópias ao final.
"""

import os
import re
from pathlib import Path

SUFFIX = re.compile(r"\.(pt|en)\.html")

output_dir = Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "docs"))

for page in list(output_dir.rglob("*.html")):
    text = page.read_text(encoding="utf-8")
    fixed = SUFFIX.sub(".html", text)
    if fixed != text:
        page.write_text(fixed, encoding="utf-8")
    if SUFFIX.search(page.name):
        page.with_name(SUFFIX.sub(".html", page.name)).write_text(fixed, encoding="utf-8")
