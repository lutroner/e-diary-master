# Скрипт для модификации базы данных электронного журнала

### Описание

Данный скрипт используется для модификации базы данных электронного журнала с использованием ORM. Электронный журнал -
это Django приложение с базой данных Sqlite. У скрипта есть следующие возможности по модификации БД:

1. Находить плохие оценки (двойки и тройки) по заданному имени ученика и исправлять их на пятерки
2. Находить замечания по заданному имени ученика и удалять их
3. По заданному имени ученика и предмету создавать похвалу для случайного урока

### Как установить

Необходимо скопировать файл `scripts.py` на сервер сайта электронного дневника в директорию `e-diary-master`.
В этой же директории должен находиться файл `manage.py`.

### Как использовать

1. Находясь в директории `e-diary-master` откройте консоль и запустите Django Shell:

```console
$ python manage.py shell 
```

2. Импортируйте все необходимые функции из файла `scripts.py`

```console
$ from scripts import *
```

3. Для замены плохих оценок на хорошие

```console
$ fix_marks(name)
```

где `name` здесь и далее ФИО ученика полностью с заглавных букв.

4. Команда для удаления всех замечаний:

```console
remove_chastisements(name)
```

5. Чтобы добавить похвалу для случайного урока заданного предмета заданного ученика:

```console
create_commendation(name, subject):
```

где `subject` - название предмета с заглавной буквы, а `name`  ФИО ученика полностью с заглавных букв.

### Как проверить

Перейдите на главную страницу сайта электронного журнала. Перейдите на страницу класса и найдите нужного ученика.
Убедитесь, что все плохие оценки были исправлены, а плохие замечания удалены. Убедитесь, что внизу страницы ученика
появились соответствующие хвалебные отзывы.
