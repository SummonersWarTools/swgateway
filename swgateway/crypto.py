from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad
from zlib import decompress

class CryptoParams:

    def __init__(self, key, iv):
        self.__key = key
        self.__iv = iv

    def GetCrypto(self):
        return AES.new(self.__key, AES.MODE_CBC, iv=self.__iv)

class SWCryptoMgr:

    DEFAULT = CryptoParams(b'Gr4S2eiNl7zq5MrU', b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    CHAT = CryptoParams(b'E2wN5Eo0t4gle92Z', b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

    def Decrypt(cryptoParams, encryptedContent, compression = True):
        decrypted = unpad(cryptoParams.GetCrypto().decrypt(encryptedContent), AES.block_size)
        if compression: return decompress(decrypted).decode('utf-8')
        else: return decrypted.decode('utf-8')

    def Encrypt(cryptoParams, plaintextContent):
        return cryptoParams.GetCrypto().encrypt(pad(plaintextContent, AES.block_size))
