from deepgram import Deepgram
import asyncio, json

DEEPGRAM_API_KEY = 'SECRET-KEY'

PATH_TO_FILE = 'AUDIO.wav'

async def main():

    dg_client = Deepgram(DEEPGRAM_API_KEY)

    with open(PATH_TO_FILE, 'rb') as audio:

        source = {'buffer': audio, 'mimetype': 'audio/wav'}
        response = await dg_client.transcription.prerecorded(source, {'punctuate': True})
        print(json.dumps(response, indent=4))

asyncio.run(main())
