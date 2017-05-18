# /usr/bin/env python3
# coding: utf-8

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatBot = ChatBot('wxChatBot')
chatBot.set_trainer(ChatterBotCorpusTrainer)
chatBot.train('chatterbot.corpus.chinese')


def main():
    print(chatBot.get_response('你好'))
    print(chatBot.get_response('你是谁'))
    print(chatBot.get_response('谢谢'))
    print(chatBot.get_response('复杂优于晦涩.'))


if __name__ == '__main__':
    main()
