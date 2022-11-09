ДЗ 2
====

Блок 1
-------
Скриншоты для п.1 находятся в папке ./screenshots


Блок 2
-------
Процесс запуска:

#. Pip
    Файл requirements находится в корне репозитория
#. Скачивание
    Запустить `dvc repro` (в текущей папке) для скачивания kaggle файлов (нужны KAGGLE переменные окружения)
#. Билд и запуск докеров
    Запустить скрипт `./build.sh`, затем `./run.sh`
#. Загрузка таблицы
    Открыть hue_. Добавить таблицу в `default DB`. Путь csv: `/2/data/artists.csv`. Назвать таблицу artists.
    Если таблица была создана неверно, можно переименовать и проверить командами `ALTER TABLE default.hue__tmp_artists RENAME TO default.artists;
    SELECT count(*) FROM artists;`. Ответ должен быть `1466083`.
#. Само задание
    #. Зайти в докер namenode, запустить `./run_pipe`
    #. Запустить `. ./venv/bin/activate`
    #. Запустить `python a.py`
    #. Запустить `python b.py`
    #. Запустить `python c.py`
    #. Запустить `python d.py`
#. Ответы находятся в файле `results.txt`, скриншоты в папке `screenshots`
    #. The Beatles
    #. seen live
    #. {'alternative': 'Radiohead', 'electronic': 'Radiohead', 'experimental': 'Radiohead', 'indie': 'Radiohead', 'seen live': 'Radiohead', 'female vocalists': 'Lady Gaga', 'pop': 'The Beatles', 'rock': 'The Beatles', 'all': 'Metallica', 'under 2000 listeners': 'Joyce Manor'}
    #. ['united states', 'united kingdom', 'germany', 'japan', 'france', 'sweden', 'russia', 'italy', 'canada', 'spain']




.. _hue: 127.0.0.1:8888