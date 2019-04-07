 
cd 到E盘根目录，执行以下命令即可
注：代码中不嫩有中文注释，否则会出现编码问题导致无法生成exe

pyinstaller -F E:\Python_Study\\project\\MyGame\\pygame_shooting\\main.py E:\Python_Study\\project\\MyGame\\pygame_shooting\\src\\plane.py E:\Python_Study\\project\\MyGame\\pygame_shooting\\src\\textAndbutton.py



//生成的程序在启动时不会打开cmd窗口
pyinstaller -F -w E:\Python_Study\\project\\MyGame\\pygame_shooting\\main.py E:\Python_Study\\project\\MyGame\\pygame_shooting\\src\\plane.py E:\Python_Study\\project\\MyGame\\pygame_shooting\\src\\textAndbutton.py
