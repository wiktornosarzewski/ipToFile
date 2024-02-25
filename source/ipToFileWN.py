import requests
import json
from datetime import datetime
#by Wiktor Nosarzewski 25-2-24
def get_public_ip():
    endpoint = 'https://ipinfo.io/json'
    response = requests.get(endpoint, verify=True)
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        exit()
    data = response.json()
    return data['ip']

# Pobierz publiczny adres IP
my_ip = get_public_ip()

# Zapisz adres IP do pliku
with open('public_ip.txt', 'a') as file:
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    file.write(f'{timestamp} - {my_ip}\n')

print(f'Twój publiczny adres IP to: {my_ip}')
print('Adres IP został zapisany do pliku public_ip.txt.')
