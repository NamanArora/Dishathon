from pydub import AudioSegment
sound=AudioSegment.from_file('speech.mp4',format='mp4')
sound.export('speech1.wav',format='wav')
