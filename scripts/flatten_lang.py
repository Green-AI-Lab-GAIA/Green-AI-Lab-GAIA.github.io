#!/usr/bin/env python3
"""Pós-processa as páginas geradas pelo Quarto (roda como post-render).

1. Remove o sufixo de idioma das páginas (index.pt.html -> index.html): cada
   perfil renderiza arquivos *.pt.qmd ou *.en.qmd, mas as URLs publicadas não
   carregam o sufixo — o idioma já é dado pelo diretório (pt na raiz, en em
   /en). O arquivo com sufixo é mantido porque o "quarto preview" depende
   dele; no build de publicação, o scripts/build.sh remove essas cópias.

2. Versiona o link do styles.css com um hash do conteúdo (styles.css?v=abc),
   para que navegadores nunca usem uma folha de estilos antiga do cache
   depois de uma atualização do site.

3. Converte links mailto: em atributos separados (data-user/data-domain),
   para que nenhum endereço de e-mail apareça inteiro no HTML e seja colhido
   por robôs de spam; o clique copia o endereço (ver link-behavior.html).
"""

import hashlib
import os
import re
from pathlib import Path

SUFFIX = re.compile(r"\.(pt|en)\.html")
CSS_LINK = re.compile(r'(href="[^"]*styles\.css)"')
MAILTO = re.compile(r'href="mailto:([^@"]+)@([^"?]+)"')

output_dir = Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "docs"))

css = output_dir / "styles.css"
versao = hashlib.md5(css.read_bytes()).hexdigest()[:8] if css.exists() else None

for page in list(output_dir.rglob("*.html")):
    text = page.read_text(encoding="utf-8")
    fixed = SUFFIX.sub(".html", text)
    fixed = MAILTO.sub(r'data-user="\1" data-domain="\2" role="button" tabindex="0"', fixed)
    if versao:
        fixed = CSS_LINK.sub(r'\1?v=%s"' % versao, fixed)
    if fixed != text:
        page.write_text(fixed, encoding="utf-8")
    if SUFFIX.search(page.name):
        page.with_name(SUFFIX.sub(".html", page.name)).write_text(fixed, encoding="utf-8")
