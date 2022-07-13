import hashlib

arquivo1 = 'Comparador de Hash/a.txt'
arquivo2 = 'Comparador de Hash/b.txt'

hash1 = hashlib.new('ripemd160')
hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(arquivo2, 'rb') .read())

if hash1.digest() != hash2.digest():
    print(f'O {arquivo1} é diferente do aruquivo {arquivo2}')
    print('O hash do arquivo a.txt é: {}'.format(hash1.hexdigest()))
    print('O hash do arquivo b.txt é: {}'.format(hash2.hexdigest()))
else:
    print(f'O {arquivo1} é gual ao {arquivo2}')
    print('O Hash de ambos arquivos é: {}'.format(hash1.hexdigest()))