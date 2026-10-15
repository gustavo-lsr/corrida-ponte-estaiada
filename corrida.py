idade_minima = 16
"""Corrida da Ponte Estaiada - Etapa 1
      Inscrição e resultado de um corredor por vez.
"""


def calcular_valor_incricao(idade, distancia, lote):
    """Calcula o valor da inscrição em reais.

    Regras de negócio:
    1º lote: R$80,00; 2º lote: R$100,00.
    Provas de 5 km têm valor padrão; provas de 10 km têm acréscimo de R$20,00.

        Parâmetros:
            idade: Idade do corredor.
            distancia: Distância da prova, em quilômetros (5 ou 10).
            lote: Lote de inscrição (1 ou 2).
        """
    if lote == 1:
                valor = 80.0
    else:
                valor = 100.0

    if distancia == 10:
        valor += 20.0
    if idade >= 60:
        valor /= 2
    return valor 