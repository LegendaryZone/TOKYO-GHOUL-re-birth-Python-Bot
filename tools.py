from Crypto.Cipher import AES
import base64
import binascii
import StringIO
from rijndael.cipher.crypt import new
from rijndael.cipher.blockcipher import MODE_CBC

class PKCS7Encoder(object):
	def __init__(self, k=16):
	   self.k = k

	def decode(self, text):
		nl = len(text)
		val = int(binascii.hexlify(text[-1]), 16)
		if val > self.k:
			raise ValueError('Input is not padded or padding is corrupt')
		l = nl - val
		return text[:l]

	def encode(self, text):
		l = len(text)
		output = StringIO.StringIO()
		val = self.k - (l % self.k)
		for _ in xrange(val):
			output.write('00')#LITTLE FUCKER
		return text + binascii.unhexlify(output.getvalue())

class RijndaelEncryptor(object):
    def __init__(self):
        self.encoder=PKCS7Encoder()

    def encrypt(self, text, input_key, input_iv):
		if (len(text) % 16)==0:
			pad_text = text
			rjn = new(input_key, MODE_CBC, input_iv, blocksize=16)
			return base64.b64encode(rjn.encrypt(pad_text))
		else:
			aes = AES.new(input_key, AES.MODE_CBC, input_iv)
			pad_text = self.encoder.encode(text)
			cipher_text = aes.encrypt(pad_text)
			return base64.b64encode(cipher_text)

    def decrypt(self, text, input_key, input_iv):
		rjn=new(input_key, MODE_CBC, input_iv, blocksize=16)
		return rjn.decrypt(base64.b64decode(text)).replace('\x00','')

class Crypter(object):
	def __init__(self):
		self.key='r6bhgx@jdsa%8#pq'
		self.iv='el0y5nbv17&d%3+c'
		self.crypt=RijndaelEncryptor()

	def decode(self,text):
		return self.crypt.decrypt(text,self.key,self.iv)

	def encode(self,text):
		return self.crypt.encrypt(text,self.key,self.iv)