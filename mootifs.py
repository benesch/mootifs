#!/usr/bin/env python
import mta
import mashup
import music
import numpy
import sys
import wav

def usage():
    print "usage: mootifs [command]"
    print "commands:"
    print "    bpm [wav]                    - detect bpm of wav"
    print "    instrumental [in] [out]      - extract instrumentals"
    print "    transpose [in] [out] [shift] - change pitch by shift factor"
    print "    mash [file] [file] ... [out] - generate mashup from files"
    print "    wav [file]                   - find motifs from wav file"
    print "    csv [file]                   - find motifs from csv file"


def command_bpm(*files):
    w = wav.Wav(files[0])
    bpm = music.get_bpm(w.time_series)
    print "{}bpm".format(bpm)

def command_instrumental(*args):
    if len(args) != 2:
        usage()
        return
    w = wav.Wav(args[0])
    out = music.extract_instrumentals(w.time_series)
    wav.write(args[1], out, w.sample_rate)

def command_transpose(*args):
    if len(args) != 3:
        usage()
        return
    w = wav.Wav(args[0])
    out = music.extract_instrumentals(w.time_series, args[2])
    wav.write(args[1], out, w.sample_rate)

def command_mash(*args):
    wavs = [wav.Wav(w) for w in args[:-1]]
    out = mashup.generate(wavs)
    wav.write(args[-1], out, 44100)

def command_wav(*files):
    SAMPLES = 1000
    w = wav.Wav(files[0])
    arr = wav.mono(w.resample(SAMPLES))
    motifs = mta.get_motifs(arr)
    print
    print "discovered motifs"
    print "-----------------"
    print "data length:", arr.shape[0]
    print
    for tracker in motifs:
        print tracker.word
        for loc in tracker.loc:
            start_sec = (loc['start'] / float(SAMPLES)) * w.duration
            len_sec = (loc['len'] / float(SAMPLES)) * w.duration
            print "\tstart {}s, length {}s".format(start_sec, len_sec)

def command_csv(*files):
    arr = numpy.genfromtxt(files[0], delimiter=',')
    if arr.ndim > 1:
        raise Error('csv has more than one column')

    motifs = mta.get_motifs(arr)
    print
    print "discovered motifs"
    print "-----------------"
    print "data length:", arr.shape[0]
    print
    for tracker in motifs:
        print tracker.word
        for loc in tracker.loc:
            print "\tstart {}, length {}".format(loc['start'], loc['len'])

if len(sys.argv) > 2:
    command = sys.argv[1]
    args = sys.argv[2:]

    if command == 'bpm':
        command_bpm(*args)
    elif command == 'instrumental':
        command_instrumental(*args)
    elif command == 'transpose':
        command_tranpose(*args)
    elif command == 'mash':
        command_mash(*args)
    elif command == 'wav':
        command_wav(*args)
    elif command == 'csv':
        command_csv(*args)
    else:
        usage()
else:
    usage()