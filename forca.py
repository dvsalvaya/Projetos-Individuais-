def main():
    print('Bem vindo ao jogo da Forca :)')
    
    str_secreta = input('Digite a palavra secreta\n-> ')
    palavra_secreta=list(str_secreta)
    palavra_descoberta = ['-']*len(palavra_secreta)
    resposta = palavra(palavra_secreta,palavra_descoberta)
    print()
    while resposta != palavra_secreta:
        print('##############')
        print('Digite uma letra :)')
        r = input('-> ')
        print()
        resposta = palavra(palavra_secreta,resposta,r)
        print(resposta)
        print()
    print('##############')

    print(f'Parabéns, a palavra secreta é {str_secreta}\n')
def palavra(palavra_secreta,palavra_descoberta,letra = ''):
    
    for i in range(len(palavra_secreta)):
        if letra == palavra_secreta[i]:
            palavra_descoberta[i] = letra
    return palavra_descoberta
        
main()