import logging
import configuration
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler


def log(msg: str) -> None:
    print(msg)
    logging.log(msg=msg, level=logging.INFO)


async def reply_to_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    voice = update.message.voice

    if text:
        log('text sent.')
        await update.message.reply_text(text)

    if voice:
        log('voice sent.')
        await update.message.reply_voice(voice)


if __name__ == '__main__':
    TELEGRAM_BOT_TOKEN = configuration.get('TELEGRAM_BOT_TOKEN')

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO,
    )

    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    message_handler = MessageHandler(None, reply_to_message)
    application.add_handler(message_handler)

    application.run_polling()
