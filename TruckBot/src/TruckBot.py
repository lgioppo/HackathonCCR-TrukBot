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
parada_keywords = 'parada paradas descanso comida fome'
suadacao = 'olá ola oi'
help_msg = ("Me desculpe {}, não lhe compreendi, mas posso lhe ajudar com as seguintes coisas:\n\n"
            "Veja as opções abaixo e escolha uma! :)\n\n"
            "Digite /medicos - PARA SABER ONDE ENCONTRAR AJUDA MÉDICA\n"
            "Digite /descanso - PARA SABER O PONTO MAIS PRÓXIMO ONDE DESCANSAR\n"
            "Digite /proximos - PARA SABER OS POSTOS MAIS PROXIMOS\n"
            "Digite /banheiros - QUAIS POSTOS TEM BANHEIRO GRATUITO")


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
    elif texto == '/medicos':
        bot.sendMessage(_id, "{}, Bem para compreender melhor o que você deseja\n"
                        "Escolha qual opção abaixo se adequa a sua necessidade medica!?\n\n"
                        "[1] - Local de apoio mais próximo da CCR\n"
                        "[2] - Exames ou informações de hoje".format(str(name)))
        return
    elif texto == '/descanso':
        bot.sendMessage(_id, "descanso {}".format(str(name)))
        return
    elif texto == '/help':
        bot.sendMessage(_id, help_msg.format(str(name)))
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
                _id, "Bem, você falou em paradas, para entender melhor o que você deseja"
                     "veja as opções abaixo e escolha uma! :)\n\n"
                     "Digite /medicos - PARA SABER ONDE ENCONTRAR AJUDA MÉDICA\n"
                     "Digite /descanso - PARA SABER O PONTO MAIS PRÓXIMO ONDE DESCANSAR")
            return
        elif word in posto_medico:
            bot.sendMessage(
                _id, "Bem, você falou em Médicos, para entender melhor o que você deseja"
                     "veja as opções abaixo e escolha uma! :)\n\n"
                     "Digite /medicos - PARA SABER ONDE ENCONTRAR AJUDA MÉDICA\n"
                     "Digite /descanso - PARA SABER O PONTO MAIS PRÓXIMO ONDE DESCANSAR")
            return

    bot.sendMessage(_id, help_msg.format(str(name)))
    return


bot = telepot.Bot(TELEGRAM_TOKEN)
bot.message_loop(resposta)

while True:
    pass
