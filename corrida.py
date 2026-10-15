idade_minima = 16
"""Corrida da Ponte Estaiada - Etapa 1
      Inscrição e resultado de um corredor por vez.
"""


def calcular_valor_inscricao(idade, distancia, lote):
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

def selecionar_categoria(idade):
    """Selecionar a categoria do corredor baseado na sua idade.
          Juvenil: 16 a 19 anos;
          Adulto: 20 a 39 anos;
          Master: 40 a 59 anos;
          Veterano: 60 anos ou mais.
       """
    if idade < 16:
           return "Não permitido"
    elif idade <= 19:
           return "Juvenil"
    elif idade <= 39:
           return "Adulto"
    elif idade <= 59:
           return "Master"
    else: 
           return "Veterano"


def informar_primeiro_nome(nome_completo):
  """retorna o primeiro nome;"""
  nome = nome_completo.strip()
  posicao = nome.find(" ")
  if posicao == -1:
    return nome
  return nome[:posicao]


def informar_ultimo_nome(nome_completo):
  """retorna o ultimo nome;"""
  nome = nome_completo.strip()
  posicao = nome.rfind(" ")
  return nome[posicao + 1:]



def gerar_codigo(nome_completo, idade):
  """gera o código do corredor
     3 primeiras letras do primeiro nome(maiúsculas) + 3 primeiras letras do último nome(maiúsculas) + idade;
     exemplo: "Gustavo Patricio Silva", 21 --> 'GUSSIL21';"""
  
  primeiro = informar_primeiro_nome(nome_completo)
  ultimo = informar_ultimo_nome(nome_completo)
  return primeiro[:3].upper() + ultimo[:3].upper() + str(idade)

def tempo_valido(tempo):
    """Retorna True se o texto estiver no formato HH:MM:SS válido.
    O tempo é desmontado por fatiamento: horas [0:2], minutos [3:5], segundos [6:8]. Rejeita '1:02:59, '00h22m00s', minutos ou segundos acima de 59 e o tempo zerado.
    """
    if len(tempo) != 8:
         return False
    if tempo[2:3] != ":" or tempo[5:6] != ":":
        return False
    horas = tempo[0:2]
    minutos = tempo[3:5]
    segundos = tempo[6:8]
    if not (horas.isdecimal() and minutos.isdecimal() and segundos.isdecimal()):
        return False
    if int(minutos) > 59 or int(segundos) > 59:
        return False
    return int(horas) * 3600 + int(minutos) * 60 + int(segundos) > 0

def converter_tempo_para_segundos(tempo):
    """Converte um tempo válido 'HH:MM:SS' para segundos (int).
    """
    horas = int(tempo[0:2])
    minutos = int(tempo[3:5])
    segundos = int(tempo[6:8])
    return horas * 3600 + minutos * 60 + segundos

def calcular_pace(tempo_segundos, distancia):
    """Retorna o pace em segundos por km, desprezando frações de segundo.
    """
    return tempo_segundos // distancia

def formatar_pace(pace_segundos):
    """Formata o pace (segundos por km) como texto, ex.: 4'18\"/km.
    """
    return f"{pace_segundos // 60}'{pace_segundos % 60:02d}\"/km"


def formatar_reais(valor):
    """Formata um valor em reais com duas casas, ex.: 'R$ 80,00'.
    """
    return f"R$ {valor:.2f}".replace(".", ",")

def obter_tempo_limite(categoria, distancia):
    """Retorna o tempo-limite de premiação, em segundos.
 
    Juvenil e Master: 25:00 (5 km) e 52:00 (10 km)
    Adulto: 22:00 (5 km) e 46:00 (10 km)
    Veterano: 30:00 (5 km) e 1:03:00 (10 km)
    """
    if categoria == "Adulto":
        return 22 * 60 if distancia == 5 else 46 * 60
    if categoria == "Veterano":
        return 30 * 60 if distancia == 5 else 63 * 60
    return 25 * 60 if distancia == 5 else 52 * 60


def verificar_premiacao(categoria, distancia, tempo_segundos):
    """Retorna True se o tempo é menor ou igual ao limite da categoria.
    """
    return tempo_segundos <= obter_tempo_limite(categoria, distancia)


