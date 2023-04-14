from flask import Flask, request
import json
import telegram
from telegram.ext import Updater , CommandHandler , Filters , MessageHandler
import time


TOKEN = "5858379831:AAGLpbVbx0TRGk5ctcch3dKvcOx4JrmBhuA"
HOST="https://fv-test.vercel.app"
bot = telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)


def greet(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="Hello there")


app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook_handler(pdate, context):
   # global updater
    
    ##if request.method == "POST":
        #global content #WORKING
        #content=request.json
        #content = json.loads(request.get_data())# #WORKING
       
        #chat_id = request.json["message"]["chat"]["id"]
        print(content)
    chat_id="1093497662"# msg.sender_chat["username"]
    update = telegram.update.Update.de_json(request.get_json(force=True))
    bot.sendMessage(chat_id=chat_id, text=str(update))
    return 'ok'


@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    bot.deleteWebhook()
    time.sleep(2)
    s = bot.setWebhook(f"https://fv-test.vercel.app/{TOKEN}") #WORKING without token 
    #s=requests.get(f'https://api.telegram.org/bot{TOKEN}/setWebHook?url={HOST}/{TOKEN}>&allowed_updates=["callback_query","message"]') #without token
    
    if s:
        return str(bot.getWebhookInfo())
    else:
        return "webhook setup failed"
