from scipy import io
from scipy import signal
import chunk
import numpy
import struct
import wave

class Wav:
    """Reads in wav files and stores them in a Wav class optimized for use with
    our music characteristic identification module.

    Public variables:
        nchannels    -- number of audio channels (1 for mono, 2 for stereo)
        nsamples     -- number of audio samples 
        sample_width -- width of one channel's sample in bytes
        sample_rate  -- sampling frequency in hertz
        duration     -- audio duration in seconds
        time_series  -- samples in numpy array of shape (nsamples, nchannels)
    """

    def __init__(self, filename):
        f = open(filename, 'rb')
        self._read_wav_info(f)
        self._read_wav_data(f)

    def _read_wav_info(self, f):
        """Read metadata from wav file f

        Uses standard library wave module to extract metadata from wav file into
        instance variables.
        """
        fp = wave.open(f, 'r')
        self.nchannels = fp.getnchannels()
        self.nsamples = fp.getnframes()
        self.sample_width = fp.getsampwidth()
        self.sample_rate = fp.getframerate()
        self.duration = self.nsamples // self.sample_rate
        fp.close()

    def _read_wav_data(self, f):
        """Read samples from wave file `f`

        Uses standard library chunk module to perform traversal and basic
        verification of WAVE file format. Uses numpy to efficiently read in
        binary data from file.

        Sets `time_series` to a numpy array with shape (nsamples, ns).
        """
        f.seek(0)
        file_chunk = chunk.Chunk(f, bigendian=False)
        if file_chunk.read(4) != 'WAVE':
            raise WavFormatError('invalid wav file')
        while True:
            try:
                sub_chunk = chunk.Chunk(file_chunk, bigendian=False)
            except EOFError:
                raise WavFormatError('unable to find data chunk')
            if sub_chunk.getname() == 'data':
                arr = numpy.fromfile(f, dtype=self._get_dtype(),
                                     count=sub_chunk.getsize())
<<<<<<< HEAD
               	print sub_chunk.getsize()
               	print arr.shape
                if self.nchannels > 1:
                    arr = arr.reshape(-1, self.nchannels)
                self.time_series = arr
=======
                self.time_series = arr.reshape(-1, self.nchannels)
>>>>>>> b6ef60128cc4e44c005705549db83ef26fbd6ab0
                return
            sub_chunk.skip()


    def _get_dtype(self):
        """Returns numpy datatype specifying format of wav file samples"""
        if self.sample_width == 1:
            # 8-bit samples are unsigned integers
            fmt = '<u1'
        elif 2 <= self.sample_width <= 3:
            # 16- and 32-bit samples are signed integers
            fmt = '<i' + str(self.sample_width)
        else:
            raise WavFormatError('unrecognized sample width')

        return numpy.dtype(fmt)

    def mono(self):
        if self.nchannels > 1:
            channels = numpy.hsplit(self.time_series, 2)
            return numpy.add(*channels) // self.nchannels
        else:
            return self.time_series

    def resample(self, nsamples):
        """Resamples audio to contain `nsamples` samples

        Uses scipy signal processing to resample audio using the Fourier method.
        Returns resampled numpy array of size (nsamples, nchannels)
        """
        dtype = self.time_series.dtype
        return signal.resample(self.time_series, nsamples).astype(dtype)


def write(filename, samples, sample_rate):
    #wav.write('all i need.wav', array, 44100)
    """Writes a wavefile from a numpy array of samples

    Arguments:
        filename -- wav filename as string
        samples  -- a numpy array of shape (nsamples, nchannels) of audio 
                    samples. Must be an integer type.
        rate     -- sample frequency in hertz
    """

    fp = wave.open(filename, 'wb')

    if samples.ndim == 1:
        fp.setnchannels(1)
    else:
        fp.setnchannels(samples.shape[1])

    fp.setnframes(samples.shape[0])
    fp.setframerate(sample_rate)
    fp.setsampwidth(samples.dtype.itemsize)

    fp.writeframes(samples.tostring())
    fp.close()
    

class WavFormatError(Exception):
    pass