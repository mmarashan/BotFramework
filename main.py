from telegram_bot_driver.telegram_bot import Bot, TelegramBot
from zkhbotapp.api.zkh_bot_api_model import BotApiModel, ZKHBotApiModelImpl

bot_api_model: BotApiModel = ZKHBotApiModelImpl()

bot: Bot = TelegramBot(token="205081013:AAG-ysgYtwuBeSLLctTKThrA-Weri0Vh_6E", bot_api_model=bot_api_model)
bot.launch()
