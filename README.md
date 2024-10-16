
# Python Criptografia Segundo Semestre 2024

Este repositório contém os materiais e questões de criptografia usando Python. Ele abrange conceitos essenciais de criptografia e será atualizado até o fim desse semestre.

## Índice

- [Instalação](#instalação)
- [Exemplos de Uso](#exemplos-de-uso)
- [Estudos e Links Úteis](#estudos-e-links-úteis)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

## Instalação

Para começar, você precisará de Python 3.x instalado. Recomendamos o uso de um ambiente virtual para gerenciar dependências.

### 1. Clonar o repositório

```bash
git clone [https://github.com/Gabrieel-Lopees/PythonCrypto.git]
cd PythonCrypto
```

### 2. Criar um ambiente virtual e instalar dependências

```bash
python -m venv venv
source venv/bin/activate  # Para Linux/macOS
venv\Scripts\activate     # Para Windows

pip install -r requirements.txt
```

### 3. Dependências

O arquivo `requirements.txt` inclui as seguintes bibliotecas:

- [cryptography](https://cryptography.io/en/latest/)
- [PyCryptoDome](https://www.pycryptodome.org/)
  
Instale todas com:

```bash
pip install cryptography pycryptodome
```

## Exemplos de Uso

### 1. Criptografia Simétrica com AES

```python
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)
nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(b"Mensagem secreta")
```

### 2. Criptografia Assimétrica com RSA

```python
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Gerar chave privada
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Serializar chave privada para salvar em um arquivo
pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.BestAvailableEncryption(b"minha-senha")
)

with open("private_ke]y.pem", "wb") as f:
    f.write(pem)
```

## Estudos e Links Úteis

Aqui estão alguns recursos úteis para aprender mais sobre criptografia em Python e segurança:

- [Documentação da Biblioteca Cryptography](https://cryptography.io/en/latest/)
- [PyCryptodome - Guia Completo](https://www.pycryptodome.org/)
- [RSA - Introdução e Implementação](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
- [OWASP Cryptography Cheatsheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
- [Guia de Segurança em Python](https://realpython.com/python-security/)

## Contribuindo

Contribuições são bem-vindas! Contate Gabrieel-Lopees para saber como contribuir!

## Licença

Este projeto é licenciado sob os termos da licença da Universidade Federal de Santa Maria.
