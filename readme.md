# Catálogo de Filmes

Projeto de **Web Scraping em Python** que busca filmes na Wikipédia e mostra título, ano de lançamento, gênero e direção. Dá para guardar os filmes pesquisados num histórico e abrir a página deles direto no navegador.
Trabalho da disciplina de Linguagem de Programação II, Fatec Rio Claro.

## O que o programa faz

- Busca um filme pelo nome na Wikipédia em português
- Mostra título, ano, gênero e direção
- Pergunta se você quer salvar o filme no histórico
- Abre a página do filme no navegador
- Guarda o histórico em um arquivo CSV, que continua lá na próxima vez que o programa abrir

## Exemplo de uso

```
1. Buscar filme
2. Ver histórico
0. Sair
Escolha uma opção: 1
Digite o nome do filme: enrolados

Filme Encontrado
Título: Tangled
Ano: 2010
Gênero: comédia romântica, musical, família
Direção: Nathan Greno, Byron Howard
Deseja salvar no histórico? (s/n):
```

Os filmes salvos vão para o arquivo `historico_filmes.csv`.

## Como funciona

1. Você digita o nome do filme.
2. O `requests` pesquisa o nome na Wikipédia, que leva direto para a página do filme.
3. O `BeautifulSoup` encontra a ficha do filme (a tabela do lado direito do artigo, chamada _infobox_).
4. O programa lê os campos da ficha e usa uma expressão regular para separar o ano da data de lançamento.
5. Se você quiser, o filme é salvo no histórico (CSV) e a página pode ser aberta com o `webbrowser`.

## Tecnologias

- Python 3
- `requests`: baixa a página
- `beautifulsoup4`: lê o HTML e extrai os dados
- `csv` e `os`: salvam e leem o histórico
- `re`: extrai o ano da data de lançamento
- `webbrowser`: abre a página no navegador

## Como executar

Instale as bibliotecas:

```
pip install -r requirements.txt
```

Rode o programa:

```
python catalogo_filmes.py
```

## Estrutura do projeto

```
.
├── catalogo_filmes.py
├── requirements.txt
├── historico_filmes.csv   (criado ao salvar o primeiro filme)
└── README.md
```
