# import requests

# url = "https://api.telegram.org/bot1198450995:AAFSYFr_s3EyB3DpNdFcKQyUYdZLGwZuubU/getUpdates"

# payload = "{\n    \"allowed_updates\": [\"messages\"]\n}"
# headers = {
#   'Content-Type': 'application/json'
# }

# response = requests.request("GET", url, headers=headers, data = payload)

# print(response.text.encode('utf8'))

import telepot
from conf.settings import BASE_API_URL, TELEGRAM_TOKEN

posto_medico = 'médico médicos medico medicos'
posto_keywords = 'posto postos banheiro banheiros gasolina abastecer'
parada_keywords = 'parada paradas descanso'
food = 'comida fome'
suadacao = 'olá ola oi'

url = 'https://lh3.googleusercontent.com/proxy/qH7BN1TrlFoAJj5bGUmjaVWMBmMGKoH6mgOtd18g7udoDCG-x5yyS1fLSw_UBqu70DL4x8LOQOyYh0YCtzyIu7qGY3TdnykjHqdksYezYwS8tGEi3qi1zOq5hUljjJBNjmfex0jYrTHjeQ'

help_msg = ("Me desculpe {}, não lhe compreendi, mas posso lhe ajudar com as seguintes coisas:\n\n"
            "Veja as opções abaixo e escolha uma! :)\n\n"
            "Digite /saude - PARA SABER ALGO RELACIONADO AO BEM ESTAR\n"
            "Digite /paradas - PARA SABER AS PARADAS MAIS PRÓXIMAS\n"
            "Digite /pontosCcr - PARA SABER OS PONSTOS DA CCR MAIS PRÓXIMOS\n"
            "Digite /postos - PARA SABER OS POSTOS MAIS PRÓXIMOS")


def resposta(msg):
    texto = msg['text']
    _id = msg['from']['id']
    name = msg['from']['first_name']

    if texto == '/start':
        bot.sendMessage(_id, "Olá {} Este é o novo canal de comunicação da CCR para auxiliá-lo.\n"
                        "Por aqui podemos nos comunicar e oferecer informações úteis para melhorar sua estadia em nossas estradas.\n"
                        "Vamos nos conhecer melhor, eu sou o TrukBot da CCR.\n\n"
                        "Como posso lhe ajudar hoje?".format(str(name)))
        return
    elif texto == '/proximos':
        bot.sendMessage(_id, "proximos {}".format(str(name)))
        return
    elif texto == '/banheiros':
        bot.sendMessage(_id, "banheiros {}".format(str(name)))
        return
    elif texto == '/saude':
        bot.sendMessage(_id, "{}, Escolha qual opção abaixo se adequa a sua necessidade medica!?\n\n"
                        "[1] - Local de apoio mais próximo da CCR\n"
                        "[2] - Exames ou informações de hoje".format(str(name)))
        return
    elif texto == '2':
        bot.sendMessage(_id, "{}, Para sua comodidade hoje estamos promovendo uma campanha de exames preventivos no Km 187, faltam só 23 Km,  em um kiosk no Posto XYZ.\n"
                        "Passe lá para fazer um exame de glicemia, é rápido e em poucos minutos sairá com resultado.\n"
                        "Participe.".format(str(name)))
        return
    elif texto == '/descanso':
        bot.sendMessage(_id, "descanso {}".format(str(name)))
        return
    elif texto == '/help':
        bot.sendMessage(_id, help_msg.format(str(name)))
        return
    elif texto == '/pontosCcr':
        bot.sendMessage(_id, help_msg.format(str(name)))
        return
    elif texto == '/postos':
        bot.sendMessage(_id, help_msg.format(str(name)))
        return
    elif texto == '/socorro':
        bot.sendMessage(_id, "{} Com base sua localização a emergência foi acionada!".format(str(name)))
        return

    words = texto.split()

    for word in words:
        word = word.lower()
        if word in suadacao:
            bot.sendMessage(_id, "Olá {}, qual sua duvida hoje?".format(str(name)))
            return
        elif word in posto_keywords:
            bot.sendMessage(_id, "Bem você falou em posto, para entender melhor o que você deseja\n"
                            "Veja as opções abaixo e escolha uma! :)\n\n"
                            "Digite /proximos - PARA SABER OS POSTOS MAIS PROXIMOS\n"
                            "Digite /banheiros - QUAIS POSTOS TEM BANHEIRO GRATUITO")
            return
        elif word in parada_keywords:
            bot.sendMessage(
                _id, "Bem, você falou em paradas, para entender melhor o que você deseja\n"
                     "veja as opções abaixo e escolha uma! :)\n\n"
                     "Digite /medicos - PARA SABER ONDE ENCONTRAR AJUDA MÉDICA\n"
                     "Digite /descanso - PARA SABER O PONTO MAIS PRÓXIMO ONDE DESCANSAR")
            return
        elif word in posto_medico:
            bot.sendMessage(
                _id, "Bem, você falou em Médicos, para entender melhor o que você deseja\n"
                     "veja as opções abaixo e escolha uma! :)\n\n"
                     "Digite /saude - PARA SABER ONDE ENCONTRAR AJUDA MÉDICA\n"
                     "Digite /descanso - PARA SABER O PONTO MAIS PRÓXIMO ONDE DESCANSAR\n"
                     "Digite /acidente - PARA ENVIARMOS SOCORRO!")
            return
        elif word in food:
            bot.sendMessage(
                _id, "Bem, Temos dois restaurantes nos próximos 35 Km, um na margem direita chamado XXXXX e outro na margem esquerda, chamado YYYYYY,\n"
                "que poderá ser acessado pelo retorno que fica no Km 345.\n\n"
                "Vou enviar a localização!! :) ")
            bot.sendPhoto(_id, url)
            return

    bot.sendMessage(_id, help_msg.format(str(name)))
    return


bot = telepot.Bot(TELEGRAM_TOKEN)
bot.message_loop(resposta)

while True:
    pass
