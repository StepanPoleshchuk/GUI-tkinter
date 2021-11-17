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
# -----------------------------------------------------------------------------
# 9) ООП при создании приложений
#    аналог задания 5, в зависимости от возраста будет давать ответ
'''
class Question:

    def __init__(self, main):   # передаем главное окно, в котором будет располагаться объект нашего класса

        self.entry1 = Entry(main, width=3, font=15)
        self.button1 = Button(main, text='Проверить')
        self.label1 = Label(main, width=27, font=15)

        self.entry1.grid(row=0, column=0)
        self.button1.grid(row=0, column=1)
        self.label1.grid(row=0, column=2)

        self.button1.bind('<Button-1>', self.answer)

    def answer(self, event):

        txt = self.entry1.get()

        try:
            if int(txt) < 18:
                self.label1['text'] = 'вам еще рано сюда'
            else:
                self.label1['text'] = 'доступ есть'
        except ValueError:
            self.label1['text'] = 'введите корректный возраст!'


root.title('сколько вам лет?')
q = Question(root)
'''
# -----------------------------------------------------------------------------
# 10) Выпадающий список(дропдаун), каждый подпунк это действие
'''
def new_win():
    win = Toplevel(root)  # Toplevel окно верхнего уровня, для создания многооконных программ/диалоговых окон
    label1 = Label(win, text='Текст в окне верхнего уровня', font=20)
    label1.pack()

def exit_app():
    root.destroy()  # уничтожаем главное окно и всех его потомков

main_menu = Menu(root)
root.configure(menu=main_menu)

first_item = Menu(main_menu, tearoff=0)  # располагаем первый в пункт в main_menu
main_menu.add_cascade(label="File", menu=first_item)  # выпадающий список
first_item.add_command(label="New", command=new_win)  # пункт, открывает новое окно
first_item.add_command(label="Exit", command=exit_app)  # пункт, закрывает приложение

second_item = Menu(main_menu, tearoff=0)  # располагаем второй в пункт в main_menu
main_menu.add_cascade(label="Edit", menu=second_item)  # выпадающий список
second_item.add_command(label="Item1")  # пункт
second_item.add_command(label="Item2")
second_item.add_command(label="Item3")
second_item.add_separator()
second_item.add_command(label="Item4")
'''
# -----------------------------------------------------------------------------
# 11) Панель инструментов и статусбар (используем код из предшествующего урока)
'''
def new_win():
    win = Toplevel(root)  # Toplevel окно верхнего уровня, для создания многооконных программ/диалоговых окон
    label1 = Label(win, text='Текст в окне верхнего уровня', font=20)
    label1.pack()

def exit_app():
    root.destroy()  # уничтожаем главное окно и всех его потомков

main_menu = Menu(root)
root.configure(menu=main_menu)

first_item = Menu(main_menu, tearoff=0)  # располагаем первый в пункт в main_menu
main_menu.add_cascade(label="File", menu=first_item)  # выпадающий список
first_item.add_command(label="New", command=new_win)  # пункт, открывает новое окно
first_item.add_command(label="Exit", command=exit_app)  # пункт, закрывает приложение

second_item = Menu(main_menu, tearoff=0)  # располагаем второй в пункт в main_menu
main_menu.add_cascade(label="Edit", menu=second_item)  # выпадающий список
second_item.add_command(label="Item1")  # пункт
second_item.add_command(label="Item2")
second_item.add_command(label="Item3")
second_item.add_separator()
second_item.add_command(label="Item4")

tool_bar = Frame(root, bg='#A1A1A1')
tool_bar.pack(side=TOP, fill=X)   # разместим растягивающийся по горизонтали фрейм сверху + пихнем туда 3 кнопки

btn1 = Button(tool_bar, text='Cut')
btn1.grid(row=0, column=0, padx=2, pady=2)
btn2 = Button(tool_bar, text='Copy')
btn2.grid(row=0, column=1, padx=2, pady=2)
btn3 = Button(tool_bar, text='Paste')
btn3.grid(row=0, column=2, padx=2, pady=2)

status_bar = Label(root, relief=SUNKEN, anchor=W, text='mission complete.')
# relief это свойство определяющее тип рамки элемента, anchor привязка содержимого к краю(в нашем случае к левому)
status_bar.pack(side=BOTTOM, fill=X)
'''
# -----------------------------------------------------------------------------
# 12) Диалоговые окна. Для информирования и взаимодействия с пользователем (messagebox)(showinfo,showwarning,showerror)
#     Информационные окна для выдачи информации, предупреждения или выдачи ошибки
#     Создадим три кнопки при нажатии на которые будут появляться соответствующие окна
'''
btn1 = Button(root, text='Info', font=('Ubuntu', 20), command=lambda: tkinter.messagebox.showinfo('ShowInfo', 'Информация'))
btn1.grid(row=0, column=0, sticky='ew')
# не пишем функцию отдельно, пользуемся лямбдой
# showinfo это информационное окно, первый параметр-заголовок окна, второй-текст в самом окне

btn2 = Button(root, text='Warning', font=('Ubuntu', 20), command=lambda: tkinter.messagebox.showwarning('ShowWarning', 'Предупреждение'))
btn2.grid(row=1, column=0, sticky='ew')

btn3 = Button(root, text='Error', font=('Ubuntu', 20), command=lambda: tkinter.messagebox.showerror('ShowError', 'Ошибка'))
btn3.grid(row=2, column=0, sticky='ew')
'''
# -----------------------------------------------------------------------------
# 13) Диалоговые окна. Вопросы, 4 вида вопросов (messagebox)(AskQuestion,AskOkCancel,AskYesNo,AskRertyCancel)
'''
def ask_question(event):
    answer = tkinter.messagebox.askquestion('AskQuestion', 'Вопрос первый?')    # диалоговое окно, параметр 1 - заголовок, 2 - тело окна
    label1.configure(text=answer)

def ask_ok(event):
    answer = tkinter.messagebox.askokcancel('AskOkCancel', 'Вопрос второй?')
    label2.configure(text=answer)

def ask_yn(event):
    answer = tkinter.messagebox.askyesno('AskYesNo', 'Вопрос третий?')
    label3.configure(text=answer)

def ask_rc(event):
    answer = tkinter.messagebox.askretrycancel('AskRertyCancel', 'Вопрос третий?')
    label4.configure(text=answer)


btn1 = Button(root, text='askquestion', font=('Ubuntu', 20), width=12)
btn1.grid(row=0, column=0, sticky='ew')
label1 = Label(root, font=('Ubuntu', 20), width=12)
label1.grid(row=0, column=1)
btn1.bind('<Button-1>', ask_question)

btn2 = Button(root, text='askokcancel', font=('Ubuntu', 20), width=12)
btn2.grid(row=1, column=0, sticky='ew')
label2 = Label(root, font=('Ubuntu', 20), width=12)
label2.grid(row=1, column=1)
btn2.bind('<Button-1>', ask_ok)

btn3 = Button(root, text='askyesno', font=('Ubuntu', 20), width=12)
btn3.grid(row=2, column=0, sticky='ew')
label3 = Label(root, font=('Ubuntu', 20), width=12)
label3.grid(row=2, column=1)
btn3.bind('<Button-1>', ask_yn)

btn4 = Button(root, text='asretrycancel', font=('Ubuntu', 20), width=12)
btn4.grid(row=3, column=0, sticky='ew')
label4 = Label(root, font=('Ubuntu', 20), width=12)
label4.grid(row=3, column=1)
btn4.bind('<Button-1>', ask_rc)
'''
# -----------------------------------------------------------------------------
# 14) Диалоговые окна. Редактор текста (filedialog)(askopenfilename,asksaveasfilename)
#     Окно в котором будет текст и меню с 3 пунктами: открыть файл, сохранить файл и закрыть приложение
'''
def open_file():   # Вызывает диалоговое окно, посредством которого мы сможем открывать файлы
    of = tkinter.filedialog.askopenfilename()
    file = open(of, 'r')   # 1 параметр - абсолютный путь переменной, 2 - тип открытия(в нашем случае для чтения)
    txt.insert(END, file.read())  # вставить в конец виджета txt то что у нас попадет в переменную of
    file.close()

def save_file():   # Позволяет сохранять все что мы внесем в файл
    sf = tkinter.filedialog.asksaveasfilename()   # инструкцией вызываем диалоговое окно
    final_text = txt.get(1.0, END)  # получить содержимое строк с 1 строки(начало с 1) с 0 столбца(начало с 0)
    file = open(sf, 'w')   # открыть файл на запись, а если он не существует-создать
    file.write(final_text)
    file.close()

def exit_app():
    root.quit()


main_menu = Menu(root)
root.configure(menu=main_menu)

first_item = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='File', menu=first_item)   # создали пункт

first_item.add_command(label='Open', command=open_file)   # подпункт с функцией открытия
first_item.add_command(label='Save', command=save_file)
first_item.add_command(label='Exit', command=exit_app)

txt = Text(root, width=40, height=15, font=12)  # Виджет текст в который мы будем помещать содержимое открываемого файла
txt.pack(expand=YES, fill=BOTH)  # Виджет будет растягиваться по всей высоте и ширине родительского окна
'''
# -----------------------------------------------------------------------------
# 15) Canvas и геометрические примитивы. Координаты начинаются сверху слева
'''
c1 = Canvas(root, width=500, height=500, cursor='pencil', bg='white')
c1.pack()

c1.create_line(250, 0, 250, 500, width=3, fill='red', arrow=LAST)  # координаты (нач,кон), ширина, цвет, arrow - стрелка
c1.create_line(0, 250, 500, 250, width=3, fill='blue', arrow=BOTH)

c1.create_rectangle(10, 10, 240, 240, fill='green', outline='red')  # координаты пр. (верхнего левого,нижнего правого)
c1.create_polygon(260, 10, 490, 10, 400, 125, 490, 240, 260, 240, 350, 125, fill='orange', smooth=1)
# многоугольник, координаты точек по часовой стрелке через запятую smooth - сглаживание
c1.create_oval(10, 260, 240, 340, fill='yellow', outline='red', width=3)  # координаты пр. описывающего овал
# производные от эллипса(сектор, сегмент, дуга)
c1.create_arc(10, 350, 90, 430, start=0, extent=270, fill='#0000cc')   # сектор
c1.create_arc(160, 350, 240, 430, start=0, extent=270, fill='#cc0099', style='chord')   # сегмент
c1.create_arc(80, 410, 160, 490, start=0, extent=270, style='arc', outline='#ff6600', width=3)   # дуга

c1.create_text(275, 330, text='Tkinter- \nэто программы\n с оконным интерфейсом', font=('Ubuntu', 17), anchor='w',
               justify='center', fill='orange')   # координаты точки отностиельно которой текст(по умолчанию посередине)
'''
# -----------------------------------------------------------------------------
# 16) Работа с Canvas (статические изменения фигур)
#     Обращаемся к статическим фигурам при помощи идентификатора объекта и атрибута tag
'''
def create_outline(event):   # возникает контур
    c1.itemconfigure(oval1, outline='blue', width=3)

def change_fill(event):   # изменяется фигура
    c1.itemconfigure(oval2, fill='orange')
    c1.coords(oval2, 250, 10, 390, 90)

def move_ovals(event):   # меняем овалы, по тегу (tag='ovals')
    c1.move('ovals', 0, 260)

def clear_canvas(event):   # очищаем все
    c1.delete('all')


c1 = Canvas(root, width=400, height = 400, bg='white')
c1.pack()

oval1 = c1.create_oval(10, 10, 90, 90, width=0, fill='red', tag='ovals')   # овал с тегом
oval2 = c1.create_oval(310, 10, 390, 90, width=0, fill='blue', tag='ovals')
triangle = c1.create_polygon(200, 200, 10, 390, 390, 390, fill='green')   # треугольник без тега
# регистрируем действия при нажатии
c1.tag_bind(oval1, '<Button-1>', create_outline)   # 1 - идентификатор объекта, 2 - тип события, 3 - функция обработчик
c1.tag_bind(oval2, '<Button-1>', change_fill)   # при нажатии будет выполняться функция
c1.tag_bind(triangle, '<Button-1>', move_ovals)
root.bind('<Button-2>', clear_canvas)   # при нажатии на ПКМ будет очищаться холст
'''
# -----------------------------------------------------------------------------
# 17) Анимированная отрисовка
#     Тригонометрические функции и их отрисовка
x = 0


def print_dot():

    global x

    y1 = sin(x)
    y2 = cos(x)

    cvs.create_oval(25 * x + 10, 25 * y1 + 100, 25 * x + 10, 25 * y1 + 100, width=1, outline='red')
    cvs.create_oval(25 * x + 10, 25 * y2 + 100, 25 * x + 10, 25 * y2 + 100, width=1, outline='blue')

    x += 0.05
    root.after(5, print_dot)
    

cvs = Canvas(root, width=600, height=200, bg='#fff')
cvs.pack()

cvs.create_line(10, 0, 10, 200, width=2, arrow='both', fill='grey')   # сделаем координаты по осям
cvs.create_line(10, 100, 600, 100, width=2, arrow='last', fill='grey')

print_dot()
root.mainloop()
