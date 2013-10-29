import os
import re
from subprocess import call

os.mkdir('wavs')

base_opts = ['pd', '-nogui', '-noaudio', '-blocksize', '1', '-send']

for filename in os.listdir('pd-patches'):
    matched = re.match(r'(?P<test_name>\S*?)\.pd$', filename)
    if matched:
      test_name = matched.group('test_name')
      print '> generating wav file for test %s' % test_name
      call(base_opts + [';testName %s' % test_name, os.path.join('pd-patches', filename)])
    else:
      print 'file %s ignored' % filename
