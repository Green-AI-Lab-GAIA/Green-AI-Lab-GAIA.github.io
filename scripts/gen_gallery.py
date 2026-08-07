#!/usr/bin/env python3
"""Gera a galeria da página Sobre a partir da pasta about/images/galeria.

Qualquer imagem colocada nessa pasta entra na galeria automaticamente no
próximo build, em ordem alfabética de nome de arquivo. Executado como
pre-render (_quarto.yml); o fragmento gerado (about/_galeria.qmd) é incluído
pelas duas versões de idioma da página.
"""

from pathlib import Path

PASTA = Path("about/images/galeria")
FRAGMENTO = Path("about/_galeria.qmd")
EXTENSOES = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg", ".avif"}

PASTA.mkdir(parents=True, exist_ok=True)

linhas = ["```{=html}"]
for arquivo in sorted(PASTA.iterdir()):
    if arquivo.suffix.lower() not in EXTENSOES:
        continue
    alt = arquivo.stem.replace("-", " ").replace("_", " ")
    linhas.append(
        f'<figure class="gallery-item">'
        f'<img src="images/galeria/{arquivo.name}" alt="{alt}" loading="lazy">'
        f"</figure>"
    )
linhas.append("```")
conteudo = "\n".join(linhas) + "\n"

# só regrava quando o conteúdo muda, para não invalidar o cache do Quarto
if not FRAGMENTO.exists() or FRAGMENTO.read_text(encoding="utf-8") != conteudo:
    FRAGMENTO.write_text(conteudo, encoding="utf-8")
