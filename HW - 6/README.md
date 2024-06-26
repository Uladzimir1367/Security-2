### Урок 6. Семинар: Основные технологии и инструменты обеспечения ИБ (некриптографические)

Самостоятельно выполнить задания 2 и 3 с операционными системами.

Доп. задание: напишите программу на Python, которая будет взаимодействовать с API VirusTotal.

Направьте ответы в текстовом файле:
— текст задания
— скриншот выполнения (последовательность на слайдах)

Все задания выполнены на Windows10 и Linux (Ubunty). 

### Задание №2 “Дискреционное управление доступом”

Вам как ИБ-специалисту необходимо настроить дискреционный доступ к каталогу
с файлами «Recovery», куда помещаются резервные копии (выгрузки) из базы данных:
📌 Один каталог «Recovery» (место размещения на усмотрение студента).
📌 Права только на чтение каталога для отдельного пользователя
#### Задание выполнено для Windows и Linux
Для Windows<br>

Создаю нового пользователя
<image src="img/Пользователи.png" alt="wind">

Создаю папку и открываю к ней общий доступ
<image src="img/Общий доступ к папке.png" alt="Windows">

Откпываю в папке -> свойства -> безопасность

<image src="img/Папка свойства безопасность.png" alt="Windows">


Меняю права пользователя в разделе "Безопасность" объект "RECOVERY"
<image src="img/Разрешения.png" alt="wind">

Для Linux <br>
Создаю  директрорию recovery

<image src="img/папка recovery в директории.png" alt="linux">

Создаю новых пользователей User1, user2

<image src="img/Новый пользователь.png" alt="linux">

Определяю доступ пользолвателей к директории
<image src="img/доступ пользователей к папке.png" alt="linux">

Ограничиваю в правах user2

<image src="img/Права пользователей.png" alt="linux">


### Задание №3 “Просмотр событий” (вопрос для Windows)

Вам как ИБ-специалисту необходимо проанализировать историю входов в операционную систему Windows.
📌 Вызвать MSC-оснастку «Просмотр событий» (Event Viewer) в Windows разными способами:
● Комбинация WIN + R (или приложение «Командная строка») и ввести eventvwr.exe
или eventvwr.msc, или eventvwr.
● Комбинация Windows + X и выбрать «Просмотр событий».
● Найти в каталоге %SystemRoot%\System32 eventvwr.exe или eventvwr.msc
📌 Найти события успешного входа: id 4624.
📌 Выйти из операционной системы, повторно войти, сначала введя неверный пароль,
найти событие неуспешного входа: id 4625.

<image src="img/Вызов журнала.png" alt="linux">

<image src="img/Просмотр событий.png" alt="linux">

<image src="img/Событие 4624.png" alt="linux">

<image src="img/Аудит отказа 4625.png" alt="linux">


### Задание №3 “Просмотр событий” (вопрос для Linux)

Вам как ИБ-специалисту необходимо проанализировать историю входов в операционную систему Linux:
📌 Просмотреть данные в журналах аутентификации:
● /var/log/secure (для Red Hat like).
● /var/log/auth.log (для Debian like).
📌 Найти события успешного входа.

### Для Ubunty - журнал событий, вход в систему.

<image src="img/Linux 1.png" alt="linux">

#### Журнал

<image src="img/Журнал - linux.png" alt="linux">

### Программа на Python, которая отправляет файл на проверку и получает отчет о нём (взаимодействует с API VirusTotal.) 
Пояснения выполнения приведены в api.py.
Для запуска требуется API-ключ VirusTotal.<br>
Устновим библиотеку vt-py для запуска программы. Результат запишем в файл analysis_result.txt
Анализируемый файл залить не удалось!


<image src="img/Результат выполнения.png" alt="программа">
