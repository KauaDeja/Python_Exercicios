"""
Exercício 04 - Escreva um programa que leia uma temperatura em graus Celsius e a converta para Fahrenheit.
A fórmula de conversão é F = C * 9/5 + 32.

Exemplo de Entrada:
Digite uma temperatura em Celsius para conversão: 25

Exemplo de Saída:
25°C é equivalente a 77.0°F
"""
temp_celsius = float(input("Digite uma temperatura em Celsius para conversão: \n"))
temp_farenheit = temp_celsius * 9/5 + 32
print(f"{temp_celsius} é equivalente a {temp_farenheit}")