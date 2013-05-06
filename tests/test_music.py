SEC = 44100
from .. import wav
from .. import mashup
from .. import music

def test_extraction():
	wav1 = wav.Wav('data/onerepublic.wav').time_series
	wav1 = music.extract_instrumentals(wav1)
	wavs = [wav1]
	segments = [(0, 0 * SEC, 25 * SEC, 5 * SEC, 1.5)]
	wav.write('extracted_onerepublic3.wav', mashup.construct(wavs, segments), SEC)
