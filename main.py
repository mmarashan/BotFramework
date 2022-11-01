from telegram_bot_driver.telegram_bot import Bot, TelegramBot
from zkhbotapp.api.intent_classifier.intent_classifier import IntentClassifierImpl
from zkhbotapp.api.zkh_bot_model import BotModel, ZKHBotModelImpl

import configparser

configParser = configparser.ConfigParser()
configParser.read_file(open(r'config.txt'))
token = configParser.get('Telegram', 'token')

intent_classifier = IntentClassifierImpl()
bot_model: BotModel = ZKHBotModelImpl(intent_classifier=intent_classifier)

bot: Bot = TelegramBot(token=token, bot_model=bot_model)
bot.launch()
