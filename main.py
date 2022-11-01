from telegram_bot_driver.telegram_bot import Bot, TelegramBot
from zkhbotapp.api.zkh_bot_api_model import BotModel, ZKHBotModelImpl

import configparser

configParser = configparser.ConfigParser()
configParser.read_file(open(r'config.txt'))
token = configParser.get('Telegram', 'token')

bot_model: BotModel = ZKHBotModelImpl()

bot: Bot = TelegramBot(token=token, bot_model=bot_model)
bot.launch()
