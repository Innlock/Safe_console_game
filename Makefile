SCRIPT = safe.py

WIN = win
LIN = lin

# onefile - упаковать все файлы проекта в один исполняемый файл
# distpath - указывает, где должен быть размещен полученный исполняемый файл
# workpath - задает рабочую директорию для PyInstaller, где временные файлы будут созданы
# specpath - где будет создан файл спецификации 
# clean - PyInstaller очистит временные файлы и каталоги после создания исполняемого файла
WIN_EXE = --onefile $(SCRIPT) --distpath $(WIN) --workpath $(WIN) --specpath $(WIN) --clean
LIN_EXE = --onefile $(SCRIPT) --distpath $(LIN) --workpath $(LIN)/safedir --specpath $(LIN) --clean

# all: win lin

win:
	mkdir $(WIN)
	pip install pyinstaller
	pyinstaller $(WIN_EXE)
# запуск полученного исполняемого файла
	./$(WIN)/safe.exe


lin:
	mkdir -p $(LIN)/safedir
	pip3 install pyinstaller
	pyinstaller $(LIN_EXE)
	./$(LIN)/safe


web:
#  запускает командную оболочку Windows с параметром /c (выполнение одной команды) -> открывает веб-страницу по адресу
	cmd /c start http://localhost:8080/index.html
# запускает веб-сервер на порту 8080
	python -m http.server 8080


clean_win:
# рекурсивно и принудительно удалять все файлы и поддиректории, находящиеся в директории
	rd /s /q $(WIN)


clean_lin:
	rm -rf $(LIN)