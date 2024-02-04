# Проект для генерации коротких ссылок с веб-интерфейсом и API.

Проект YaCut — это сервис укорачивания ссылок. 
Его назначение — ассоциировать длинную пользовательскую ссылку с короткой,
которую предлагает сам пользователь или предоставляет сервис.

Например, ссылка
https://yacut.ru/di
воспринимается лучше, чем 
https://habr.com/ru/companies/otus/articles/505342/

# Стэк технологий

Flask, SQLAlchemy

# Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:VitaliyPavlow/yacut.git
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
# Запуск проекта из корневой директории
```
flask run
```
