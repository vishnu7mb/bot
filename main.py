import vishnu as keys
from  telegram.ext import *
import Responses as R



print(" bot started....")
def start_command(update,context):
    update.message.reply_text("type somthing...")

def start_help(update, context):
    update.message.reply_text("if need somthing ask me")

def handle_message(update,comtext):
    text = str(update.message.text).lower()
    response = R.sample_respons(text)

    update.message.reply_text(response)

def error(update,context):
    print(f"update {update} caused error {context.error}")



def main():
    updater = Updater(keys.API_KEY,use_context= True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("help", handle_message))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()



main()

