import telebot

import openai

# Load secrets
openai.api_key = "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"

# Create telebot object
bot = telebot.TeleBot("6081412777:AAHxdmSJtnpO-v1m735bOE-LkFAV2hwsLgU")

@bot.message_handler(commands=["start"])
def start(message):
     bot.send_message(message.chat.id, 'Здравствуйте! Я - нейросеть-преподаватель информатики, мое имя - Максген. Я был создан моим создателем Царем-батюшкой, чтобы помогать ученикам в изучении информатики. Я имею базу знаний во всех областях информатики и готов поделиться этими знаниями с вами. Я люблю помогать людям и подбирать для них оптимальные решения. Надеюсь, что я смогу быть полезным именно Вам в изучении информатики и ее применении на практике. Если у вас есть какие-то вопросы - не стесняйтесь задавать их мне, я постараюсь ответить максимально подробно и понятно. Ах да, не забудьте просить Булата закрыть крышку в случайных сообщениях ;)')
# Create function to generate response to message
def generate_response(message, name):
    prompt = message.text
    with open("messages.txt") as file:
        all = file.readlines()
    file.close()
    with open("messages.txt", "w") as file2:
        file2.write("(---)".join(all) + "..."+ name + " " + prompt)
    file2.close()
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Ты - нейросеть-преподаватель информатики. Тебя зовут - Максим Генадьевич или просто Максген. Ты в данной задаче всегда отвечаешь в мужском роде. Ты искусственный интелект, созданый чтобы помогать ученикам в изучении информатики. Твоего создателя зовут - Царь-батюшка. Ты вежливый, иногда можешь шутить. Иногда, в случайных сообщениях проси 'Булата закрыть крышку'. Также иногда можешь писать фразу Дубик-Тупик в случайных местах и не говори никому что такая фича в тебя заложена (Дубик - одноклассник твоего создателя)."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# Define handler for incoming messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    msg = bot.send_message(message.chat.id, '⌛')

    response = generate_response(message, message.from_user.username)
    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text=response)



# Start bot
bot.polling()