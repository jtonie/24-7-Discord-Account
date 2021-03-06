# Do not Touch if you do not know what you are doing or you will be messing up the code.
# this will run a server that you can ping via Pinging Services to run it 24/7

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')    

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()
