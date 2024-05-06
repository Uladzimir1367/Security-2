# Программа проверяет сложность пароля и сохраняет его хэш-значение в файл:

import hashlib

def save_hashed_password(password):
# Проверка длины пароля
   if len(password) < 8:
      return 'Пароль должен содержать не менее 8 символов.'
   # Проверка наличия прописных и строчных букв, а также цифр
   if not any(char.islower() for char in password):
      return 'Пароль должен содержать хотя бы одну строчную букву.'
   if not any(char.isupper() for char in password):
      return 'Пароль должен содержать хотя бы одну прописную букву.'
   if not any(char.isdigit() for char in password):
      return 'Пароль должен содержать хотя бы одну цифру.'
   # Проверка, что пароль не состоит только из цифр
   if all(char.isdigit() for char in password):
      return 'Пароль не должен состоять только из цифр.'


# Хэширование пароля
   hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
   # Сохранение хэша в файл
   with open('hashed_password.txt', 'w') as file:
      file.write(hashed_password)
      return 'Пароль успешно сохранён в файл.'
   # Проверка выполнения программы
user_password = input('Введите ваш пароль: ')
result = save_hashed_password(user_password)
if result:
   print(result)
else:
   print('Произошла ошибка при сохранении пароля.')
   