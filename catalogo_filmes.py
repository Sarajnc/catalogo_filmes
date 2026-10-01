import csv
import os
import re
import webbrowser
import bs4
import requests

URL = "https://pt.wikipedia.org/wiki/"
HEADERS = {"User-Agent": "Mozilla/5.0"} 
ARQUIVO = "historico_filmes.csv"

def buscar_filme(nome):
    palavras = nome.strip().split()
    termo = "_".join(palavras)
    
    url_final = URL + termo
    resposta = requests.get(url_final, headers=HEADERS)
    
    if resposta.status_code != 200:
        print(f"Erro ao buscar filme! (Código: {resposta.status_code})")
        return None

    soup = bs4.BeautifulSoup(resposta.text, "html.parser")
    
    tabela = soup.find("table", {"class": "infobox"})
    if not tabela:
        print("Infobox não encontrada na página.")
        return None

    ficha = {}
    for linha in tabela.find_all("tr"):
        rotulo = linha.find("th")
        valor = linha.find("td")
        if rotulo and valor:
            ficha[rotulo.text.strip()] = valor.get_text(", ", strip=True)

    def achar_campo(palavra):
        for r, v in ficha.items():
            if palavra in r:
                return v
        return "-"

    lancamento = achar_campo("Lançamento")
    ano_match = re.search(r"\d{4}", lancamento)
    ano = ano_match.group(0) if ano_match else "-"

    return {
        "titulo": soup.find("h1").text,
        "ano": ano,
        "genero": achar_campo("Gênero"),
        "direcao": achar_campo("Direção"),
        "link": resposta.url
    }

def mostrar(filme):
    print("\nFilme Encontrado")
    print("Título:", filme["titulo"])
    print("Ano:", filme["ano"])
    print("Gênero:", filme["genero"])
    print("Direção:", filme["direcao"])

def salvar(historico):
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=["titulo", "ano", "genero", "direcao", "link"])
        escritor.writeheader()
        escritor.writerows(historico)

def main():
    historico = []
    
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, newline="", encoding="utf-8") as f:
            historico = list(csv.DictReader(f))

    while True:
        print("\n1. Buscar filme")
        print("2. Ver histórico")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do filme: ")
            filme = buscar_filme(nome)
            if filme:
                mostrar(filme)
                salvar_op = input("Deseja salvar no histórico? (s/n): ")
                if salvar_op.lower() == "s":
                    historico.append(filme)
                    salvar(historico)
                    print("Salvo com sucesso!")

                abrir = input("Deseja abrir o link no navegador? (s/n): ")
                if abrir.lower() == "s":
                    webbrowser.open(filme["link"])

        elif opcao == "2":
            if len(historico) == 0:
                print("Histórico vazio.")
            else:
                print("\n--- Histórico de Filmes ---")
                for f in historico:
                    print(f"{f['titulo']} ({f['ano']}) - {f['genero']}")

        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()