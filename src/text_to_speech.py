import configuration
import os
from time import time_ns
from logs import log


def synthesize_text(text) -> str:
	"""Synthesizes speech from the input string of text."""
	from google.cloud import texttospeech

	client = texttospeech.TextToSpeechClient()

	input_text = texttospeech.SynthesisInput(text=text)

	# Note: the voice can also be specified by name.
	# Names of voices can be retrieved with client.list_voices().
	voice = texttospeech.VoiceSelectionParams(
		language_code=configuration.get("GOOGLE_TTS_LANGUAGE_CODE"),
		name=configuration.get("GOOGLE_TTS_VOICE_NAME"),
		ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
	)

	audio_config = texttospeech.AudioConfig(
		audio_encoding=texttospeech.AudioEncoding.MP3
	)

	response = client.synthesize_speech(
		request={"input": input_text, "voice": voice,
				 "audio_config": audio_config}
	)

	voices_dir = configuration.get('VOICES_DIR')
	if not os.path.exists(voices_dir):
		os.makedirs(voices_dir)

	# The response's audio_content is binary.
	now = time_ns()
	voice_path = f'{voices_dir}{now}.mp3'
	with open(voice_path, "wb") as out:
		out.write(response.audio_content)
		log(f'Audio content written to file "{voice_path}"')
		return voice_path


def text_to_speech(text: str) -> str:
	"""
		Converts text to speech and returns the path to the audio file.

		:param text: The text to be converted to speech.
		:return: The path to the audio file.
	"""
	return synthesize_text(text)
