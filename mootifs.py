#!/usr/bin/python
import mta
import mashup
import numpy
import sys
import wav

def usage():
    print "usage: mootifs [command] [file] [file] [file] ..."
    print "commands:"
    print "    mash - generate mashup from files"
    print "    wav  - export motifs from first wav file"
    print "    csv  - export motifs from first csv file"


def command_mash(wavs):
    wavs = [wav.Wav(w) for w in wavs]
    music.mashup(wavs)

def command_csv(wavfile):
    w = wav.Wav(wavfile)
    motifs = mta.get_motifs(w.mono())
    for tracker in motifs:
        start_sec = tracker.loc['start'] / w.sample_rate
        end_sec = tracker.loc['length'] / w.sample_rate
        print tracker.word
        print "\tstart {}, end {}".format(start_sec, end_sec)
        
def command_csv(csvfile):
    arr = numpy.genfromtxt(csvfile, delimiter=',')
    if arr.ndim > 1:
        raise Error('csv has more than one column')

    motifs = mta.get_motifs(arr)
    for tracker in motifs:
        print tracker.word
        print "\tstart {}, length {}".format(tracker.loc['start'],
                                             tracker.loc['length'])

if len(sys.argv) > 2:
    command = sys.argv[1]
    files = sys.argv[2:]

    if command == 'mash':
        command_mash(files)
    elif command == 'wav':
        command_wav(files[0])
    elif command == 'csv':
        command_csv(files[0])
    else:
        usage()
else:
    usage()