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



