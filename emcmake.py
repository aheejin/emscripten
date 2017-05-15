#!/usr/bin/env python2

import os, subprocess, sys
from tools import shared
from tools import mylog

#
# Main run() function
#
def run():
  configure_path = shared.path_from_root('emconfigure')

  mylog.log_cmd([shared.PYTHON, configure_path] + sys.argv[1:])
  exit(subprocess.call([shared.PYTHON, configure_path] + sys.argv[1:]))

if __name__ == '__main__':
  run()
