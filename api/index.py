from flask import Flask, request
import json
import telegram
from telegram.ext import Updater , CommandHandler , Filters , MessageHandler
import time


TOKEN = "5858379831:AAGLpbVbx0TRGk5ctcch3dKvcOx4JrmBhuA"
HOST="https://fv-test.vercel.app"
bot = telegram.Bot(token=TOKEN)
#updater = Updater(token=TOKEN, use_context=True)

app = Flask(__name__)

#@app.route('/')
#def home():
 #   return 'Hello, World!'

@app.route('/test')
def test():
    chat_id="@1093497662"# msg.sender_chat["username"]
  
    bot.sendMessage(chat_id=chat_id, text="test")
    


@app.route('/') #5858379831:AAGLpbVbx0TRGk5ctcch3dKvcOx4JrmBhuA', methods=['POST'])
def index():
    global bot
   # global updater
    
    if request.method == "POST":
        global content #WORKING
        content = json.loads(request.get_data())# #WORKING
       
        #chat_id = request.json["message"]["chat"]["id"]
        chat_id="@1093497662"# msg.sender_chat["username"]
  
        bot.sendMessage(chat_id=chat_id, text=str(content))

    return 'ok'


@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    global bot
    bot.deleteWebhook()
    time.sleep(2)
    s = bot.setWebhook(f"https://fv-test.vercel.app/{TOKEN}") #WORKING without token 
    #s=requests.get(f'https://api.telegram.org/bot{TOKEN}/setWebHook?url={HOST}/{TOKEN}>&allowed_updates=["callback_query","message"]') #without token
    
    if s:
        return str(bot.getWebhookInfo())
    else:
        return "webhook setup failed"
