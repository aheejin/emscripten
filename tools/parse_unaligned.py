import os, sys
from subprocess import Popen, PIPE, STDOUT
import mylog

shown = set()

for line in open(sys.argv[1]).readlines():
  try:
    x = line.split(' in ')[1].split(':')[0]
    #output = str([x, Popen(['c++filt', x], stdout=PIPE).communicate()])
    mylog.log_cmd(['c++filt', x], stdout=PIPE)
    output = Popen(['c++filt', x], stdout=PIPE).communicate()[0]
    if output not in shown:
      shown.add(output)
      print output,
  except:
    pass


