# It is a simple notepad for simple work.  It is my first program with tkinter.


from tkinter import *
from tkinter.filedialog import *


def full_screen(event):
    root.attributes("-fullscreen", True)


def normailze(event):
    root.attributes("-fullscreen", False)
    root.minsize(800, 500)


root = Tk()
root.title("HippoText")
root.minsize(800, 500)

font_size = 15
font_type = "Courier New"
font_color = '#FFFFFF'
background_color = '#000000'
font_style = 'normal'

root.bind('<Alt_R>', full_screen)
root.bind('<Escape>', normailze)
text = Text(root, background=background_color, font=(font_type, font_size, font_style), fg=font_color, cursor="heart")
text.pack(expand=True, fill=BOTH)


def save():
    file = open(asksaveasfilename()+'.txt', 'w')
    file.write(text.get('1.0', END+'-1c'))
    file.close()


def my_open():
    file = open(askopenfilename(), 'r')
    text.delete(1.0, END + '-1c')
    for line in file:
        text.insert(END, line)
    file.close()


def new_file():
    text.delete(1.0, END + '-1c')


file_menu = Menu(font=("это хуйня", 10), tearoff=0)
file_menu.add_command(label="Новый файл", command=new_file)
file_menu.add_command(label="Открыть", command=my_open)
file_menu.add_command(label="Сохранить", command=save)


def inc_size():
    global font_size
    font_size += 1
    global text
    text.config(font=(font_type, font_size))


def dec_size():
    global font_size
    font_size -= 1
    global text
    text.config(font=(font_type, font_size))


def light():
    global font_color
    global background_color
    font_color = '#000000'
    background_color = '#FFFFFF'
    text.config(background=background_color, fg=font_color)


def dark():
    global font_color
    global background_color
    font_color = '#FFFFFF'
    background_color = '#000000'
    text.config(background=background_color, fg=font_color)


def red():
    global font_color
    global background_color
    font_color = '#CC0033"'
    background_color = '#FFFFFF'
    text.config(background=background_color, fg=font_color)


color_style_menu = Menu(font=("это хуйня", 10), tearoff=0)
color_style_menu.add_command(label="Светлая", command=light)
color_style_menu.add_command(label="Темная", command=dark)
color_style_menu.add_command(label="Кровавая", command=red)

view_menu = Menu(font=("это хуйня", 10), tearoff=0)
view_menu.add_command(label="Увеличить шрифт", command=inc_size)
view_menu.add_command(label="Уменьшить шрифт", command=dec_size)
view_menu.add_cascade(label="Виды раскраски", menu=color_style_menu)

main_menu = Menu()
main_menu.add_cascade(label="Файл", menu=file_menu)
main_menu.add_cascade(label="Вид", menu=view_menu)

root.config(menu=main_menu)
root.mainloop()
