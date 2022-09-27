#phonenumbers -> fornece vários recursos, como informaçes básicas de um número de telefone, validação... etc.

import phonenumbers

from phonenumbers import geocoder, carrier, timezone


phone = input('Digite o telefone no formato: +5511080012345: ')

phone_numbers = phonenumbers.parse(phone)

print("Este telefone esta localizado em: ")
print(geocoder.description_for_number(phone_numbers, 'pt'))
print("Utiliza a operadora: ")
print(carrier.name_for_number(phone_numbers, 'pt'))
print("E o fuso horário: ")
print(timezone.time_zones_for_geographical_number(phone_numbers))





