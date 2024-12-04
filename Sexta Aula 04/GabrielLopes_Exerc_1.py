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

