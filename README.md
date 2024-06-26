# TraidingNetwork

#### Установка зависимостей осуществляется с помощью команды: `pip install -r requirements.txt`


## Торговая сеть - механика работы сайта

### Сеть представляет собой иерархическую структуру из трех уровней:
- завод
- розничная сеть
- индивидуальный предприниматель

Каждое звено сети ссылается только на одного поставщика оборудования.
Важно отметить, что уровень иерархии определяется не названием звена, а отношением к остальным элементам сети.
Завод всегда находится на уровне 0, а если розничная сеть относится напрямую к заводу, минуя остальные звенья, ее уровень — 1.

### Каждое звено сети обладает следующими элементами:

- **название**
- **контакты**:
  - email 
  - страна
  - город
  - улица
  - номер дома
- **продукты**:
  - название
  - модель
  - дата выхода продукта на рынок
  - цена
- **поставщик**
- **задолженность перед поставщиком в денежном выражении с точностью до копеек**
- **время создания (заполняется автоматически при создании)**

### Созданные объекты выводятся в админ панели в виде таблицы.
#### Также существует возможность создания и редактирования объектов в админ панели.

### На странице объекта сети добавлены:
- ссылка на «Поставщика»
- фильтр по названию города и страны
- admin action, очищающий задолженность перед поставщиком у выбранных объектов

#### Редактирование поля задолжности запрещено.
#### Права доступа имеют только активные сотрудники.
#### Уровень поставки ('supply_level') выставляется автоматически.

### При создании поставщика функционируют следующие валидации:
 - у завода ('seller_type') не может быть поставщика ('supplier_name')
 - на нулевом уровне поставки ('supply_level') может находиться только завод ('seller_type')
 - уровень поставщика должен быть на 1 выше уровня вашего поставщика ('supply_level')
 - при выборе типа сети не завод ('seller_type') обязательно должен быть поставщик ('supplier_name')
 - у завода ('seller_type') не может быть задолженности ('debt')
 - тип сети не может быть пустым ('seller_type')

#### Для проверки фильтрации поставщика по стране: `http://127.0.0.1:8000/supplier/?contact__state=Bolivia`
#### Для проверки фильтрации контакта по стране: `http://127.0.0.1:8000/contact/?state=Bolivia`

### В корневой папке проекта лежат фикстуры контактов, продуктов и поставщиков - traidingnet.json. 
### Фикстуры пользователей - users.json.
### Фикстуры модераторов - moderator.json.
### Для загрузки фикстур нужно выполнить команды:
- `python -Xutf8 manage.py loaddata traidingnet -o traidingnet.json`
- `python -Xutf8 manage.py loaddata users -o users.json`
- `python manage.py loaddata moderator.json`


### В папке management представлены файлы для создания разных видов пользователей: 
- **обычного (CU)**:
  - python manage.py cu
- **модератора (CMU)**:
  - python manage.py cmu
- **суперюзера(CSU)**:
  - python manage.py csu

#### Команды создают пользователей с заданными параметрами:
 - `email`=Почта
 - `first_name`=Имя
 - `last_name`=Фамилия
 - `is_superuser`=(True или False) - задает права администратора
 - `is_staff`=(True или False) - задает права модератора
 - `is_active`=(True или False) - задает активность пользователя

#### Данные email, first_name и last_name нужно указать свои, а поля is_* оставляем по умолчанию.
#### Поле `user.set_password('password')` задает пароль пользователя.