import logging
from telethon import TelegramClient, events
from decouple import config

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.INFO
)

bottoken = None
# start the bot
logging.info("Starting...")
apiid = 6
apihash = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
try:
    bottoken = config("BOT_TOKEN")
except:
    logging.info("Environment vars are missing! Kindly recheck.")
    logging.info("Bot is quiting...")
    exit()

if bottoken != None:
    try:
        BotzHub = TelegramClient("bot", apiid, apihash).start(bot_token=bottoken)
    except Exception as e:
        logging.info(f"ERROR!\n{str(e)}")
        logging.info("Bot is quiting...")
        exit()
else:
    logging.info("Environment vars are missing! Kindly recheck.")
    logging.info("Bot is quiting...")
    exit()

@BotzHub.on(events.NewMessage(incoming=True, pattern="^/start"))
async def msgg(event):
    await send_start(event, "Working fine.")

logging.info("Bot has started.")
logging.info("Do visit @BotzHub..")
BotzHub.run_until_disconnected()
