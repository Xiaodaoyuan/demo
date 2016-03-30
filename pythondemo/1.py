from functools import wraps

def log(f):
   @wraps(f)
   def call(*args,**kw):
       print 'call %s'% f.__name__
       return f(*args,**kw)
   return call

@log
def now():
   print '2016-3-24'

now()
