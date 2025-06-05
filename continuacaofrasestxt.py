with open("frases.txt", "r", encoding="utf-8") as f:
    linhas = f.readlines()

with open("contagem.txt", "w", encoding="utf-8") as f:
    for i, linha in enumerate(linhas, start=1):
        linha = linha.strip()
        palavras = linha.split()
        quantidade_palavras = len(palavras)
        f.write(f"Linha {i}: {quantidade_palavras} palavras\n")
