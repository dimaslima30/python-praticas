from ctypes.wintypes import PBOOL
from hashlib import pbkdf2_hmac


estado = input('digite a sigla do seu Estado: ')
if estado == "PE" or estado == "PB":
    print('Você é cabra da peste!')
if estado == "SP" or estado == "RJ":
    print('Você é sudestino fedido.')
