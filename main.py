import hashlib
s='runnertool'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