#LEITURA E VALIDAÇÃO DE ENTRADAS

def ler_nome():
    """Pede o nome completo até receber nome e sobrenome."""
    while True:
        nome = input("Nome completo: ").strip()
        if " " in nome:
            return nome
        print("Digite o nome completo (nome e sobrenome).")



def ler_idade():
    """Pede a idade até receber um inteiro entre 1 e 120."""
    while True:
        texto = input("Idade: ").strip()
        if texto.isdecimal() and 1 <= int(texto) <= 120:
            return int(texto)
        print("Idade inválida. Digite um número inteiro entre 1 e 120.")



def ler_opcao(pergunta, validas):
    """Pede um número até que esteja entre as opções válidas."""
    while True:
        texto = input(pergunta).strip()
        if texto.isdecimal() and int(texto) in validas:
            return int(texto)
        opcoes = " ou ".join(str(v) for v in validas)
        print(f"Opção inválida. Digite {opcoes}.")



def ler_tempo():
    """Pede o tempo até receber um HH:MM:SS válido."""
    while True:
        tempo = input("Tempo de prova (HH:MM:SS): ").strip()
        if tempo_valido(tempo):
            return tempo
        print("Tempo inválido. Use HH:MM:SS, com minutos e segundos até 59.")



#Ações do MENU

def fazer_inscricao():
    """Faz a inscrição. Retorna o valor pago, ou None se for recusada."""
    nome = ler_nome()
    idade = ler_idade()
    if idade < idade_minima:
        print(f"Inscrição recusada: idade mínima de {idade_minima} anos.\n")
        return None
    distancia = ler_opcao("Distância em km (5 ou 10): ", (5, 10))
    lote = ler_opcao("Lote (1 ou 2): ", (1, 2))
 
    valor = calcular_valor_inscricao(idade, distancia, lote)
    print("\n===== COMPROVANTE DE INSCRIÇÃO =====")
    print(f"Corredor : {informar_primeiro_nome(nome)}")
    print(f"Código   : {gerar_codigo(nome, idade)}")
    print(f"Categoria: {selecionar_categoria(idade)}")
    print(f"Distância: {distancia} km")
    print(f"valor    : {formatar_reais(valor)}")
    print("====================================\n")
    return valor


def calcular_resultado():
    """Lê os dados da prova e exibe o resultado."""
    idade = ler_idade()
    if idade < idade_minima:
        print(f"Não há categoria para menores de {idade_minima} anos.\n")
        return
    distancia = ler_opcao("Distância em km (5 ou 10): ", (5, 10))
    tempo = ler_tempo()
 
    categoria = selecionar_categoria(idade)
    segundos = converter_tempo_para_segundos(tempo)
    pace = calcular_pace(segundos, distancia)
    premiado = verificar_premiacao(categoria, distancia, segundos)
 
    print("\n===== RESULTADO =====")
    print(f"Categoria: {categoria}")
    print(f"Tempo    : {segundos} segundos")
    print(f"Pace     : {formatar_pace(pace)}")
    print(f"Premiado : {'Sim' if premiado else 'Não'}")
    print("=====================\n")




#Programa principal


def main():
    """Exibe o menu até o usuário sair e mostra o resumo da sessão."""
    total_inscricoes = 0
    total_arrecadado = 0.0
 
    while True:
        print("=== CORRIDA NOTURNA DA PONTE ESTAIADA ===")
        print("1 - Fazer inscrição")
        print("2 - Calcular resultado")
        print("3 - Sair")
        opcao = ler_opcao("Escolha uma opção: ", (1, 2, 3))
 
        if opcao == 1:
            valor = fazer_inscricao()
            if valor is not None:
                total_inscricoes += 1
                total_arrecadado += valor
        elif opcao == 2:
            calcular_resultado()
        else:
            print("\n===== RESUMO DA SESSÃO =====")
            print(f"Inscrições feitas: {total_inscricoes}")
            print(f"Total arrecadado : {formatar_reais(total_arrecadado)}")
            print("============================")
            break
 
 
if __name__ == "__main__":
    main()

