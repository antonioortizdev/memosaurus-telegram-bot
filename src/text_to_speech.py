import configuration
from time import time_ns
from logs import log


def synthesize_text(text) -> None:
    """Synthesizes speech from the input string of text."""
    from google.cloud import texttospeech

    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.VoiceSelectionParams(
        language_code=configuration.get("TTS_LANGUAGE_CODE"),
        name=configuration.get("TTS_VOICE_NAME"),
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice,
                 "audio_config": audio_config}
    )

    # The response's audio_content is binary.
    now = time_ns()
    with open(f'{now}.mp3', "wb") as out:
        out.write(response.audio_content)
        log(f'Audio content written to file "{now}.mp3"')


def text_to_speech(text: str):
    return synthesize_text(text)
