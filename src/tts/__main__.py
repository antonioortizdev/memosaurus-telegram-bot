import logging


def text_to_speech(text: str):
    """Converts text to speech using Google Text-to-Speech."""
    from gtts import gTTS
    tts = gTTS(text=text, lang='en')
    return tts
