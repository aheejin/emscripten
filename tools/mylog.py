import sys

mydebug = True

def log_cmd(cmd, cwd='', *args, **kwargs):
  sys.stdout.flush()
  sys.stderr.flush()
  if not mydebug:
    return
  print 'CMD: ' + ' '.join(cmd)
  if cwd:
    print '  CWD: ' + cwd
  sys.stdout.flush()
  sys.stderr.flush()

def log_move(src, dst):
  sys.stdout.flush()
  sys.stderr.flush()
  if not mydebug:
    return
  print 'MOVE: mv %s %s' % (src, dst)
  sys.stdout.flush()
  sys.stderr.flush()

def log_copy(src, dst):
  sys.stdout.flush()
  sys.stderr.flush()
  if not mydebug:
    return
  print 'COPY: cp %s %s' % (src, dst)
  sys.stdout.flush()
  sys.stderr.flush()

def log_remove(f, *args, **kwargs):
  sys.stdout.flush()
  sys.stderr.flush()
  if not mydebug:
    return
  print 'REMOVE: ' + f
  sys.stdout.flush()
  sys.stderr.flush()

def log_chdir(d):
  sys.stdout.flush()
  sys.stderr.flush()
  if not mydebug:
    return
  print 'CHDIR: ' + d
  sys.stdout.flush()
  sys.stderr.flush()
