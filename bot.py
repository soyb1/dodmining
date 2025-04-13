import logging
from telegram import Update, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "7564198568:AAHjuSfh3doH4HMZ2OlenfvEZk9MkSCSQC0"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [ 
            {
                "text": "🚀 Open DOD Miner",
                "web_app": WebAppInfo(url="https://your-ngrok-url/webapp")
            }
        ]
    ]
    await update.message.reply_text("Welcome to DOD Mining Bot!", reply_markup={"keyboard": keyboard, "resize_keyboard": True})

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
