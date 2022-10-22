# Бонусные задачи:
- Запуск используя Docker
- Использование environment variables
- Просмотр Django Моделей в Django Admin панели
- Запуск приложения на удаленном сервере, доступном для тестирования
- Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items

# Небольшие изменения

Из-за отсутствия чёткий требований по реализации модели Order, изменён список методов

/buy/item/id - как /buy/id в задании

/buy/order/id - аналогично /buy/item/id, но для заказа из нескольких товаров

/item/id - как в задании

/order/id - аналогично /item/id, но для заказа из нескольких товаров

При необходимости возможно сокращение кол-ва методов путём усложнения страницы item/id

# Запуск

## Без использования docker

Устанавливаем пакеты: `pip install -r requirements.txt`

Подготавливаем БД: `python manage.py makemigrations` `python manage.py migrate`

Далее необходимо:

1) Указать переменные среды `sk` и `pk` для секретного и публичного ключей API соответственно (для windows: `set var=val`, для linux: `export var=val`)
2) Добавить админа: `python manage.py createsuperuser`

Запускаем сервер: `python manage.py runserver`

Переходим по http://127.0.0.1:8000/

## С использованием docker

Скачиваем образ с https://hub.docker.com/r/silverfatt/django-stripe: `docker pull silverfatt/django-stripe`

Или собираем образ на месте (необходимо находиться в корне проекта): `docker build -t django-stripe .`

Запускаем контейнер: `docker run -d --name CONTAINER_NAME -p 80:80 -e sk=SECRET_KEY -e pk=PUBLIC_KEY django-stripe`, вместо `CONTAINER_NAME`, `SECRET_KEY` и `PUBLIC_KEY` указываем имя контейнера (произвольно), секретный ключ и публичный ключ соответственно.

Затем в CLI контейнера добавляем админа: `python manage.py createsuperuser`

Переходим по http://127.0.0.1:80/

# Подготовка к работе с API

В БД через админку необходимо добавить товары и добавить их в магазин (см.фото ниже, если не добавить их в магазин, при попытке покупки будет показываться сообщение о недоступности товара). 
![image](https://user-images.githubusercontent.com/90452368/191329990-8004fb16-a2e3-477d-8403-fa99b3d58c2b.png)

После добавления товаров можно добавить заказы: json'ы вида  
```json
[{"id": 1, "amount": 2}, {"id": 2, "amount": 3}, ...]
```
`id` - id товара, `amount` - количество.

После создания товаров, добавления их в магазин можно начинать использовать методы `/item/id` и `/buy/item/id`
После создания заказов можно начинать использовать методы `/order/id` и `/buy/order/id`

В админке предусмотрены поиск продукта по id и имени, заказа - по id.
![image](https://user-images.githubusercontent.com/90452368/191330985-6f01fa18-0ac7-4a7e-bf13-80122ef68142.png)
![image](https://user-images.githubusercontent.com/90452368/191331025-8c5a459d-87ac-424f-8d38-93fc7978f1d2.png)






