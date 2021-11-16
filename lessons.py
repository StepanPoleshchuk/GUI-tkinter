from tkinter import *

root = Tk()

# -----------------------------------------------------------------------------
# 1) обозначение объекта
'''
the_label = Label(root, text='окошко')
the_label.pack()
'''
# -----------------------------------------------------------------------------
# 2) организация главного окна, делим на верхнюю рамку, нижнюю рамку, размещаем кнопки
'''
top_frame = Frame(root)
top_frame.pack()

bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)

button1 = Button(top_frame, text='кнопка 1', fg='red')
button2 = Button(top_frame, text='кнопка 2', fg='blue')
button3 = Button(top_frame, text='кнопка 3', fg='green')
button4 = Button(bottom_frame, text='кнопка 4', fg='gray')

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)
'''
# -----------------------------------------------------------------------------
# 3) дополнительные виджеты в окне, надпись,упаковщик
'''
one = Label(root, text='один', bg='red', fg='yellow')
one.pack()
two = Label(root, text='два', bg='blue', fg='white')  # fill растягивает по оси при изменении размера окна
two.pack(fill=X)
three = Label(root, text='три', bg='green', fg='purple')
three.pack(side=LEFT, fill=Y)
'''
# -----------------------------------------------------------------------------
# 4) Упаковщик grid, таблица с ячейками в которую помещаются различные виджеты
'''
Label_1 = Label(root, text='Имя')
Label_2 = Label(root, text='Пароль')

entry_1 = Entry(root)   # поле в которое пользователь может ввести какую-либо информацию
entry_2 = Entry(root)

Label_1.grid(row=0, column=0, sticky=E)  # строка 0 колонка 0, sticky у какой границы расположиться, N,S,W,E
Label_2.grid(row=1, column=0)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c = Checkbutton(root, text='остаться в системе')  # виджет галочка пункт
c.grid(columnspan=2)   # занимает сразу две колонки
'''
# -----------------------------------------------------------------------------
# 5) добавляем функционал, приложение взаимодействует, реагирует на
#    клик мышкой, нажатие клавиши на клавиатуре
#    Приложение спрашивает сколько ему лет, и будет давать доступ или не будет +18
'''
def output(event):   # аргумент есть объект класса event там описано наступившее событие
    txt = entry1.get()   # значение возвращаемое методом get объекта entry, возвращает строку
    try:    # функция вызывается когда происходит нажатие на кнопку button1
        if int(txt) < 18:
            label1['text'] = 'вам еще рано сюда!'
        else:
            label1['text'] = 'добро пожаловать!'

    except ValueError:
        label1['text'] = 'введите корректный возраст'


root.title('сколько вам лет?')

entry1 = Entry(root, width=3, font=15)
button1 = Button(root, text='проверить')
label1 = Label(root, width=27, font=15)

entry1.grid(row=0, column=0)
button1.grid(row=0, column=1)
label1.grid(row=0, column=2)

button1.bind('<Button-1>', output)   # '<Button-1>' это клик ЛКМ. при клике вызываем функцию output
'''
# -----------------------------------------------------------------------------
# 6) основные события мыши
#    создадим 3 фрейма по горизонтали и будем окрашивать в красный ту часть какая кнопка на мышке нажата
'''
def left_click(event):
    frame1.configure(bg='red')
    frame2.configure(bg='white')
    frame3.configure(bg='white')

def middle_click(event):
    frame1.configure(bg='white')
    frame2.configure(bg='red')
    frame3.configure(bg='white')

def right_click(event):
    frame1.configure(bg='white')
    frame2.configure(bg='white')
    frame3.configure(bg='red')


root.configure(bg='black')   # метод позволяет конфигурировать методы во времы выполнения программы, сделали цвет черный

frame1 = Frame(root, width=250, heigh=250, bg='white')
frame2 = Frame(root, width=250, heigh=250, bg='white')
frame3 = Frame(root, width=250, heigh=250, bg='white')

frame1.grid(row=0, column=0)
frame2.grid(row=0, column=1, padx=1)  # бордюры по оси Х
frame3.grid(row=0, column=2)

# чтоб нажатия работали по всему окну bind пишем в root
root.bind('<Button-1>', left_click)   # <Button-1> - Клик ЛКМ, left_click - функция
root.bind('<Button-3>', middle_click)   # <Button-2> - Клик ролика
root.bind('<Button-2>', right_click)   # <Button-3> - Клик ПКМ
'''
# -----------------------------------------------------------------------------
# 7) события нажатия на клавиши клавиатуры, связываем простое нажатие на клавици с функцией
#    функция chr() принимает код символа, возвращает символ
'''
def print_char(event):
    label1.configure(text=event.char)  # возвращает символ клавиши, по которой нажали

def print_su(event):
    label1.configure(text='Shift Up')

def print_cd(event):
    label1.configure(text='Control Down')


label1 = Label(root, width=12, font=('Ubuntu', 100))
label1.pack()   # будем выводить клавиши на которые нажимаем на клавиатуре

for i in range(65, 123):
    root.bind(chr(i), print_char)

root.bind('<Shift-Up>', print_su)   # комбинация из двух кнопок
root.bind('<Control-Down>', print_cd)
'''
# -----------------------------------------------------------------------------
# 8) реализиция секундомера
#    функция tick это функция запуска таймера
#    в графических приложениях нельзя использовать обычные бесконечные циклы
#    циклический вызов функции через after и after_cancel
'''
from datetime import datetime

temp = 0   # количество секунд с момента старта секундомера
after_id = ''   # хранит идентификатор возвращаемый методом after

def tick():
    global temp, after_id   # глобальные переменные, все изменения видны и за пределами функциий
    after_id = root.after(1000, tick)   # tick вызывается рекурсивно, с периудом в 1 секунду
    f_temp = datetime.fromtimestamp(temp).strftime('%M:%S')
    watchface.configure(text=str(f_temp))
    temp += 1

def start_sw():  # будет запускать таймер, прятать кнопку старт, отображать кнопку стоп
    btn_start.grid_forget()  # убираем кнопку старт
    btn_stop.grid(row=1, columnspan=2, sticky='ew')  # размещает кнопку стоп в освободившемся месте
    tick()

def stop_sw():
    btn_stop.grid_forget()  # убираем кнопку стоп
    btn_continue.grid(row=1, column=0, sticky='ew')   # размещает кнопку продолжить в освободившемся месте
    btn_reset.grid(row=1, column=1, sticky='ew')    # размещает кнопку сбросить в освободившемся месте
    root.after_cancel(after_id)   # завершает цикл after при вызове функции tick

def continue_sw():
    btn_continue.grid_forget()   # убираем кнопку продолжить
    btn_reset.grid_forget()   # убираем кнопку ресет
    btn_stop.grid(row=1, columnspan=2, sticky='ew')  # размещает кнопку стоп в освободившемся месте
    tick()

def reset_sw():
    global temp  # делаем глобальной, чтоб сбросить счетчик секунд
    temp = 0
    watchface.configure(text='00:00')   # сбросим надпись в виджете
    btn_continue.grid_forget()  # убираем кнопку продолжить
    btn_reset.grid_forget()  # убираем кнопку ресет
    btn_start.grid(row=1, columnspan=2, sticky='ew')


root.title('Stopwatch')

watchface = Label(root, width=5, font=('Ubuntu', 100), text='00:00')
watchface.grid(row=0, columnspan=2)

btn_start = Button(root, text='Start', font=('Ubuntu', 30), command=start_sw)  # добавили функцию при нажатии
btn_stop = Button(root, text='Stop', font=('Ubuntu', 30), command=stop_sw)
btn_continue = Button(root, text='Continue', font=('Ubuntu', 30), command=continue_sw)
btn_reset = Button(root, text='Reset', font=('Ubuntu', 30), command=reset_sw)
# до запуска секундомера видна только кнопка старт
btn_start.grid(row=1, columnspan=2, sticky='ew')   # sticky - к какой границе приклеить виджет
'''

root.mainloop()
