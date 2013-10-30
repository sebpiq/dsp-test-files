Reference test files for dsp 
==============================

This is a set of reference wav files for testing various dsp stuff. All the files are saved to JSON format so they are easy to load anywhere. 


Waveforms
-----------

All the waveforms are generated to 16-bits mono signals.


Building the test files
-------------------------

To build the test files you must have Pure Data and Python (with numpy and scipy) installed.

From the root directory run `python build.py` and the files are generated under `test-files`.
