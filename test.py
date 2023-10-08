import shutil, os
import subprocess
import difflib


def init_test(a,b,c):
  # создаем копии файлов с предопределенными значениями
  os.mkdir('tests')
  shutil.copyfile('safe.bas', 'tests/safe_test.bas')
  with open ('tests/safe_test.bas', 'r') as f:
    old_data = f.read()

  new_data = old_data.replace('260 A=INT(RND(1)*81)+10\n270 B=INT(RND(1)*81)+10\n280 C=INT(RND(1)*81)+10', f'260 A={a}\n270 B={b}\n280 C={c}')

  with open ('tests/safe_test.bas', 'w') as f:
    f.write(new_data)

  shutil.copyfile('safe.py', 'tests/safe_test.py')
  with open ('tests/safe_test.py', 'r') as f:
    old_data = f.read()

  new_data = old_data.replace('return (A, B, C), A1', f'return ({a}, {b}, {c}), A1')

  with open ('tests/safe_test.py', 'w') as f:
    f.write(new_data)

  # сравнение выводов
  res1 = subprocess.run([f'C:\Python310\python.exe',f'tests/safe_test.py'],input=f'YES\nYES\n{a}\n{b-2}\n{b}\n{c}\nNO\n',capture_output=True,text='utf-8')
  res1 = res1.stdout

  res2 = subprocess.run(f'tests\safe_test.bas',input=f'YES\nYES\n{a}\n{b-2}\n{b}\n{c}\nNO\n', shell=True,capture_output=True,text='utf-8')
  res2 = res2.stdout[:-45]

  matcher = difflib.SequenceMatcher(None, res2, res1)
  print("overlap: "+ str(matcher.ratio()))

  # запись вывода в файлы
  with open("text_new.txt", "w") as file:
      file.write(res1)
  with open("text_original.txt", "w") as file:
      file.write(res2)

  shutil.rmtree('tests')
  return res1, res2


def test1():
  res1, res2 = init_test(71, 38, 83)
  assert res1 == res2

def test2():
  res1, res2 = init_test(84, 44, 72)
  assert res1 == res2

def test3():
  res1, res2 = init_test(76, 30, 31)
  assert res1 == res2


init_test(71, 38, 83)