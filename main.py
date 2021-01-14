import hashlib

string = 'a'.encode()
sha = hashlib.new('sha256')

sha.update(string)
print(sha.hexdigest())