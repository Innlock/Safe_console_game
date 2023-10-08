# Safe_console_game

Команды следует вводить в консоли с правами администратора (должен быть установлен pip и pip3 для linux):
* `make win` - создает исполняемый exe файл для windows
* `make lin` - создает исполняемый файл для linux
* `make web` - запускает веб-сервер и открывает веб-страницу
* `make clean_win` - удаляет созданные командой `make win` файлы
* `make clean_lin` - удаляет созданные командой `make lin` файлы
* `make test` - проводит тест

`pytest test.py` - проводит несколько тестов в pytest (должен быть установлен pytest)