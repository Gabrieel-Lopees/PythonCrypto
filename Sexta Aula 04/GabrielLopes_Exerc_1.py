from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os

def gerar_chaves():
    chave = RSA.generate(2048)  
    chave_privada = chave.export_key()  
    chave_publica = chave.publickey().export_key() 
    
    with open("chave_privada.pem", "wb") as f_privada:
        f_privada.write(chave_privada)
    
    with open("chave_publica.pem", "wb") as f_publica:
        f_publica.write(chave_publica)

def criptografar(mensagem):
    with open("chave_publica.pem", "rb") as f_publica:
        chave_publica = RSA.import_key(f_publica.read())
    
    cifra = PKCS1_OAEP.new(chave_publica)
    mensagem_encriptada = cifra.encrypt(mensagem.encode()) 
    return mensagem_encriptada

def descriptografar(mensagem_encriptada):
    with open("chave_privada.pem", "rb") as f_privada:
        chave_privada = RSA.import_key(f_privada.read())
    
    cifra = PKCS1_OAEP.new(chave_privada)
    mensagem_descriptografada = cifra.decrypt(mensagem_encriptada).decode() 
    return mensagem_descriptografada

def main():
    gerar_chaves()
    
    mensagem = input("Digite a mensagem a ser criptografada: ")
    
    mensagem_encriptada = criptografar(mensagem)
    print("Mensagem criptografada: ", mensagem_encriptada)
    
    mensagem_descriptografada = descriptografar(mensagem_encriptada)
    print("Mensagem descriptografada: ", mensagem_descriptografada)
    
if __name__ == "__main__":
    main()


#x1c$\xe5\x16Ks\x8f\xfb\xb1\x08\x1f\xd8\x85\xda\x9boVB\xd3\xc4r\xbaG9\xd4\xf0\xed\xf3\x0c.GO2\x9c5\xf1\xf8\x89\x1d\xa2$P\xae\xe2\x01\xc9\x8f1\x7f\x80Y!\xb6\xb8b\xeb\xf2\xc1\x16\x1a}f\x03\x97\x8a\xb8*\x1e\xcb!*tE\x7f\xbc\xabc\x0bTL\xa0
#b'gc\xd2\x8fj\x05X\xa6\xe2\xc9\x17H\xb3\xbfCP\x9f \xfd*\xe5s\xb2=\xb9\x13\x0ez\x87\x85\xf2\x15\xb7\x8c\xe6\x81\x14\x10\xed\xbe\xfb?M\xb6\x8c\x11\xa9\xbdE\x1d\x91\xb9o\xd1=\xc5D8\rdt\xc1\xee\rK \xbf@\x7f\x06\x87u\xc3\xb1&\x88\x05\x89\xe5\xa5$\xf8Z\xe2\x12\xd1\xb4\xb5\xf8oe\xd7\x1f\x8a\xb8\x07\xf8P8\xe0O\xf4\x8a+\xab\xe7\xf7\xfb\xa1\xc7\x1f\tU{M\xdf&\x00d\xa7k\xbd\x8cWV\xfa#c\x00nbQ;O\xcb\xbb`5\xd6\xcae\x08C\r-e\xe1\xabF\xa1\t2\x8b\x9f\x16\x08\x85\x93\xc3\xb1\xb0\xbb\xfb\x08\xb6\xd1h\x03\x13]\x17\x946\x0bo\xb8:?\x8b(\xeb\xe45q\xdf $?\x00h\x88\x82\xda\xc9\xaf\x16.Tm[\x0f7\xf6*\x81\xfd-\xd2\xb1\xe3T\xcfi*1\xd3\xc6\xf4\x897V\xec\x91\xf6!\xbf\x14W\xfcY1=\xdb\xde\xaa\xadI?3V\x84WD\xcb^;\xeec\x07kI\x99d\xcfA\x98'
