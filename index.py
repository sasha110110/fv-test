from flask import Flask, request
import json
import telegram
from telegram.ext import Updater , CommandHandler , Filters , MessageHandler
import time

update=telegram.Update
context=telegram.ext.CallbackContext

TOKEN = "6008314594:AAE1RO_UMtHDMw9VtVFt-3xmh-JsDj8paGY"

HOST="https://fv-test.vercel.app"

bot = telegram.Bot(token=TOKEN)

def hello(update, context):
    chat_id="1093497662"# msg.sender_chat["username"]
    bot.sendMessage(chat_id=chat_id, text="test")
   
   
updater = Updater(TOKEN)

dp = updater.dispatcher


   
greet_handler=CommandHandler("start", hello)
dp.add_handler(greet_handler)
    
    
updater.start_webhook(listen="0.0.0.0",
                       port=443,
                       url_path=TOKEN, 
                      webhook_url='https://test-with-hook.vercel.app/' + TOKEN))
