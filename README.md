# mootifs: a music similarity engine
**cs51 final project, harvard university**
nikhil benesch, joseph botros, francis loh


## instructions
### requirements
- Python 2.7.4
- NumPy/SciPy
- nose (Python test runner)


### installation
These instructions apply to OS X Mountain Lion. 

1. Install Xcode &amp; Xcode Command Line Tools
1. Install [Homebrew](http://mxcl.github.io/homebrew/). [Detailed instructions.](https://github.com/mxcl/homebrew/wiki/Installation)
1. `brew install python`
1. Ensure `/usr/local/bin/` occurs first in `/etc/paths/`.
1. Place `/usr/local/share/python` on your path.
1. Run `pip install -r requirements.txt`.
   * You may need a fortran compiler. `brew install gfortran` does the trick.

In short, just get the requirements installed somehow.


###usage
mootifs.py is a command-line interface to our code. From within the appropriate
virtual environment, run 

    python mootifs.py [command] [options...]

Git should set the executable bit, so you can invoke `./mootifs.py` directly as
well. Run the command with no options to see brief usage instructions,
reproduced below.

    usage: mootifs [command]
    commands:
        bpm [wav]                    - detect bpm of wav
        instrumental [in] [out]      - extract instrumentals
        transpose [in] [out] [shift] - change pitch by shift factor
        mash [file] [file] ... [out] - generate mashup from files
        wav [file]                   - find motifs from wav file
        csv [file]                   - find motifs from csv file

####bpm
Takes the path to one wave file `wav`. Outputs the beats per minute.

####instrumental
Takes the path to an input wave file `in` and output wave file `out`. Writes
an instrumental version to `out`.

####transpose
Takes the path to an input wave file `in` and output wave file `out`. Scales
song by `shift` factor, thus changing the pitch. Use floats greater than 1
to lengthen song and lower pitch, or floats less than 1 to shorten song and
increase pitch.

####mash
Generate a mashup from `file`s and write out into `out` file. Uses the first
file passed as an instrumental backdrop, and cycles through motifs of all 
additional files passed in.

Note that this command can take quite a while to run, especially on larger
wave files. We recommend creating mashups with no more than three songs.

####wav
Find motifs within wave `file`. This command uses less downsampling than the 
mashup command to provide more resolution for the MTA. Thus, the motifs returned
by this command may not be the same motifs used in mashup generation.

Motifs are output in the following format

        ['?' '?' '?' '?' '?']
            start ##s, length ##s
            start ##s, length ##s
            start ##s, length ##s

where each `?` represents a symbol in the motif, and each following line denotes
a discovered instance of the motif, starting at time ##s with length ##s.

####csv
Find motifs with csv `file`. This command takes approximately 10 minutes to
run on a data file with 1000 entries. The CSV should contain only one column
of data, where rows are separated by newline characters '\n'.

Motifs are output in the following format

        ['?' '?' '?' '?' '?']
            start ##, length ##
            start ##, length ##
            start ##, length ##

where each `?` represents a symbol in the motif, and each following line denotes
a discovered instance of the motif, starting at row ## with length ##.

####general notes
Not all wave file formats are supported. In particular, wave files must be
uncompressed, with samples stored as 8-, 16-, or 32-bit integers. If a 
particular wave file is denoted unreadable, try re-exporting from audio editing
software with all metadata removed.


###testing
Run `nosetests` to invoke the nose test runner. This will run autodiscover all
tests located in files in the tests/ diretory.

Testcases for algorithms are enabled by default. Testing the music and mashup
modules require generation of wav files and are commented out by default.
To run these tests, uncomment the tests in the appropriate files
(`tests/test_music.py` and `tests/test_mashup.py`).