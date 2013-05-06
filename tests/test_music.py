SEC = 44100
from .. import wav
from .. import mashup
from .. import music

# def test_extract_instrumentals():
# 	wav1 = wav.Wav('data/onerepublic.wav').time_series
# 	wav1 = music.extract_instrumentals(wav1)
# 	wavs = [wav1]
# 	segments = [(0, 0 * SEC, 25 * SEC, 5 * SEC, 1.5)]
# 	wav.write('extracted_onerepublic3.wav', mashup.construct(wavs, segments), SEC)

# def test_transpose_key():
# 	w = wav.Wav('data/sail.wav')
# 	music.transpose_key(0.8, w)

# def test_get_bpm():
# 	w = wav.Wav('data/i knew you were trouble.wav')
# 	music.get_bpm(w)