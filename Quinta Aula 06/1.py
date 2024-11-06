import hmac
from hashlib import md5
key = b'DECLARATION'
h = hmac.new(key,b' ',md5)
# adicona o conteudo da mensagem

h.update(b'Teste de HMAC!!!')
#imprime a assinatura/hash HMAC
print (h.hexdigest() )