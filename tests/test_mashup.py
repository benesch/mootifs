SEC = 44100

def test_simple():
	wav1 = wav.Wav('data/for the first time.wav')
	wav2 = wav.Wav('data/i knew you were trouble.wav')
	wav3 = wav.Wav('data/all i need.wav')
	wavs = [wav1, wav2, wav3]

	segments = [
		(0, 2 * SEC, 25 * SEC, 17 * SEC, 0.8),
		(1, 7 * SEC, 25 * SEC, 1 * SEC, 0.4),
		(2, 19 * SEC, 25 * SEC, 33 * SEC, 1.3)
	]
	wav.write('out.wav', construct(wavs, segments), SEC)
