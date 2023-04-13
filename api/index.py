from flask import Flask, request
import json
import telegram
from telegram.ext import Updater , CommandHandler , Filters , MessageHandler
import time


TOKEN = "5858379831:AAGLpbVbx0TRGk5ctcch3dKvcOx4JrmBhuA"
HOST="https://fv-test.vercel.app"
global bot
bot = telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)
#bot.deleteWebhook()"
HOST="https://tg-bot-test-2.vercel.app"
global bot
bot = telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)
#bot.deleteWebhook()

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'
