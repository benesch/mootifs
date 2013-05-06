SEC = 44100
from .. import wav
from .. import mashup

# commented out for time purposes - can be uncommented and run to test mashup module

# def test_simple():
# 	wav1 = wav.Wav('data/for the first time.wav').time_series
# 	wav2 = wav.Wav('data/i knew you were trouble.wav').time_series
# 	wav3 = wav.Wav('data/all i need.wav').time_series
# 	wavs = [wav1, wav2, wav3]

# 	segments = [
# 		(0, 2 * SEC, 25 * SEC, 17 * SEC, 0.8),
# 		(1, 7 * SEC, 25 * SEC, 1 * SEC, 0.4),
# 		(2, 19 * SEC, 25 * SEC, 33 * SEC, 1.3)
# 	]
# 	wav.write('out.wav', mashup.construct(wavs, segments), SEC)