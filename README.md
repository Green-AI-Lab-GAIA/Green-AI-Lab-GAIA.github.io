# GAIA Lab — site

Site do grupo, feito com [Quarto](https://quarto.org). O conteúdo é bilíngue:
cada página existe em dois arquivos, `*.pt.qmd` (português, publicado na raiz)
e `*.en.qmd` (inglês, publicado em `/en/`). Os perfis `_quarto-pt.yml` e
`_quarto-en.yml` definem a navbar e o destino de cada idioma.

## Desenvolvimento local

Requer o [Quarto CLI](https://quarto.org/docs/get-started/) instalado.

```sh
# Editar com recarga automática, um idioma por vez
quarto preview                # português
quarto preview --profile en   # inglês

# Gerar o site completo (docs/, os dois idiomas) e conferir com o botão PT/EN
./scripts/build.sh
python3 -m http.server 4200 --directory docs
```

O `quarto preview` renderiza apenas o idioma do perfil ativo e apaga o
diretório do outro idioma de `docs/` — por isso, rode `./scripts/build.sh`
antes de commitar. O GitHub Pages publica o conteúdo de `docs/`, que é
gerado: edite sempre os arquivos `.qmd`, nunca o HTML.

## Adicionar fotos à galeria do Sobre

Solte os arquivos de imagem (jpg, png, webp, gif, svg, avif) em
`about/images/galeria/` e rode o build — a galeria é montada sozinha, em
ordem alfabética de nome de arquivo. A foto oficial do grupo é o arquivo
`about/images/foto-oficial.jpg` (substitua mantendo o nome).

## Adicionar um membro da equipe

Crie a pasta `people/nome-sobrenome/` com a foto e copie os modelos
`people/_template.pt.qmd` e `people/_template.en.qmd` para dentro dela,
renomeando para `nome-sobrenome.pt.qmd` e `nome-sobrenome.en.qmd`.
