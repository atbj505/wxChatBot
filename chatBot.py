# /usr/bin/env python3
# coding: utf-8

import requests
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask

from wxbot import WXBot

app = Flask(__name__)

chatBot = ChatBot('ChatBot')
chatBot.set_trainer(ChatterBotCorpusTrainer)
chatBot.train('chatterbot.corpus.chinese')


@app.route('/chatBot/<input>')
def chatBotFun(input):
    response = chatBot.get_response(input).text
    return response


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
