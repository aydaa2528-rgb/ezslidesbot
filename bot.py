import telebot

TOKEN = "8764664211:AAGtBNQ10Ml97myFxj1NK1PrremIZXa70-E"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "أهلاً بك في بوت EZ Slides 📚\nأرسل صورة وسأحولها إلى بوربوينت قريبًا.")

@bot.message_handler(content_types=['photo'])
def photo(message):
    bot.reply_to(message, "تم استلام الصورة ✅")

print("Bot Running...")
bot.infinity_polling()
