b64_index = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def convert_string(input_bytes):
    converted = ''

# Cria lista "bin" com a conversão dos bytes da string para binário, removendo o "2b" e preenchendo com 0 os
# digítos restantes do número binário
    bin = list(''.join([bin(byte)[2:]].zfill(8) for byte in string))
