import telebot
import database

TOKEN = "add your own telegram bot token"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start_message(m):
    bot.send_message(m.chat.id,"Hello there")

@bot.message_handler(content_types=["location"])
def location_received(m):
    print(m)
    bot.send_message(m.chat.id,"Location received")
    bot.send_message(m.chat.id,"Searching for nearest AED...")
    nearestAED = database.get_nearest_aed(m.location.latitude,m.location.longitude)
    bot.send_location(m.chat.id,nearestAED[0],nearestAED[1])
    bot.send_message(m.chat.id,"Here is the location of the nearest AED")

bot.polling()