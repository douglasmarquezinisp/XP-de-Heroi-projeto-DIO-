# Espaço para solicitar a entrada do nome do Heroi e a Quantidade de XP
nome = input("Digite o nome do herói: ")
xp = int(input("Digite a experiência do herói (de 1 a 150000): "))

# Fiz a inclusão de nivel para não ter numero final infinito
if 1 <= xp <= 150000:
    # Aqui está a classificação de XP de acordo com a DIO solicitou
    if xp < 1000:
        nivel = "Ferro"
    elif 1001 <= xp <= 2000:
        nivel = "Bronze"
    elif 2001 <= xp <= 5000:
        nivel = "Prata"
    elif 6001 <= xp <= 7000:
        nivel = "Ouro"
    elif 7001 <= xp <= 8000:
        nivel = "Platina"
    elif 8001 <= xp <= 9000:
        nivel = "Ascendente"
    elif 9001 <= xp <= 10000:
        nivel = "Imortal"
    else: # XP é maior ou igual a 10001
        nivel = "Radiante"

    # Exibir mensagem de retorno com nome e nivel
    print(f"O Herói {nome} está no nível  {nivel}")
else:
    print("A experiência do herói deve estar entre 1 e 150000.")


