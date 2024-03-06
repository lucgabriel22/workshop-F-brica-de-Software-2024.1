# Calculadora de IMC


def calculo():
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))
    imc = peso / (altura/100)**2
    if imc <= 18.5:
        print(f'seu IMC: {imc:.2f}, Magreza. Por favor consultar um médico!')
    elif imc >= 18.6 and imc < 24.9:
      print(f'seu IMC: {imc:.2f}, Peso normal')
    elif imc >= 25.0 and imc < 29.9:
      print(f'seu IMC: {imc:.2f}, Sobrepeso')
    elif imc >= 30.0 and imc < 39.9:
      print(f'seu IMC: {imc:.2f}, Obesidade')
    elif imc >= 40:
      print(f'seu IMC: {imc:.2f}, Obesidade grave')

    else:
      print('Digite um valor válido!')
    



calculo()