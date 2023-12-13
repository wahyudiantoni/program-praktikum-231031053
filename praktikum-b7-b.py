import os
os.system('cls')
a = True

while a:
    jawab = input('Apa ingin lanjutkan? (y/n)')
    if jawab == 'y':
        os.system('cls')
        print('Selamat datang lagi:')
        a = True
    elif jawab == 'n':
        print('sampe ketemu lagi :D')
        a = False
    else:
        os.system('cls')
        print('jangan aneh-aneh deh :.)')
        a = False