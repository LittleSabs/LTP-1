try:
   # Código que pode levantar uma exceção
   print('e'+2)
except Exception as e:
   # Código que será executado se uma exceção ocorrer
   # no bloco try
   print("Ocorreu um erro:", e)
#########################################################
try:
   # Código que pode gerar uma exceção específica
   dividendo = 10
   divisor = 0
   resultado = dividendo / divisor
except ZeroDivisionError as e:
   # Captura apenas exceções de divisão por zero
   print("Divisão por zero não é permitida:", e)
#########################################################
try:
   # Código que pode gerar múltiplos tipos de exceções
   valor = int(input("Digite um número: "))
   resultado = 10 / valor
except ValueError as e:
   # Executado se um ValueError ocorrer
   print("Por favor, insira um número válido:", e)
except ZeroDivisionError as e:
   # Executado se um ZeroDivisionError ocorrer
   print("Divisão por zero não é permitida:", e)
else:
   print("Você digitou o número", valor,
         'e o resultado é',resultado)
#########################################################
try:
   valor = int(input("Digite um número: "))
except ValueError:
   print("Isso não é um número!")
finally:
   print("Esta mensagem será impressa não importa o que aconteça.")