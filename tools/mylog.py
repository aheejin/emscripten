import sys

mydebug = True

def log_cmd(cmd, cwd='', *args, **kwargs):
  if not mydebug:
    return
  print 'CMD: ' + ' '.join(cmd)
  if cwd:
    print '  CWD: ' + cwd
  sys.stdout.flush()

def log_move(src, dst):
  if not mydebug:
    return
  print 'MOVE: mv %s %s' % (src, dst)
  sys.stdout.flush()

def log_copy(src, dst):
  if not mydebug:
    return
  print 'COPY: cp %s %s' % (src, dst)
  sys.stdout.flush()

def log_remove(f, *args, **kwargs):
  if not mydebug:
    return
  print 'REMOVE: ' + f
  sys.stdout.flush()
