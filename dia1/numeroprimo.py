n1 = input(int('Digite um número: '))

def primo():
    if n1 > 1:
        for i in range(2, n1):
            print(n1, 'não é par')
            break
        else:
            print(n1, 'é primo')






            
primo()