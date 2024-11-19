#!/bin/bash

quiet() {
    "$@" > /dev/null 2>&1
}

dirScript=$PWD
dirVenv="$PWD/venv"
fileRequirements="$PWD/requirements.txt"

echo "Создаю виртуальное окружение по адресу: '$dirVenv'."
quiet python3 -m venv "$dirVenv"

echo "Запускаю виртуальное окружение."
quiet source "$dirVenv/bin/activate"

echo "Устанавливаю зависимости из файла: '$fileRequirements'."
quiet python3 -m pip install -r "$fileRequirements"

echo "Запускаю бота."
python3 ./prize_drawing_bot

echo "Нажмите любую клавишу для выхода..."
read -n 1 -s
