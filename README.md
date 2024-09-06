# Final_work
Финальная работа по атоматизации

### Задача проекта
Автоматизировать UI- и API-тесты из финальной работы по ручному тестированию

### Структура проекта
Проект включает в себя:
1. Папка pages. Здесь находятся файлы с созданными классами для API-тестов и UI-тестов
2. Папка test. Содержит в себе 2 файла с тестами: API-тесты и UI-тесты
Также проект включает в себя вспомогательные файлы:
- constants.py - содержит данные для импорта: ссылки, данные для авторизации, токены для API-запросов 
- requirements.txt - содержит перечень всех зависимостей, необходимых для проекта

### Библиотеки (!)
- pyp install pytest
- pip install selenium
- pip install webdriver-manager
- pyp install allure-pytest
- pip install requests

### Шаги
1. Склонировать проект 'git clone https://github.com/Elena-Hay/Final_work.git'
2. Установить зависимости
3. Запустить тесты: 
- для запуска всех тестов 'pytest'
- для запуска UI-тестов: 'pytest test_ui_fun_and_sun.py'
- для запуска API-тестов: 'pytest test_api_fun_and_sun.py'
4. Сгенерировать отчет 'allure generate allure-files -o allure-report'
5. Открыть отчет 'allure open allure-report'
