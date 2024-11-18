@echo off

REM Устанавливает кодировку на UTF-8
chcp 65001 > nul

set dirScript=%CD%
set dirVenv=%dirScript%\venv
set fileRequirements=%dirScript%\requirements.txt

echo Создаю виртуальное окружение по адресу: '%dirVenv%'.
python -m venv "%dirVenv%" > nul 2>&1

echo Запускаю виртуальное окружение.
call %dirVenv%\Scripts\activate

echo Устанавливаю зависимости из файла: '%fileRequirements%'.
python -m pip install -r "%fileRequirements%" > nul 2>&1

echo Запускаю бота.
python %dirScript%\prize_drawing_bot

pause