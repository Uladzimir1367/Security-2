import hashlib

# Функция для вычисления хэша SHA-256
def calculate_sha256(text):
   sha_signature = hashlib.sha256(text.encode()).hexdigest()
   return sha_signature

# Функция для записи хэша в файл
def save_hash_to_file(hash_value, file_name):
   with open(file_name, 'w') as file:
      file.write(hash_value)

# Основная часть программы
if __name__ == "__main__":
   text_to_hash = input("Введите текст для вычисления хэша SHA-256: ")
   hash_value = calculate_sha256(text_to_hash)
   print(f"Хэш-значение для текста '{text_to_hash}' это: {hash_value}")

# Запрашиваем у пользователя имя файла для сохранения хэша
   file_name = input("Введите имя файла для сохранения хэш-значения: ")
   save_hash_to_file(hash_value, file_name)
   print(f"Хэш-значение было сохранено в файле {file_name}")