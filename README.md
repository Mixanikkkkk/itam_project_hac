Сайт для поиска команды на хакатон 

Frontend - Svetle
Backend - Python(FastAPI, uvicorn, pydantic, sqlalchemy)
Redis - используется для сохранения данных сессий
MySQL - основняа БД

Устройство проекта:
app - бекенд
frontend - фронт

Описание структуры:
Проект осуществялет регистрацию пользователя на сайте с проверкой на оригинальность username и email
Пароль шифруется и сохраняется в СУБД
Логин на сайт происходит через usernname и пароль и осуществляетяс с помощью сохраненяи сессий в Redis
Используется проверка для определения прав пользователя на сайте
Авторизованный пользователь может создавать команды и отправлять приглашения другим пользователям
Пользователь может отклонить или принять инвайт


