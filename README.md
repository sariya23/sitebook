# Книжный сайт
## Описание
Мое первое приложение на Django. Функиональность - CRUD. Можно добавлять, редактировать и проссматривать информацию и книгах. Операция редактирования доступна только пользователям с правами на редактирование, выдаваемых через админку Django. Также реализована регистрация пользователей и восставновление пароля по почте.
## Локальный запуск
1. Клонирование репозитория
    
    - `git clone git@github.com:sariya23/sitebook.git` - по SSH
    
    - `git clone https://github.com/sariya23/sitebook.git` - по HTTP
2. Установка зависимостей
    
     В корне проекта создать виртуальное окружение, выполнив команду:
    `python -m venv venv`
   
   `. venv/bin/activate`
    
    Далее через менеджер пакета установить зависимости:
    
    `pip install -r requirements.txt`

3. Далее нужно выполнить миграции и создать супер пользователя
   
   В корне проекта выполнить команды:
   
   `python3 manage.py makemigrations`
   
   `python3 manage.py migrate`

   `python3 manage.py createsuperuser`
   
   Далее придумать логин и пароль, действовать так, как будет выводится в консоль
   
4. Переменные окружения
   
      Если вы хотите использовать командый бекенд, то нужно изменить переменную `EMAIL_BACKEND` на `django.core.mail.backends.console.EmailBackend`. Тогда ссылка на восстановление пароля будет приходить в консоль. Но переменные окружения все равно поставить надо!!!

   Для работыы алгоритма восстановления пароля можно воспользоваться либо django-бекендом SMTP, либо использовать бекенд консоли. 
   
   Какой бы вариант вы не выбрали, нужжно установить переменные окружения в файле `.env`, чтобы скрипт их загрузки все не ломал.
   
   В файле `.env.example` приведены переменные окружения со значениями.
   
   - `SECRET_KEY` - ключ для шифрования в django. Можно сгенерировать самому. Любая строка. 
   - `SMTP_KEY` - в этой переменной лежит ключ от настроенного под приложение почтового ящика yandex. **Если используете бекенд консоли, то можно придумать любую строку.**
   - `EMAIL_HOST_USER` - указывается почтовый ящик. **Если используете бекенд консоли, то можно придумать любую строку.**
   - `EMAIL_HOST` - название email хоста. **Если используете бекенд консоли, то можно придумать любую строку.**
   -
5. Запуск
   Для запуска в корне проекта выполнить:

   `python3 manage.py runserver`
   