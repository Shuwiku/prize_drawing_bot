# -*- coding: utf-8 -*-
"""Запросы к базе данных."""

# Добавляет нового пользователя в базу данных
add_user: str = """
INSERT INTO user (
    uid,
    registration_date
) VALUES (?, ?)
"""

# Создаёт индекс для поля uid таблицы user
create_index_user_uid: str = """
CREATE INDEX IF NOT EXISTS index_uid ON user (uid)
"""

# Создаёт таблицу user
create_table_user: str = """
CREATE TABLE IF NOT EXISTS user (
    uid INTEGER PRIMARY KEY,
    draw_count INTEGER NOT NULL DEFAULT "0",
    language VARCHAR NOT NULL DEFAULT "ru",
    registration_date DATETIME NOT NULL
)
"""

# Получает данные пользователя по его ID
get_user: str = """
SELECT * FROM user WHERE uid = ?
"""

# Получает локаль пользователя
get_user_language: str = """
SELECT language FROM user WHERE uid = ?
"""

# Устанавливает локаль пользователя
set_user_language: str = """
UPDATE user SET language = ? WHERE uid = ?
"""
