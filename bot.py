import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "8152348968:AAGo_GiGkefoYH3pILeAN8T6aySP2nV4Oxk")

API_ID = int(os.environ.get("API_ID", "19481274"))

API_HASH = os.environ.get("API_HASH", "edbb4d162c4871c25ccd6f7179dad8cf")

STRING = os.environ.get("STRING", "BQCEW4EeuFlxOgnqbBx6xIZDCjhEI8WNVt29Z6AtLL-OozpUF6et-QEt1Ujrj3z8xBgPYqfdoNana1V5BXr9n1RRp6GRVygCNcHCeMfaMOguce1GT3sOFjsUehlIy4QSzLed3_zRC-zy6mgXBQDARi2ZHT6xoQS9J6nRsWEKoIOBHaFaQCM316Wfp2o4LkyGjs3JgLtYrUUA-w6daP6WE9bMRequzkNYXkvfh1nZZIK1sgg95evbhvbqe7gHlraKWR6fMZjxSAFEEJ8zhugE7wGHtC_qugGgZ6Hy4-ilbDz5dzt9s-AiPmTfJ4GKb0jQkXtYn8qZovmAaiakgTYV67miAAAAAYiHvBkA")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()

