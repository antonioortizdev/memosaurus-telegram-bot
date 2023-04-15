import speech_recognition as sr


def speech_to_text(audio: Audio) -> str:
    """Converts speech to text using Google Speech Recognition."""
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio.file_path) as source:
        audio = recognizer.record(source)
    return recognizer.recognize_google(audio, language='ru-RU')
