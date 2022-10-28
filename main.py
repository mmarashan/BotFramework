from telegram_bot_driver.telegram_bot import Bot, TelegramBot
from zkhbotapp.api.zkh_bot_api_model import BotApiModel, ZKHBotApiModelImpl

import configparser

configParser = configparser.ConfigParser()
configParser.read_file(open(r'config.txt'))
token = configParser.get('Telegram', 'token')

bot_api_model: BotApiModel = ZKHBotApiModelImpl()

bot: Bot = TelegramBot(token=token, bot_api_model=bot_api_model)
bot.launch()
