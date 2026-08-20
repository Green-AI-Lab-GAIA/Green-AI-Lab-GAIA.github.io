# GAIA Lab — site

Site do grupo, feito com [Quarto](https://quarto.org). O conteúdo é **bilíngue**:
cada página existe em dois arquivos, `*.pt.qmd` (português, publicado na raiz)
e `*.en.qmd` (inglês, publicado em `/en/`). Os perfis `_quarto-pt.yml` e
`_quarto-en.yml` definem a navbar e o destino de cada idioma.

> **As 5 regras de ouro**
> 1. Edite sempre os arquivos `.qmd` — **nunca** o HTML dentro de `docs/` (é gerado).
> 2. Toda página tem **duas versões**: `.pt.qmd` e `.en.qmd`. Edite as duas.
> 3. Rode `./scripts/build.sh` **antes de commitar** — a pasta `docs/` vai junto no commit e é o que o site publica.
> 4. Datas no campo `date:` sempre no formato `AAAA-MM-DD` (ordena as listagens e alimenta o filtro de ano).
> 5. Deixe `summary`/`snippet` em **uma linha só** — quebrar em várias linhas costuma quebrar o build (erro de YAML).

---

## Índice

- [Instalação](#instalação)
- [Compilar o site](#compilar-o-site)
- [Rodar o servidor local](#rodar-o-servidor-local)
- [Atualizar o perfil de alguém](#atualizar-o-perfil-de-alguém)
- [Adicionar um novo membro](#adicionar-um-novo-membro)
- [Adicionar foto com legenda à galeria](#adicionar-foto-com-legenda-à-galeria)
- [Adicionar uma notícia](#adicionar-uma-notícia)
- [Adicionar um artigo](#adicionar-um-artigo)
- [Mapa das pastas](#mapa-das-pastas)

---

## Instalação

Requer o **[Quarto CLI](https://quarto.org/docs/get-started/)** e o **Python 3**
(que já vem na maioria dos Linux/Mac). Confirme que o Quarto está instalado:

```sh
quarto --version
```

Se o comando não for encontrado, verifique se o Quarto está no `PATH`
(numa instalação sem administrador ele costuma ficar em `~/.local/bin`).

---

## Compilar o site

Gera o site completo (os dois idiomas) na pasta `docs/`:

```sh
./scripts/build.sh
```

Esse script faz tudo de uma vez: monta a galeria a partir das fotos, renderiza
o português (na raiz) e o inglês (em `/en/`), tira o sufixo de idioma das URLs
e versiona o CSS para o navegador não usar uma versão antiga do cache. **Rode-o
sempre antes de commitar.**

Para **editar com recarga automática** (útil enquanto escreve), use o preview —
mas ele mostra só um idioma por vez:

```sh
quarto preview                # português
quarto preview --profile en   # inglês
```

> O `quarto preview` apaga o diretório do outro idioma de `docs/`. Por isso,
> quando terminar de editar, rode `./scripts/build.sh` para regenerar tudo.

---

## Rodar o servidor local

Para ver o site completo (com o botão PT/EN funcionando), sirva a pasta `docs/`:

```sh
./scripts/build.sh
python3 -m http.server 4200 --directory docs
```

Depois abra **http://localhost:4200** no navegador. Se a página parecer
desatualizada, force o recarregamento com **Ctrl+Shift+R**.

Para **desligar o servidor**: `Ctrl+C` no terminal onde ele está rodando.
Se ele tiver ficado "solto" (Ctrl+C não resolve), mate pela porta:

```sh
fuser -k 4200/tcp      # encerra o que estiver na porta 4200
```

---

## Atualizar o perfil de alguém

Edite os **dois** arquivos da pessoa em `people/nome-sobrenome/`:
`nome-sobrenome.pt.qmd` e `nome-sobrenome.en.qmd`. Os campos que importam ficam
no topo (entre os `---`):

| Campo | O que é | Exemplo |
|---|---|---|
| `people_group` | Define **em qual seção** a pessoa aparece | `masters` |
| `subtitle` | Cargo no GAIA Lab | `Assistente de Pesquisa` |
| `education` | Linha de formação que aparece no card | `Mestrando em X, FGV EMAp` |
| `image` | Nome do arquivo da foto (na mesma pasta) | `avatar.jpeg` |

Valores possíveis de `people_group` (também definem a **ordem** das seções):
`professor`, `postdoc`, `phd`, `masters`, `undergrad`, `alumni`.
Ex.: alguém que terminou o mestrado e virou doutorando muda de `masters` para
`phd`; quem deixou o grupo vira `alumni`.

O corpo do arquivo tem a **biografia** (2 a 4 frases), a seção **Formação**
(uma linha por grau; se estiver em andamento, use o gerúndio: *Graduando,
Mestrando, Doutorando*) e a seção **Interesses**.

**Trocar a foto:** substitua o arquivo mantendo o mesmo nome, ou aponte o campo
`image:` para o novo arquivo. Recorte-a em quadrado (1:1); veja os detalhes na
seção seguinte.

Ao final, rode `./scripts/build.sh`.

---

## Adicionar um novo membro

1. Crie a pasta `people/nome-sobrenome/`.
2. Coloque a foto lá dentro (ex.: `avatar.jpeg`). **Sem foto ainda?** Copie
   `images/avatar-default.svg` para dentro da pasta como `avatar.svg` — o site
   usa um avatar genérico até chegar a foto real.
3. Copie os modelos `people/_template.pt.qmd` e `people/_template.en.qmd` para
   dentro da pasta, renomeando para `nome-sobrenome.pt.qmd` e
   `nome-sobrenome.en.qmd`.
4. Preencha os campos e o texto nos dois arquivos (veja a tabela da seção
   anterior).
5. Rode `./scripts/build.sh`. A pessoa aparece automaticamente na seção do seu
   `people_group`, em ordem alfabética.

**Sobre a foto:** envie recortada em **quadrado (1:1)** — o que você recortar é
exatamente o que aparece no rol (quadrado) e no perfil (círculo). Use jpg, png
ou webp, no mínimo 800×800 px (ideal 1200×1200) e até ~500 KB. Fotos fora do
1:1 também funcionam (o site recorta sozinho, priorizando o topo), mas o 1:1 dá
o melhor resultado.

---

## Adicionar foto com legenda à galeria

A galeria da página **Sobre** é montada sozinha a partir da pasta
`about/images/galeria/`.

1. Solte o arquivo de imagem (jpg, png, webp, gif, svg, avif) em
   `about/images/galeria/`.
2. Abra `about/images/galeria/legendas.txt` e adicione **uma linha** no formato:

   ```
   nome-do-arquivo | legenda em português | caption in English
   ```

   Exemplo:

   ```
   fim-de-ano-2025.jpeg | Confraternização de fim de ano, 2025 | End-of-year gathering, 2025
   ```

   Fotos sem linha no `legendas.txt` usam o nome do arquivo como legenda.
3. Rode `./scripts/build.sh`. As fotos entram em ordem alfabética de nome de
   arquivo; passam sozinhas a cada 10 s, e clicar amplia (com zoom).

---

## Adicionar uma notícia

As notícias ficam **dentro** das páginas de publicações, não em pastas
separadas. Acrescente um item na lista `news`, no topo de **ambos**
`publications/index.pt.qmd` e `publications/index.en.qmd`:

```yaml
      - title: "Título da notícia"
        path: "https://link-da-materia"
        date: 2026-05-20
        news-source: "FGV"
        news-date: "20 de maio de 2026"
        image: "images/nome-da-foto.jpg"
        summary: "Um resumo curto em uma única linha."
```

- `date` (`AAAA-MM-DD`) ordena a lista e alimenta o filtro de ano; `news-date`
  é o texto que aparece na tela.
- A foto vai em `publications/images/`. Se não tiver imagem, omita a linha
  `image:` — o card funciona sem foto.
- Mantenha o `summary` em **uma linha só**.

A busca, o filtro de ano e a paginação se ajustam sozinhos. Rode
`./scripts/build.sh` ao final.

---

## Adicionar um artigo

1. Crie a pasta `publications/nome-do-artigo/`.
2. Coloque a miniatura da primeira página do PDF como `thumbnail.png`. **Sem PDF
   de acesso aberto?** Copie `images/paper-default.svg` para a pasta como
   `thumbnail.svg` (uma miniatura esquemática neutra).
3. Copie `publications/_template.pt.qmd` e `publications/_template.en.qmd` para
   a pasta, renomeando para `nome-do-artigo.pt.qmd` e `nome-do-artigo.en.qmd`.
4. Preencha, nos dois arquivos, os campos do topo (título, autores, `date`,
   `venue`, `image`, `snippet`) e o corpo (resumo, citação BibTeX, link).
5. Rode `./scripts/build.sh`. O artigo entra na lista automaticamente, ordenado
   pela `date` (mais recente primeiro).

**Figuras do artigo (opcional):** coloque a(s) imagem(ns) na pasta e use o
bloco `.pub-figures`, entre o resumo e a citação. Uma figura ocupa a largura
toda; duas ficam lado a lado. As figuras são clicáveis (abrem com zoom).

```markdown
:::: {.pub-figures}
![Legenda explicando a figura](figura-1.png)
::::
```

A legenda aceita **fórmulas em LaTeX** entre cifrões — ex.: `$\alpha = 0.2$` —
que são renderizadas automaticamente.

---

## Mapa das pastas

```
├── _quarto.yml            Configuração comum aos dois idiomas
├── _quarto-pt.yml         Navbar e rodapé em português (publica na raiz)
├── _quarto-en.yml         Navbar e rodapé em inglês (publica em /en)
├── styles.css             Estilos do site
├── scripts/
│   ├── build.sh           Gera o site completo (rode este antes de commitar)
│   ├── gen_gallery.py     Monta a galeria a partir das fotos + legendas.txt
│   └── flatten_lang.py    Ajusta URLs e versiona o CSS (pós-build)
├── _includes/             Trechos de JavaScript (galeria, zoom, filtros, etc.)
├── _ejs/                  Modelos dos cards (equipe, publicação, notícia)
├── index.{pt,en}.qmd      Página inicial
├── about/                 Sobre (inclui a galeria: images/galeria/)
├── research/              Pesquisa
├── courses/               Cursos
├── join-us/               Junte-se a nós
├── people/                Um diretório por membro; _template.* para novos
├── publications/          Um diretório por artigo; index.* traz as notícias
└── docs/                  SAÍDA GERADA — não edite à mão
```

> Os PDFs do LinkedIn e a pasta `perfis/` (usados só como fonte para escrever os
> perfis) contêm dados pessoais e **não** entram no repositório — já estão no
> `.gitignore`.
