import nmap
import csv

# Создаем объект сканера
nm = nmap.PortScanner()

# Запускаем сканирование
nm.scan('127.0.0.1', '22-443')

# Открываем файл CSV для записи
with open('result.csv', 'w', newline='') as csvfile:
   fieldnames = ['host', 'protocol', 'port', 'state', 'name', 'product', 'version', 'extrainfo']
   writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

   # Записываем заголовки
   writer.writeheader()
   # Проходим по всем хостам и записываем информацию о портах
   for host in nm.all_hosts():
      for proto in nm[host].all_protocols():
         lport = sorted(nm[host][proto].keys())
         for port in lport:
            service = nm[host][proto][port]
            writer.writerow({
               'host': host,
               'protocol': proto,
               'port': port,
               'state': service['state'],
               'name': service['name'],
               'product': service.get('product', ''),
               'version': service.get('version', ''),
               'extrainfo': service.get('extrainfo', '')
            })
print("Сканирование завершено и результаты записаны в 'result.csv'")                         
          

               

