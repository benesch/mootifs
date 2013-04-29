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
Beta instructions to run our version of the MTA.

1. `python` will open the Python shell
2. `import mashup` will import the mashup module
3. `m = mashup.make_mashup()` will create a list of tracker objects corresponding to identified motifs
4. Examine the result by looking at specific trackers and their matches: `m[-1].word` returns the matched symbol sequence of the last tracker, while `m[-1].starts` returns a list of start points for the motif. Since our PAA calculation uses a sliding scale, these indices correspond to the indices in our original list. Looking back at the original data in Excel, we can display the motifs of interest by taking the data points starting at the indicated positions in the tracker and spanning the length of the motif symbol sequence. We plan to build in functionality so as to not have to do this manually in our final version.