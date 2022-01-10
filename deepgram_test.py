from deepgram import Deepgram
import asyncio, json

DEEPGRAM_API_KEY = '1ce10e16e3dad3729fef9547bbb07a8f1c2ff452'

PATH_TO_FILE = 'life.wav'

async def main():

    dg_client = Deepgram(DEEPGRAM_API_KEY)

    with open(PATH_TO_FILE, 'rb') as audio:

        source = {'buffer': audio, 'mimetype': 'audio/wav'}
        response = await dg_client.transcription.prerecorded(source, {'punctuate': True})
        print(json.dumps(response, indent=4))

asyncio.run(main())