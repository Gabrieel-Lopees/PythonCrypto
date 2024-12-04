from Crypto.PunlicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os

#Gerando as chaves 
def gerar_chaves():
    chave = RSA.generate (2048) 
    chave_privada = chave.export_key()
    chave_publica = chave.publickey().export_key()
    
    with open("chave_privada.pem", "wb") as f_privada:
        f_privada.write(chave_privada)
    
    with open("chave_publica.pem", "wb") as f_publica:
        f_publica.write(chave_publica)
        
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
    
    mensagem_encriptada - criptografar(mensagem)
    print("Mensagem criptografada: ", mensagem_encriptada)
    
    mensagem_descriptografada = descriptografar(mensagem_encriptada)
    print("Mensagem descriptofrada: ", mensagem_descriptografada)
    
if __name__ == "__main__":
    main()
