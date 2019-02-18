#!/usr/bin/env python2
# Copyright 2016 The Emscripten Authors.  All rights reserved.
# Emscripten is available under two separate licenses, the MIT license and the
# University of Illinois/NCSA Open Source License.  Both these licenses can be
# found in the LICENSE file.

import subprocess
import sys
from tools import shared
from tools import mylog


#
# Main run() function
#
def run():
  configure_path = shared.path_from_root('emconfigure')
  mylog.log_cmd([shared.PYTHON, configure_path] + sys.argv[1:])
  return subprocess.call([shared.PYTHON, configure_path] + sys.argv[1:])


if __name__ == '__main__':
  sys.exit(run())
