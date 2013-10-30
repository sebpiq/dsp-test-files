import os
import re
import json
from subprocess import call
from scipy import signal
from scipy.io import wavfile

# Creating the folder structure for generated test files
TEST_FILES_DIR = 'test-files'
TMP_DIR = os.path.join(TEST_FILES_DIR, 'tmp')
WAVEFORMS_DIR = os.path.join(TEST_FILES_DIR, 'waveforms')
WIN_FUNC_DIR = os.path.join(TEST_FILES_DIR, 'window-functions')

for dirname in [TEST_FILES_DIR, TMP_DIR, WAVEFORMS_DIR, WIN_FUNC_DIR]:
  if not os.path.exists(dirname):
    os.mkdir(dirname)

# Generating test files for waveforms 
base_opts = ['pd', '-nogui', '-noaudio', '-blocksize', '1', '-r', '44100', '-send']
for patch_filename in os.listdir('pd-patches'):
    matched = re.match(r'(?P<test_name>\S*?)\.pd$', patch_filename)
    if matched:
        test_name = matched.group('test_name')
        print '> generating wav file for test %s' % test_name
        call(base_opts + [';testName %s' % test_name, os.path.join('pd-patches', patch_filename)])
        waveform_data = wavfile.read('%s/%s.wav' % (TMP_DIR, test_name))[1].tolist()
        dest_filename = '%s/%s.json' % (WAVEFORMS_DIR, test_name)
        with open(dest_filename, 'w') as fd:
            fd.write(json.dumps(waveform_data))

# Generating test files for window functions
test_cases = [
    {'func_name': 'bartlett', 'test_name': 'bartlett-window'},
    {'func_name': 'barthann', 'test_name': 'bartlett-hann-window'},
    {'func_name': 'blackman', 'test_name': 'blackman-window'},
    {'func_name': 'cosine', 'test_name': 'cosine-window'},
    {'func_name': 'gaussian', 'test_name': 'gaussian-window-sigma-0.25', 'args': [0.25]},
    {'func_name': 'gaussian', 'test_name': 'gaussian-window-sigma-0.5', 'args': [0.5]},
    {'func_name': 'gaussian', 'test_name': 'gaussian-window-sigma-0.9999', 'args': [0.9999]},
    {'func_name': 'hamming', 'test_name': 'hamming-window'},
    {'func_name': 'hann', 'test_name': 'hann-window'},
    {'func_name': 'triang', 'test_name': 'triangular-window'}
]
for test_case in test_cases:
    window_data = getattr(signal, test_case['func_name'])(1024, *test_case.get('args', [])).tolist()
    dest_filename = '%s/%s.json' % (WIN_FUNC_DIR, test_case['test_name'])
    with open(dest_filename, 'w') as fd:
        fd.write(json.dumps(window_data))
    print '> generated json file for test %s' % test_case['test_name']


