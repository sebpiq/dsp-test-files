Reference test files for dsp 
==============================

This is a set of reference wav files for testing various dsp stuff. All the files are saved to JSON format so they are easy to load anywhere. 

You can see plots of all the test files [here](http://sebpiq.github.io/dsp-test-files/plots/).

Waveforms
-----------

All the waveforms test files contain 4410 samples of 16-bits mono signal, with sample rate 44100 Hz.


Window functions
------------------

All the window function test files contain 1024 samples.


Building the test files
-------------------------

To build the test files you must have Pure Data and Python (with numpy and scipy) installed.

From the root directory run `python build.py` and the files are generated under `test-files`.
