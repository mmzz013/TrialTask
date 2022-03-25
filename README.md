Для установки всех необходимых библиотек нужно прописать в терминале команду:
```commandline
pip install -r requirements.txt
python manage.py migrate
```
И заполнить `.env` на подобии `.example.env`

Для запуска локального сервира необходимо прописать в терминале команду:
```commandline
python manage.py runserver
```


## POST /api/auth

### Авторизация пользователя

### Body
```json
{
  "phone_number": "89284551190"
}
```

### Response 200
```json
{
    "refresh": "{refresh_token}",
    "access": "{access_token}"
}
```

### Response 401
```json
{
    "detail": "Не найдено активной учетной записи с указанными данными"
}
```

## GET /api/user_info/

### Выдаёт информацию о профиле

### Headers
```json
{
  "Authorization": "Bearer {access_token}"
}
```

### Response 200
```json
{
    "user": {
        "phone_number": "89993100133",
        "invite_code": "R85211",
        "invited_by": 4,
        "list_of_invitees": [
            "89991111111"
        ],
        "inviter_code": "T5K0EW"
    }
}
```
### Response 401
```json
{
    "detail": "Учетные данные не были предоставлены."
}
```
### Response 401
```json
{
    "detail": "Данный токен недействителен для любого типа токена",
    "code": "token_not_valid",
    "messages": [
        {
            "token_class": "AccessToken",
            "token_type": "access",
            "message": "Токен недействителен или просрочен"
        }
    ]
}
```

## POST /api/user_info/

### Позволяет ввести 1 инвайт код другого пользователя

### Headers
```json
{
  "Authorization": "Bearer {access_token}"
}
```

### Body
```json
{
  "invite_code": "12sd314"
}
```

### Response 200
```json
{
  "message": "Все прошло успешно"
}
```

## POST /api/code/

### Ввод 4х значного кода из СМС

### Headers
```json
{
  "Authorization": "Bearer {access_token}"
}
```
### Body
```json
{
  "code": "1121"
}
```

### Response 200
```json
{
    "message": "код успешно принят"
}
```
### Response 400
```json
{
    "detail": "JSON parse error - Expecting ',' delimiter: line 2 column 14 (char 15)"
}
```

