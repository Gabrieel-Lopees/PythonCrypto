from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Função para descriptografar a mensagem com a chave privada
def descriptografar(mensagem_encriptada):
    # Carregar a chave privada (que foi transferida do Computador A)
    with open("chave_privada.pem", "rb") as f_privada:
        chave_privada = RSA.import_key(f_privada.read())
    
    # Descriptografar a mensagem com a chave privada
    cifra = PKCS1_OAEP.new(chave_privada)
    mensagem_descriptografada = cifra.decrypt(mensagem_encriptada).decode()  # Convertendo bytes para string
    return mensagem_descriptografada

def main():
    # Passo 1: Carregar a mensagem criptografada (transferida do Computador A)
    # Aqui você substituiria pelo conteúdo que recebeu, pode ser de um arquivo ou diretamente como bytes.
    
    # Exemplo: Digite ou copie a mensagem criptografada recebida de A (em formato binário)
    # Exemplo de uma mensagem criptografada em bytes (substitua pela real mensagem recebida)
    mensagem_encriptada = b'\x9b\xdf\xab\xd2\x7f\x92...'  # Exemplo: a mensagem criptografada real
    
    # Passo 2: Descriptografar a mensagem com a chave privada
    mensagem_descriptografada = descriptografar(mensagem_encriptada)
    
    # Passo 3: Exibir a mensagem descriptografada
    print("Mensagem descriptografada: ", mensagem_descriptografada)

if __name__ == "__main__":
    main()
