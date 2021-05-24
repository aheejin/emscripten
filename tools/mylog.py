import sys

mydebug = True

def log_cmd(cmd, cwd='', *args, **kwargs):
  sys.stdout.flush()
  sys.stderr.flush()
  if not mydebug:
    return
  if not isinstance(cmd[0], str):
    cmd = [str(item) for item in cmd]
  print('CMD: ' + ' '.join(cmd))
  if cwd:
    print('  CWD: ' + cwd)
  sys.stdout.flush()
  sys.stderr.flush()

def log_move(src, dst):
  sys.stdout.flush()
  sys.stderr.flush()
  if not mydebug:
    return
  if not isinstance(src, str):
    src = str(src)
    dst = str(dst)
  print('MOVE: mv %s %s' % (src, dst))
  sys.stdout.flush()
  sys.stderr.flush()

def log_copy(src, dst):
  sys.stdout.flush()
  sys.stderr.flush()
  if not mydebug:
    return
  if not isinstance(src, str):
    src = str(src)
    dst = str(dst)
  print('COPY: cp %s %s' % (src, dst))
  sys.stdout.flush()
  sys.stderr.flush()

def log_remove(f, *args, **kwargs):
  sys.stdout.flush()
  sys.stderr.flush()
  if not mydebug:
    return
  if not isinstance(f, str):
    f = str(f)
  print('REMOVE: ' + f)
  sys.stdout.flush()
  sys.stderr.flush()

def log_chdir(d):
  sys.stdout.flush()
  sys.stderr.flush()
  if not mydebug:
    return
  if not isinstance(d, str):
    d = str(d)
  print('CHDIR: ' + d)
  sys.stdout.flush()
  sys.stderr.flush()
