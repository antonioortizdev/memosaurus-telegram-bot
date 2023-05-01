from logs import log
import configuration
from text_to_speech import text_to_speech
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler


async def reply_to_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    voice = update.message.voice

    if text:
        log('text sent.')
        await update.message.reply_voice(text_to_speech(text))

        """  if voice:
        log('voice sent.')
        await update.message.reply_text(speech_to_text(voice)) """


if __name__ == '__main__':
    TELEGRAM_BOT_TOKEN = configuration.get('TELEGRAM_BOT_TOKEN')

    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    message_handler = MessageHandler(None, reply_to_message)
    application.add_handler(message_handler)

    application.run_polling()
