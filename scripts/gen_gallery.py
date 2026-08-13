#!/usr/bin/env python3
"""Gera a galeria da página Sobre a partir da pasta about/images/galeria.

Qualquer imagem colocada nessa pasta entra na galeria no próximo build, em
ordem alfabética de nome de arquivo. As legendas (pt e en) vêm do arquivo
legendas.txt na mesma pasta; fotos sem legenda usam o nome do arquivo.
Executado pelo scripts/build.sh antes do Quarto; gera um fragmento de
miniaturas por idioma (about/_galeria.pt.qmd e about/_galeria.en.qmd).
"""

import html
from pathlib import Path

PASTA = Path("about/images/galeria")
LEGENDAS = PASTA / "legendas.txt"
EXTENSOES = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg", ".avif"}

PASTA.mkdir(parents=True, exist_ok=True)


def ler_legendas():
    mapa = {}
    if not LEGENDAS.exists():
        return mapa
    for linha in LEGENDAS.read_text(encoding="utf-8").splitlines():
        linha = linha.strip()
        if not linha or linha.startswith("#"):
            continue
        partes = [p.strip() for p in linha.split("|")]
        if len(partes) >= 3:
            mapa[partes[0]] = (partes[1], partes[2])
    return mapa


legendas = ler_legendas()

for lang in ("pt", "en"):
    linhas = ["```{=html}"]
    for arquivo in sorted(PASTA.iterdir()):
        if arquivo.suffix.lower() not in EXTENSOES:
            continue
        padrao = arquivo.stem.replace("-", " ").replace("_", " ")
        par = legendas.get(arquivo.name, (padrao, padrao))
        legenda = html.escape(par[0] if lang == "pt" else par[1])
        linhas.append(
            f'<button class="gallery-thumb" type="button" data-caption="{legenda}">'
            f'<img src="images/galeria/{arquivo.name}" alt="{legenda}" loading="lazy">'
            f"</button>"
        )
    linhas.append("```")
    conteudo = "\n".join(linhas) + "\n"

    destino = Path(f"about/_galeria.{lang}.qmd")
    # só regrava quando o conteúdo muda, para não invalidar o cache do Quarto
    if not destino.exists() or destino.read_text(encoding="utf-8") != conteudo:
        destino.write_text(conteudo, encoding="utf-8")
