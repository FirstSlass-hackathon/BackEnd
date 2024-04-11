# Backend for Firstclass

## Настройка отправки сообщения
1. Создаем в корневой папке файл .env.
2. Входим в google-аккаунт -> Безопасность -> Пароли приложений. Создаем пароль приложения.
3. Записываем в файл .env ключи:
   * ACCOUNT_NAME=ваша_почта_до_@gmail.com
   * ACCOUNT_PASSWORD=пароль_вашего_приложения
4. Для того чтобы проверить корректность отправки почты, нужно ввести команду ```py manage.py test rest_api.tests```