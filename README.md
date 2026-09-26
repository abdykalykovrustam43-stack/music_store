Music Store API
Backend-сервер мини музыкального магазина  на Django REST Framework.

1.Python
2.Django
3.Django REST Framework
4.JWT Authentication
5.drf-spectacular / Swagger
6.SQLite
включает в себя :
1.User registration
2.JWT authentication
3.User profile
4.Music catalogue
5.Saved music
6.Add and remove saved tracks
7.REST API
8.Swagger API documentation
API
 endpoints:
1.POST /register/ — регистрация пользователя
2.POST /login/ — вход и получение JWT-токенов
3.POST /login/refresh/ — обновление access-токена
4.GET /profile/ — профиль пользователя
5.GET /sound/ — список музыки
6.POST /sound/create/ — добавление композиции
7.GET /saved/ — сохранённые композиции
8.POST /saved/ — добавить композицию в сохранённые
9.DELETE /saved/<id>/ — удалить сохранённую композицию
API документация
Swagger:
/swagger/
