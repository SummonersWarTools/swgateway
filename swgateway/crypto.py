from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad
from zlib import decompress

class CryptoParams:

    def __init__(self, key, iv):
        self.__key = key
        self.__iv = iv
        self.__crypto = AES.new(self.__key, AES.MODE_CBC, iv=self.__iv)

    def GetCrypto(self):
        return self.__crypto

class SWCryptoMgr:

    DEFAULT = CryptoParams(b'Gr4S2eiNl7zq5MrU', b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

    def Decrypt(cryptoParams, encryptedContent):
        return decompress(SWCryptoMgr.__WithRecrypto(unpad(cryptoParams.GetCrypto().decrypt(encryptedContent), AES.block_size))).decode('utf-8')

    def Encrypt(cryptoParams, plaintextContent):
        return SWCryptoMgr.__WithRecrypto(cryptoParams.GetCrypto().encrypt(pad(plaintextContent, AES.block_size)))

    def __WithRecrypto(param):
        SWCryptoMgr.DEFAULT = CryptoParams(b'Gr4S2eiNl7zq5MrU', b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        return param