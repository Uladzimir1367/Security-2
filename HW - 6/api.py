import vt
import os

# API-ключ VirusTotal
API_KEY = 'API-ключ VirusTotal'

# Имя файла в текущей директории программы
file_name = 'Имя файла.exe'

# Получение абсолютного пути к файлу
file_path = os.path.join(os.path.dirname(__file__), file_name)

# Инициализация клиента VirusTotal
client = vt.Client(API_KEY)

try:
# Отправка файла
   with open(file_path, 'rb') as file:
      analysis = client.scan_file(file)
      print(f'Файл отправлен на анализ. ID анализа: {analysis.id}')

# Получение отчета о файле
      analysis = client.get_object(f'/analyses/{analysis.id}')
      analysis_result = f'Результат анализа: {analysis.stats}'
      print(analysis_result)

# Запись результата анализа в файл
   with open('analysis_result.txt', 'w') as result_file:
      result_file.write(analysis_result)
      print("Результат анализа записан в файл 'analysis_result.txt'.")
finally:
# Закрытие соединения с клиентом
   client.close()











