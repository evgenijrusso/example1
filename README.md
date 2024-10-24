#  Замечания
- Запуск проекта:
В терминале запускаем команду `poetry new example1`, потом находим его в каталоге и открываем в `pycharm`.  
- И сразу добавляем интерпретатор питона для создания виртуального окружения.
- `poetry init` используется, если проект уже существует.

##  Установка
- poetry add fastapi[all]   
-  poetry add pydantic[email]
- poetry add sqlalchemy, psycopg, asyncpg, pymysql (p.s. sqlalchemy не установилось сразу)
- poetry show --tree (проверка зависимостей)
- poetry add black --group dev (p.s. пока поставил через `settings`)
- poetry add aiosqlite