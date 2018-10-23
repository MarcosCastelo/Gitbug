import hashlib
def encrypt(string):
	encoded = bytes(string, 'utf-8')
	h = hashlib.md5()
	h.update(encoded)
	return h.hexdigest()