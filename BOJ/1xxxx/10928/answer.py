import hashlib as h
print(h.sha1(input().encode('utf-8')).hexdigest())