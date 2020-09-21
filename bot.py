import telebot
from bs4 import BeautifulSoup
import urllib.request

# идентификаторы бота и вашего с ним чата
token = '1387684993:AAGnkjRcM5DkgE5-9LWTt-8_wqECrwQtu6o'
chat_id = 355747941

# создаем экземпляр бота
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == '/test':
        # делаем запрос к сайту
        resp = urllib.request.urlopen("https://www.pmedpharm.ru/studentu_ochniku/pervyiy_kurs_ochnick/")
        soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))

        for link in soup.find_all('a', href=True):
            #получаем определенную ссылку из списка и сохраняем в переменную
            if '/content/newcont/files/%D0%A0%D0%B0%D1%81%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5%205%20%D0%BA%D1%83%D1%80%D1%81%D0%B0%20%D0%BE%D1%81%D0%B5%D0%BD%D1%8C%202020%20%D0%A4%D0%B0%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B4%D0%B8%D1%81%D1%82%D0%B0%D0%BD%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D0%BE%D0%B5%282%29.pdf' in link['href']:
                s = link['href']

        try:
            if s == '/content/newcont/files/%D0%A0%D0%B0%D1%81%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5%205%20%D0%BA%D1%83%D1%80%D1%81%D0%B0%20%D0%BE%D1%81%D0%B5%D0%BD%D1%8C%202020%20%D0%A4%D0%B0%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B4%D0%B8%D1%81%D1%82%D0%B0%D0%BD%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D0%BE%D0%B5%282%29.pdf':
                bot.send_message(chat_id, 'Cсыль есть')
        except:
            bot.send_message(chat_id, 'Cсыль отлетела, пора обновлять')


    else:
        bot.send_message(chat_id, 'Саси')


bot.polling()
