# /usr/bin/env python
# coding: utf-8

from flask import Flask, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


app = Flask(__name__)

chatBot = ChatBot('ChatBot')
chatBot.set_trainer(ChatterBotCorpusTrainer)
chatBot.train('chatterbot.corpus.chinese')


@app.route('/chatBot')
def chatBotResponse():
    response = chatBot.get_response(request.args.get('user_input')).text
    return response


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
