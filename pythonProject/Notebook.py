from __future__ import print_function
import math
import string
from IPython.display import clear_output
from random import shuffle
from colorama import Fore, Style
from builtins import input
import sys
import random
import time
from termcolor import colored, COLORS
import unittest
import os
from pythonProject.Classes import Employee
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import cap
import sqlite3
import re


def oop():
    class Employee:

        def __init__(self, first, last, pay):
            self.first = first
            self.last = last
            self.pay = pay

        def __repr__(self):
            return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

        def __str__(self):
            return '{} - {}'.format(self.fullname, self.email)

        def __add__(self, other):
            return self.pay + other.pay

        def __len__(self):
            return len(self.fullname)

        @property
        def email(self):
            return '{}.{}@email.com'.format(self.first, self.last)

        @property
        def fullname(self):
            return '{} {}'.format(self.first, self.last)

        @fullname.setter
        def fullname(self, name):
            first, last = name.split(' ')
            self.first = first
            self.last = last

        @fullname.deleter
        def fullname(self):
            print('Delete Name!')
            self.first = None
            self.last = None

    emp_1 = Employee('John', 'Smith', 50000)
    emp_2 = Employee('Keanu', 'Reeves', 60000)
    print(emp_1 + emp_2)
    # __add__ dunder creates addition method (+) for emp_1
    # __len__ dunder creates len() method for emp_1

    emp_1.fullname = "Corey Schafer"
    # by adding a {method_name}.setter dunder after property: method => attribute that can be reassigned or "set"
    print(emp_1.first)
    print(emp_1.email)
    # property change email method into attribute
    print(emp_1.fullname)

    del emp_1.fullname
    # @{method_name}.deleter: allows attribute to be deleted


def regular_expression():
    text_to_search = '''
    abcdefghijklmnopqurtuvwxyz
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    1234567890
    Ha HaHa
    MetaCharacters (Need to be escaped):
    . ^ $ * + ? { } [ ] \ | ( )
    coreyms.com
    321-555-4321
    123.555.1234
    123*555*1234
    800-555-1234
    900-555-1234
    Mr. Schafer
    Mr Smith
    Ms Davis
    Mrs. Robinson
    Mr. T
    '''
    sentence = 'Start a sentence and then bring it to an end'
    pattern = re.compile(r"\d\d\d.\d\d\d.\d\d\d\d")
    matches = pattern.finditer(text_to_search)
    # literal search
    for match in matches:
        print(match)

    with open("data.txt", "r") as f:
        contents = f.read()
        pattern = re.compile(r"(Mr|Ms|Mrs)\.?\s[A-Z]\w*")  # anything except inside brackets
        # []: a single character inside bracket
        # [1-5]: any single character from 1 to 5
        # [a-zA-Z]: from a to z, from A to Z
        # cach 1: pattern = re.compile(r"\d\d\d.\d\d\d.\d\d\d\d")
        # cach 2: pattern = re.compile(r"\d{3}.\d{3}.\d{4}
        # {n}: n times, {n,m}: n to m times
        # x*: 0 or more occurrences of x
        # x+: 1 or more occurrences of x
        # x?: 0 or 1 occurrence of x
        # (): multiple patterns

        matches = pattern.finditer(text_to_search)
        for match in matches:
            print(match)

    emails = '''
    CoreyMSchafer@gmail.com
    corey.schafer@university.edu
    corey-321-schafer@my-work.net
    '''
    # pattern = re.compile(r"[a-zA-Z0-9_+.-]+@[a-zA-Z0-9_+.-]+\.(com|edu|net)")

    urls = '''
    https://www.google.com
    http://coreyms.com
    https://youtube.com
    https://www.nasa.gov
    '''
    pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")
    matches = pattern.finditer(urls)
    # findall: return only group if there are groups or else return fully
    for match in matches:
        print(match.group(1))
        # 0 print all, 1 first group () in this case www.

    subbed_urls = pattern.sub(r'\2\3', urls)
    # substitute matched results in urls with group 2 and 3 of said url.
    print(subbed_urls)

    pattern = re.compile(r'Start', re.IGNORECASE)
    # re.IGNORECASE = ignore upper and lower case

    matches = pattern.match(sentence)
    # doesn't return an iterable, only 1st match
    print(matches)

    s = 'one two one two one'
    print(s.replace(' ', '-'))
    # one-two-one-two-one
    print(s.replace('one', 'XXX').replace('two', 'YYY'))
    # XXX YYY XXX YYY XXX

    s = 'aaa@xxx.com bbb@yyy.com ccc@zzz.com'
    print(re.sub('[a-z]*@', 'ABC@', s))
    # ABC@xxx.com ABC@yyy.com ABC@zzz.com
    print(re.sub('[a-z]*@', 'ABC@', s, 2))
    # ABC@xxx.com ABC@yyy.com ccc@zzz.com
    print(re.sub('[xyz]', '1', s))
    # aaa@111.com bbb@111.com ccc@111.com
    print(re.sub('([a-z]*)@', '\\1-123@', s))
    # aaa-123@xxx.com bbb-123@yyy.com ccc-123@zzz.com
    print(re.sub('([a-z]*)@', r'\1-123@', s))
    # aaa-123@xxx.com bbb-123@yyy.com ccc-123@zzz.com
    # if raw then \1, else \\1: refer to first group(), \\2 refers to 2nd group()


def sql3():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    # method such as CREATE, INSERT, SELECT are capitalized for readability
    # even if uncapitalized they still work
    # execute only
    c.execute("""CREATE TABLE employees (
                first text,
                last text,
                pay integer
                )""")

    ''' Long way
    c.execute("INSERT INTO employees VALUES ('Corey', 'Schafer', 5000)")
    c.execute("INSERT INTO employees VALUES ('Nguyen', 'Le', 1000)")
    c.execute("INSERT INTO employees VALUES ('kaboom', 'hi', 10000)")
    '''

    'Short way'
    name_list = [('Corey', 'Schafer', 5000), ('Nguyen', 'Le', 1000), ('kaboom', 'hi', 10000)]
    c.executemany("INSERT INTO employees VALUES(?,?,?)", name_list)

    # In order to print out a value, you need to select it first
    t = ('Nguyen',)
    # use tuple since string operations are prone to errors
    c.execute("SELECT * FROM employees where first=?", t)
    # ? is where you want to place, where to specify what value to take
    print(c.fetchone())

    c.execute("SELECT * FROM employees")
    print(c.fetchall())

    conn.commit()

    conn.close()


def basic():
    """https://learnxinyminutes.com/docs/python/"""
    """Pointing"""
    x = 10
    y = x
    x += 5  # add 5 to x's value, and assign it to x
    print("x =", x)
    print("y =", y)
    """y points to x which points to 10 => y value is 10
    x+= 5 => x points to new value 10+5 or 15.
    y still points to 10
    """


'''Set: Union, intersection, difference, issubset'''


def set_training():
    my_set = {False, 4.5, 3, 6, 'cat'}
    your_set = {99, 3, 100}

    print(my_set.union(your_set))
    print(my_set | your_set)
    # {False, 4.5, 3, 100, 6, 'cat', 99}

    print(my_set.intersection(your_set))
    print(my_set & your_set)
    # {3}

    print(my_set.difference(your_set))
    print(my_set - your_set)
    # {False, 4.5, 6, 'cat'}

    print({3, 100}.issubset(your_set))
    print({3, 100} <= your_set)
    # True

    print(my_set.add("house"))
    # {False, 4.5, 3, 6, 'house', 'cat'}

    print(my_set.remove(4.5))
    # {False, 3, 6, 'house', 'cat'}


'''Directory'''


def directory_testing():
    """ Directory
        - Khi có nhiều file để xử lý trong chương trình Python, thì sắp xếp vào các thư mục để dễ quản lý
        - Một thư mục (directory/folder) là một tập hợp các file và thư mục con
        - Python cung cấp module os chứa nhiều phương thức để làm việc với directory (và cả file khá tốt)
    """

    """ Cách lấy đường dẫn thư mục hiện tại, dùng getcwd() """

    import os
    print(os.getcwd())

    """ Cách di chuyển sang thư mục khác dùng chdir() """
    os.chdir('/home/hoanpp/Desktop/')
    print(os.getcwd())

    """ Cách lấy danh sách thu mục con và file dùng listdir() """

    os.chdir('/home/hoanpp/Desktop/')
    print(os.listdir())  # Lấy từ thư mục đang làm việc
    print(os.listdir('/home/hoanpp/Desktop/PyCore-Course'))  # Lấy từ thư mục chỉ định

    """ Tạo ra thư mục mới bằng: mkdir() """

    os.mkdir('test_dir')
    print(os.listdir())

    """ Đổi tên thư mục hoặc file, dùng rename() """
    print(os.listdir())
    os.rename('test_dir', 'new_test_dir')
    print(os.listdir())

    """ Xóa bỏ thư mục hoặc file, dùng rmdir() - cái này chỉ dùng xóa đi được thư mục rỗng,
        còn dùng rmtree() trong module shutil để remove toàn bộ thư mục,
        còn file thì dùng remove()"""
    print(os.listdir())
    os.remove('old.txt')
    print(os.listdir())
    os.rmdir('new_one')
    print(os.listdir())


'''Reading, writing ans such'''


def file_handling():
    # ``r''   Open text file for reading.  The stream is positioned at the
    #         BEGINNING of the file.

    # ``r+''  Open for reading and writing.  The stream is positioned at the
    #         BEGINNING of the file.

    # ``w''   Open for writing. The file is created if it does not exist, otherwise it is truncated.
    #         The stream is positioned at the BEGINNING of the file.

    # ``w+''  Open for reading and writing.  The file is created if it does not
    #         exist, otherwise it is truncated.  The stream is positioned at
    #         the BEGINNING of the file.

    # ``a''   Open for writing.  The file is created if it does not exist.  The
    #         stream is positioned at the END of the file.

    # ``a+''  Open for reading and writing.  The file is created if it does not
    #         exist.  The stream is positioned at the END of the file.

    print(os.getcwd())

    with open("file_test.txt", 'w', encoding='utf-8') as f:
        f.write("my first file\n")
        f.write("This file\n\n")
        f.write("contains three lines\n")

    f_read = open('file_test.txt', 'r', encoding='utf-8')
    print(f_read.read(4))  # Đọc 4 ký tự đầu
    print(f_read.read(10))  # Đọc 4 ký tự tiếp theo 4 ký tự đầu
    print(f_read.read())  # Đọc tiếp đến khi nào hết dữ liệu
    print(f_read.read())  # Đọc tiếp => hết file rồi nên trả về chuỗi rỗng
    print(f_read.tell())  # Lấy vị trí hiện tại của con trỏ đọc file
    f_read.seek(0)  # Cho con trỏ về lại đầu file
    print(f_read.read())

    for line in f_read:
        print(line, end='')
    # Chú ý, mặc định mỗi dòng đều đã có xuống dòng, để đỡ bị dòng trắng thì ta dùng end='' cho câu lệnh print
    f_read.seek(0)  # Cho con trỏ về lại đầu file
    print(f_read.readline())
    print(f_read.readline())
    print(f_read.readlines())  # Trả lại toàn bộ các dòng trong file dưới dạng list


'''Exception handling: Value Error'''


def ex_han():
    random_list = ['a', 0, 0.5]

    for item in random_list:
        try:
            print("Phần tử:", item)
            r = 1 / int(item)
            print("Nghịch đảo của ", item, "is", r)
        except:
            print("Oops!", sys.exc_info()[0], "Toang Rồi!.")  # import module sys to get the type of exception
            # 0 for class, 1 for value, 2 for value address
            print("=> next \n")
    try:
        a = int(input("Nhập một số nguyên dương: "))
        if a <= 0:
            raise ValueError("Số vừa nhập không phải số nguyên dương!")
    except ValueError as ve:
        print(ve)
    finally:
        print("Definitely happen")
    # The int() function takes a number or a string. It can convert the string "21" to the integer 21,
    # but it can't convert "dog" to a number => it's getting the right type, but it's not a value that it can convert.
    # This is when we get the ValueError. It's of the right type, but the value is such that it still can't be done.
    # If input is neither a string nor a number, it would have generated a TypeError as it is of the wrong type.


'Some color exercise'


def color_mess():
    a = "LET's go"
    print(Fore.RED + a)
    print(a)
    print(f"{Fore.BLUE}Hello World{Style.RESET_ALL}")
    print(a)


'''Database: sqlite3'''


def dtb():
    conn = sqlite3.connect(':memory:')

    c = conn.cursor()

    c.execute("""CREATE TABLE employees (
                first text,
                last text,
                pay integer
                )""")

    def insert_emp(emp):
        with conn:
            # c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
            #           {'first': emp.first, 'last': emp.last, 'pay': emp.pay})
            c.execute("INSERT INTO employees VALUES (?,?,?)", (emp.first, emp.last, emp.pay))

    def get_emps_by_name(lastname):
        c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
        return c.fetchall()

    def update_pay(emp, pay):
        with conn:
            c.execute("""UPDATE employees SET pay = :pay
                        WHERE first = :first AND last = :last""",
                      {'first': emp.first, 'last': emp.last, 'pay': pay})

    def remove_emp(emp):
        with conn:
            c.execute("DELETE from employees WHERE first = :first AND last = :last",
                      {'first': emp.first, 'last': emp.last})

    emp_1 = Employee('John', 'Doe', 80000)
    emp_2 = Employee('Jane', 'Doe', 90000)

    insert_emp(emp_1)
    insert_emp(emp_2)

    emps = get_emps_by_name('Doe')
    print(emps)

    update_pay(emp_2, 95000)
    remove_emp(emp_1)

    emps = get_emps_by_name('Doe')
    print(emps)

    conn.close()


def dtb2():
    '''Creating a window'''
    root = Tk()
    root.title("boom")
    root.geometry('700x700')

    frame = LabelFrame(root, padx=5, pady=2)
    frame.grid(padx=10, pady=5, columnspan=4, column=0, row=0, sticky="nw")

    '''Calculator making'''

    def click(number):
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))

    def clear():
        e.delete(0, END)
        global result
        result = 0

    def add():
        num = e.get()
        e.delete(0, END)
        e.insert(0, "+")
        global result
        result += int(num)

    def equal():
        entry = e.get()
        global result
        if "+" in entry:
            num = entry[entry.rfind('+') + 1:]
            result += int(num)
            label = Label(frame, text=result)
            label.grid()
        else:
            label = Label(frame, text=result)
            label.grid()

    e = Entry(frame, width=25, borderwidth=5)
    e.grid(row=0, column=0, columnspan=3, pady=10, sticky="nsew")
    e.insert(0, "Enter here: ")  # 0 specifies index to insert text

    button_1 = Button(frame, text="1", width=6, borderwidth=3, command=lambda: click(1)) \
        .grid(row=1, column=0, padx=1, pady=1, sticky="nsew")
    button_2 = Button(frame, text="2", width=6, borderwidth=3, command=lambda: click(2)) \
        .grid(row=1, column=1, padx=1, pady=1, sticky="nsew")
    button_3 = Button(frame, text="3", width=6, borderwidth=3, command=lambda: click(3)) \
        .grid(row=1, column=2, padx=1, pady=1, sticky="nsew")
    button_4 = Button(frame, text="4", width=6, borderwidth=3, command=lambda: click(4)) \
        .grid(row=2, column=0, padx=1, pady=1, sticky="nsew")
    button_5 = Button(frame, text="5", width=6, borderwidth=3, command=lambda: click(5)) \
        .grid(row=2, column=1, padx=1, pady=1, sticky="nsew")
    button_6 = Button(frame, text="6", width=6, borderwidth=3, command=lambda: click(6)) \
        .grid(row=2, column=2, padx=1, pady=1, sticky="nsew")
    button_7 = Button(frame, text="7", width=6, borderwidth=3, command=lambda: click(7)) \
        .grid(row=3, column=0, padx=1, pady=1, sticky="nsew")
    button_8 = Button(frame, text="8", width=6, borderwidth=3, command=lambda: click(8)) \
        .grid(row=3, column=1, padx=1, pady=1, sticky="nsew")
    button_9 = Button(frame, text="9", width=6, borderwidth=3, command=lambda: click(9)) \
        .grid(row=3, column=2, padx=1, pady=1, sticky="nsew")
    button_0 = Button(frame, text="0", borderwidth=3, command=lambda: click(0)) \
        .grid(row=4, column=0, sticky="nsew")

    button_add = Button(frame, text="+", borderwidth=3, command=add) \
        .grid(row=4, column=1, sticky="nsew")
    button_equal = Button(frame, text="=", borderwidth=3, command=equal) \
        .grid(row=4, column=2, sticky="nsew")
    button_clear = Button(frame, text="Clear", borderwidth=3, command=clear) \
        .grid(row=5, column=0, sticky="nsew", columnspan=3)

    '''Working with images'''

    img1 = ImageTk.PhotoImage(Image.open('C:\\Users\\Asus\\Pictures\\ghibili.jpg')
                              .resize((160, 200), Image.ANTIALIAS))
    img2 = ImageTk.PhotoImage(Image.open('C:\\Users\\Asus\\Pictures\\dragon.jpg')
                              .resize((200, 200), Image.ANTIALIAS))
    img3 = ImageTk.PhotoImage(Image.open('C:\\Users\\Asus\\Pictures\\dragon art exclusive.jpg')
                              .resize((200, 200), Image.ANTIALIAS))
    img4 = ImageTk.PhotoImage(Image.open('C:\\Users\\Asus\\Pictures\\202007056097511217170126584-01.jpeg')
                              .resize((160, 200), Image.ANTIALIAS))

    image_list = [img1, img2, img3, img4]
    n = 0
    label = Label(frame, image=image_list[n])
    label.grid(columnspan=3)
    status = Label(frame, text=f'Image {n + 1} of {len(image_list)}', relief=SUNKEN, bd=1)
    status.grid(row=7, column=1, columnspan=1, sticky="nsew")

    '''Going through image files'''

    def forward():
        global n
        global label
        global button_forward
        global status
        label.grid_forget()
        n += 1
        if n == len(image_list) - 1:
            button_forward = Button(frame, width=6, borderwidth=3, text=">>", command=forward, state=DISABLED)
            button_forward.grid(row=7, column=2, sticky="e", columnspan=2)
        label = Label(frame, image=image_list[n])
        label.grid(columnspan=3, row=6)
        status = Label(frame, text=f'Image {n + 1} of {len(image_list)}', relief=SUNKEN, bd=1)
        status.grid(row=7, column=1, columnspan=1, sticky="nsew")

    def back():
        global n
        global label
        global button_back
        global status
        label.grid_forget()
        n -= 1
        if n == 0:
            button_back = Button(root, width=6, borderwidth=3, text="<<", command=back, state=DISABLED)
            button_back.grid(row=7, column=0, sticky='w', columnspan=2)
        label = Label(frame, image=image_list[n])
        label.grid(columnspan=3, row=6)
        status = Label(frame, text=f'Image {n + 1} of {len(image_list)}', relief=SUNKEN, bd=1)
        status.grid(row=7, column=1, columnspan=1, sticky="nsew")

    button_back = Button(frame, width=6, borderwidth=3, text="<<", command=back)
    button_back.grid(row=7, column=0, sticky='w', columnspan=2)
    button_forward = Button(frame, width=6, borderwidth=3, text=">>", command=forward)
    button_forward.grid(row=7, column=2, sticky="e", columnspan=2)

    ''' Exit window'''
    q = Button(frame, text="Exit", command=frame.quit, borderwidth=3)
    q.grid(row=8, columnspan=5, sticky='nsew')

    '''Creating a frame'''
    frame2 = LabelFrame(root, padx=5, pady=2)
    frame2.grid(padx=10, pady=5, columnspan=4, column=4, row=0, sticky="nw")
    label = Label(frame2, text="hi")
    label.grid()

    # r = IntVar()
    # r.set(2)

    '''Radio buttons'''
    label2 = Label(frame2, text='')

    def clicked(value):
        global label2
        label2.grid_forget()
        label2 = Label(frame2, text=value)
        label2.grid()

    # rd = Radiobutton(frame2, text="Option1", variable=r, value=1, command=lambda: clicked(r.get()))
    # rd.grid()
    # rd2 = Radiobutton(frame2, text="Option2", variable=r, value=2, command=lambda: clicked(r.get()))
    # rd2.grid()
    MODES = [
        ("hi", "HI"),
        ("boom", "BOOM"),
        ("kaboom", "KABOOM"),
        ("chiu", "CHIU")
    ]
    explosion = StringVar()
    explosion.set("Explosion")

    for text, mode in MODES:
        rd = Radiobutton(frame2, text=text, variable=explosion, value=mode, command=lambda: clicked(explosion.get()))
        rd.grid(sticky=W)

    label3 = Label(frame2, text="")

    '''Popup'''

    def popup():
        global label3
        response = messagebox.askyesnocancel('This is what showinfo does', "BOom")
        label3.grid_forget()
        if response == 1:
            label3 = Label(frame2, text="YOu clicked Yes")
            label3.grid()
        elif response == 0:
            label3 = Label(frame2, text="You clicked No")
            label3.grid()
        else:
            label3 = Label(frame2, text="You clicked Cancel")
            label3.grid()

    mb = Button(frame2, text="popup", command=popup).grid()

    '''Open new window'''

    def open_window():
        top = Toplevel()
        top.title("Second window")
        top.geometry("150x250")
        label4 = Label(top, image=img1)
        label4.grid()
        button_delete_window = Button(top, text="close", command=top.destroy)
        button_delete_window.grid()

    button_open_window = Button(frame2, text="Open window", command=open_window)
    button_open_window.grid()

    '''Open files to choose images'''

    def open_image():
        global image_root_filename
        root.filename = filedialog.askopenfilename(initialdir='C:\\Users\\Asus\\Pictures', title="Select a file",
                                                   filetypes=[("image files", "*.jpeg"), ("something", '*.jpg')])
        label4 = Label(frame2, text=root.filename)
        label4.grid()
        image_root_filename = ImageTk.PhotoImage(Image.open(root.filename).resize((160, 200), Image.ANTIALIAS))
        label5 = Label(frame2, image=image_root_filename)
        label5.grid()

    button_open_image = Button(frame2, text="Open image from Image", command=open_image)
    button_open_image.grid()

    '''Slide bar'''

    def slide(width, length):
        # when execute line: vertical = Scale(frame2, from_=0, to=1000, command=function(no parameter)
        # if function has 0 parameters, the below error will occur
        # TypeError: slide() takes 0 positional arguments but _ was given
        # fix by adding variable def function(var): to make it work
        root.geometry(f'{str(width)}x{str(length)}')

    vertical = Scale(frame2, from_=0, to=1000)
    vertical.grid(sticky="nw")
    horizontal = Scale(frame2, from_=0, to=1000, orient=HORIZONTAL)
    horizontal.grid()

    button_weight = Button(frame2, text="Click to measure MBI", command=lambda: slide(horizontal.get(), vertical.get()))
    button_weight.grid()

    '''Check button'''

    def check():
        label4 = Label(frame2, text=var.get())
        label4.grid()

    var = StringVar()
    c = Checkbutton(frame2, text="Click here", variable=var, onvalue="Hi", offvalue="bye")
    c.deselect()
    c.grid()
    # when no onvalue or offvalue passed in: ticked == True  == 1, unticked == False == 0

    button_check = Button(frame2, text='New value', command=check)
    button_check.grid()

    '''Option Menu'''

    def show(dy):
        label5 = Label(frame2, text=f'Hi today is {dy}')
        label5.grid()

    days = ['monday', "tuesday", 'wednesday', 'friday', 'saturday', 'sunday']
    day = StringVar()
    day.set("Day of the week")
    drop = OptionMenu(frame2, day, *days)
    drop.grid()

    button_say_hi = Button(frame2, text="What day today?", command=lambda: show(day.get()))
    button_say_hi.grid()

    '''Working with databases'''

    def submit():
        with conn:
            c.execute('INSERT INTO residences VALUES (?,?,?)',
                      (f_name_entry.get(), l_name_entry.get(), address_entry.get()))
        f_name_entry.delete(0, END)
        l_name_entry.delete(0, END)
        address_entry.delete(0, END)

    def show_residence():
        c.execute("SELECT *,oid FROM residences ORDER BY f_name DESC")
        lst = c.fetchall()
        for a in range(len(lst)):
            label_residence = Label(frame3, text=f'Mr. {lst[a][0]} {lst[a][1]} '
                                                 f'lives in {lst[a][2]}. '
                                                 f'His oid is {lst[a][3]}')
            label_residence.grid(sticky='w', columnspan=3, row=8 + a)

    def delete_id():
        with conn:
            c.execute("DELETE from residences WHERE oid=(?)", (entry_choose_id.get()))

    def confirm_update_id():
        global update_f_name_entry
        global update_l_name_entry
        global update_address_entry
        with conn:
            c.execute("""UPDATE residences SET 
                f_name = (?),
                l_name = (?),
                address = (?)
                WHERE oid = (?)       
            """, (update_f_name_entry.get(), update_l_name_entry.get(),
                  update_address_entry.get(), entry_choose_id.get()))
            update_window.destroy()

    def update_id():
        global update_f_name_entry
        global update_l_name_entry
        global update_address_entry
        global update_window
        update_window = Toplevel()
        update_window.title("Update window")
        update_window.geometry("350x350")
        update_f_name = Label(update_window, text='First name: ')
        update_f_name.grid(row=1, column=0)
        update_f_name_entry = Entry(update_window)
        update_f_name_entry.grid(row=1, column=1)

        update_l_name = Label(update_window, text='Last name: ')
        update_l_name.grid(row=2, column=0)
        update_l_name_entry = Entry(update_window)
        update_l_name_entry.grid(row=2, column=1)

        update_address = Label(update_window, text='Address: ')
        update_address.grid(row=3, column=0, sticky='w')
        update_address_entry = Entry(update_window)
        update_address_entry.grid(row=3, column=1)

        update_button_submit = Button(update_window, text="Submit update", command=confirm_update_id)
        update_button_submit.grid(row=4, column=1, sticky="nw", padx=2, pady=5)

    frame3 = LabelFrame(root, padx=5, pady=2)
    frame3.grid(padx=10, pady=5, columnspan=4, column=8, row=0, sticky="ne")
    label = Label(frame3, text="hi")
    label.grid()

    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute("""CREATE TABLE residences (
                f_name text,
                l_name text,
                address text
              )""")

    f_name = Label(frame3, text='First name: ')
    f_name.grid(row=1, column=0)
    f_name_entry = Entry(frame3)
    f_name_entry.grid(row=1, column=1)

    l_name = Label(frame3, text='Last name: ')
    l_name.grid(row=2, column=0)
    l_name_entry = Entry(frame3)
    l_name_entry.grid(row=2, column=1)

    address = Label(frame3, text='Address: ')
    address.grid(row=3, column=0, sticky='w')
    address_entry = Entry(frame3)
    address_entry.grid(row=3, column=1)

    button_submit = Button(frame3, text="Submit", command=submit)
    button_submit.grid(row=4, column=1, sticky="nw", padx=2, pady=5)

    button_show = Button(frame3, text="Show address list", command=show_residence)
    button_show.grid(row=5, columnspan=3, sticky="nsew", padx=2, pady=5)

    label_choose_id = Label(frame3, text="Choose ID")
    label_choose_id.grid(row=6, column=0, padx=2, pady=5)

    entry_choose_id = Entry(frame3)
    entry_choose_id.grid(row=6, column=1, sticky='nsew', padx=2, pady=5, columnspan=3)

    button_delete = Button(frame3, text='Delete address by ID', command=delete_id)
    button_delete.grid(row=7, column=0, sticky='nsew', padx=5, pady=5, ipadx=8)

    button_update = Button(frame3, text='Update residences by ID', command=update_id)
    button_update.grid(row=7, column=1, sticky='nsew', padx=5, pady=5, ipadx=8)

    root.mainloop()


'''Bai tap'''


def bai_tap():
    """Bài 01: Viết chương trình thay thế tất cả các ký tự giống ký tự đầu tiên của một Chuỗi thành $."""

    def replacement_training():
        s_01 = input("Nhập vào một chuỗi: ")
        if len(s_01) > 0:
            print(s_01.replace(s_01[0], '$'))
        # replace(old_value, new_value, count(optional))

    '''FINDING THE PERCENTAGE
    https://www.hackerrank.com/challenges/finding-the-percentage/problem'''

    def percentage():
        n = int(input())
        student_marks = {}
        for _ in range(n):
            name, *line = input().split()
            scores = list(map(float, line))
            student_marks[name] = scores
        query_name = input()
        query_score = student_marks[query_name]
        a = (sum(query_score) / len(query_score))
        print("{0:.2f}".format(a))

    '''NESTED LISTS
    https://www.hackerrank.com/challenges/nested-list/problem'''

    def nested_lst():
        list_score = []
        list_name = []
        n = int(input())
        result = []
        for _ in range(n):
            name = input()
            score = float(input())
            list_name.append(name)
            list_score.append(score)

        sorted_list_score = sorted(set(list_score))
        for x in range(n):
            if list_score[x] == sorted_list_score[1]:
                result.append(list_name[x])
        true_result = sorted(result)
        for x in range(len(true_result)):
            print(true_result[x])

    '''FIND THE RUNNER-UP SCORE!
    https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem'''

    def find_max():
        n = int(input())
        nums = map(int, input().split())
        print(sorted(list(set(nums)))[-2])

    '''LIST COMPREHENSIONS
    https://www.hackerrank.com/challenges/list-comprehensions/problem'''

    def lst_com():
        x, y, z, n = (int(input()) for _ in range(4))
        print([[a, b, c] for a in range(0, x + 1) for b in range(0, y + 1) for c in range(0, z + 1) if a + b + c != n])

    '''PRINT FUNCTION
    https://www.hackerrank.com/challenges/python-print/problem'''

    def prnt():
        n = int(input())
        print(*range(1, n + 1), sep="")

    '''WRITE A FUNCTION   
    https://www.hackerrank.com/challenges/write-a-function/problem'''

    def is_leap(year):
        return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

    '''PYTHON IF-ELSE
    https://www.hackerrank.com/challenges/py-if-else/problem'''

    def if_else():
        n = int(input().strip())
        if n % 2 == 0 and 1 <= n <= 100:
            if 2 <= n <= 5:
                print("Not Weird")
            elif 6 <= n <= 20:
                print('Weird')
            else:
                print('Not Weird')
        else:
            print('Weird')

    '''FIND A STRING
    https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=false'''

    def count_substring(string, sub_string):
        repeat = 0
        for n in range(0, len(string) - 1):
            if string[n + 1:n + len(sub_string)] == sub_string[1:]:
                repeat += 1
            else:
                continue
        return repeat

    'GUESSING GAME W/ NUMBER'

    def guessing_game():
        print("I'm thinking of a number between 1 and 100")
        print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
        print("If your guess is within 10 of my number, I'll tell you you're WARM")
        print("If your guess is farther/closer than your most recent guess, I'll say you're getting COLDER/WARMER")
        print("LET'S PLAY!")

        import random
        guesses = [0]
        num = random.randint(1, 100)
        print(num)

        while True:
            # we can copy the code from above to take an input
            guess = int(input('Between 1 and 100, what is your guess?'))
            if guess < 1 or guess > 100:
                print('OUT OF BOUNDS! Please try again: ')
                continue

            # here we compare the player's guess to our number
            if guess == num:
                print(f'CONGRATULATIONS, IT TOOK {len(guesses)} GUESSES!!')
                break

            guesses.append(guess)
            # if guess is incorrect, add guess to the list
            # when testing the first guess, guesses[-2]==0, which evaluates to False
            # and brings us down to the second section
            if guesses[-2] == 0:
                if abs(num - guess) < abs(num - guesses[-2]):
                    print('WARMER!')
                else:
                    print('COLDER!')
            else:
                if abs(num - guess) <= 10:
                    print('WARM!')
                else:
                    print('COLD!')

    '''LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers
    if both numbers are even, but returns the greater if one or both numbers are odd'''

    def lesser(a, b):
        if a % 2 == 0 and b % 2 == 0:
            return min(a, b)
        else:
            return max(a, b)

    '''ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter'''

    def animal_crackers(text):
        wordlist = text.split()
        return wordlist[0][0] == wordlist[1][0]

    '''MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20.'''

    def makes_twenty(n1, n2):
        return (n1 + n2) == 20 or n1 == 20 or n2 == 20

    'OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name'

    def old_macdonald(name):
        if len(name) > 3:
            return name[:3].capitalize() + name[3:].capitalize()
        else:
            return 'Name is too short!'

    'MASTER YODA: Given a sentence, return a sentence with the words reversed'

    def master_yoda(saying):
        n = saying.split()
        reverse_saying = list(reversed(n))
        result = " ".join(reverse_saying)
        return result.capitalize()

    def master_yoda(text):
        return ' '.join(text.split()[::-1])

    'Given an integer n, return True if n is within 10 of either 100 or 200'

    def almost_there(n):
        return abs(n - 100) <= 10 or abs(n - 200) <= 10

    'FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.'

    def has_33(list_number):
        for n in range(len(list_number) - 1):
            "return list_number[n] == list_number[n+1] and list_number[n] == 3"
            return list_number[n:n + 2] == [3, 3]

    'PAPER DOLL: Given a string, return a string where for every character in the original there are three characters'

    def paper_doll(text):
        new_text = ""
        for n in text:
            new_text += n * 3
        return new_text

    'SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order'

    def spy_game(nums):
        spy_check = False
        spy_double_check = False
        spy_code = []
        for num in nums:
            while not spy_check:
                if num == 0:
                    spy_check = True
                    spy_code.append(num)
                    continue
                else:
                    break
            while spy_check:
                if num == 0:
                    spy_double_check = True
                    spy_code.append(num)
                    break
                else:
                    break
            while spy_check and spy_double_check:
                if num == 7:
                    spy_code.append(num)
                    break
                else:
                    break
        return spy_code == [0, 0, 0, 7]

    def spy_game(nums):
        code = [0, 0, 7, 'x']
        for num in nums:
            if num == code[0]:
                code.pop(0)  # code.remove(num) also works

        return len(code) == 1

    'COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number'

    def count_prime(lst_end):
        lst = []
        prime_num = 0
        prime_total = []
        for n in range(2, lst_end + 1):
            lst.append(n)
        for m in lst:
            for l in range(1, m + 1):
                if m % l == 0:
                    prime_num += 1
                else:
                    continue
            if prime_num == 2:
                prime_total.append(m)
                prime_num = 0
            else:
                prime_num = 0
        return prime_total

    '''PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
    print_big('a')
     *
    * *
    *****
    *    *
    *    *'''

    def print_big(num):
        small_big = {}
        if num == "a":
            small_big[num] = """
             *
            * *
           *****
           *   *
           *   *   
           """
        if num == "b":
            small_big[num] = """
           *****
           *   *
           *****
           *   *
           *****
           """
        return small_big[num]

    def print_big(letter):
        patterns = {1: '  *  ', 2: ' * * ', 3: '*   *', 4: '*****', 5: '**** ', 6: '   * ', 7: ' *   ', 8: '*   * ',
                    9: '*    '}
        alphabet = {'A': [1, 2, 4, 3, 3], 'B': [5, 3, 5, 3, 5], 'C': [4, 9, 9, 9, 4], 'D': [5, 3, 3, 3, 5],
                    'E': [4, 9, 4, 9, 4]}
        for pattern in alphabet[letter.upper()]:
            print(patterns[pattern])

    'Write a function that computes the volume of a sphere given radius.'

    def lam_math():
        import math
        y = lambda x: (x ** 3) * (4 / 3) * (math.pi)
        print(y(2))

    'Write a Python function that accepts a string and calculates the number of uppercase letters and lower case letters.'

    def up_low(s):
        low_count = []
        high_count = []
        for n in s:
            if n.isupper():
                high_count.append(n)
            elif n.islower():
                low_count.append(n)
            else:
                pass
        return f"{low_count}\n{high_count}"

    'Write a Python function that checks whether a word or phrase is palindrome or not.'

    def palindrome(s):
        new_s = s.replace(" ", "")
        return new_s.lower() == new_s[::-1].lower()

    'Write a Python function to check whether a string is a pangram or not. (Assume it does not have punctuation)'

    # import string
    def ispangram(lst):
        new_lst = sorted(set(lst.replace(" ", "").lower()))
        return new_lst == list(string.ascii_lowercase)

    '''VALIDATORS
    https://www.hackerrank.com/challenges/string-validators/problem'''

    def validators():
        s = input()
        print(any(c.isalnum() for c in s))
        print(any(c.isalpha() for c in s))
        print(any(c.isdigit() for c in s))
        print(any(c.islower() for c in s))
        print(any(c.isupper() for c in s))

    '''TEXT WRAP
    https://www.hackerrank.com/challenges/text-wrap/problem'''

    def wrap(string, max_width):
        return "\n".join([string[i:i + max_width] for i in range(0, len(string), max_width)])

    '''String Formatting
    https://www.hackerrank.com/challenges/python-string-formatting/problem'''

    def print_formatted(n):
        binn = bin(n).replace("0b", "")
        for i in range(1, n + 1):
            deci = str(i).rjust(len(binn), " ")

            octa = oct(i).replace("0o", "").rjust(len(binn), " ")

            hexi = hex(i).replace("0x", "").upper().rjust(len(binn), " ")

            bina = bin(i).replace("0b", "").rjust(len(binn), " ")

            print(deci, octa, hexi, bina, sep="")

    '''ALPHABET RANGOLI
    https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true
    '''

    def print_rangoli(size):
        alphabet = str(string.ascii_lowercase)
        for n in range(0, size):
            print(
                *(alphabet[(size - 1):(size - 1 - n):-1] + alphabet[(size - 1 - n):(size)]).center((1 + (size - 1) * 2),
                                                                                                   "-"), sep="-")
        for n in range(size - 2, -1, -1):
            print(
                *(alphabet[(size - 1):(size - 1 - n):-1] + alphabet[(size - 1 - n):(size)]).center((1 + (size - 1) * 2),
                                                                                                   "-"), sep="-")

    '''SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6
    and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers
    '''

    def summer_69(arr):
        total = 0
        add = True
        for num in arr:
            while add:
                if num != 6:
                    total += num
                    break
                else:
                    add = False
            while not add:
                if num != 9:
                    break
                else:
                    add = True
                    break
        return total


'''BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
If their sum exceeds 21 *and* there's an eleven, reduce the total sum by 10.
Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
'''


def blackjack(a, b, c):
    if a + b + c <= 21:
        return a + b + c
    elif a == 11 and b < 11 and c < 11 and 31 > a + b + c > 21:
        return a + b + c - 10
    elif b == 11 and a < 11 and c < 11 and 31 > a + b + c > 21:
        return a + b + c - 10
    elif c == 11 and b < 11 and a < 11 and 31 > a + b + c > 21:
        return a + b + c - 10
    else:
        return "BUST"


'TIC TAC TOE FOR 2'


def tic_tac_toe():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    lst_check = lst[:]
    game_end = True

    def display(lst_pa):
        print(f'''
      {lst_pa[0]}|{lst_pa[1]}|{lst_pa[2]}
      -|-|-
      {lst_pa[3]}|{lst_pa[4]}|{lst_pa[5]}
      -|-|-
      {lst_pa[6]}|{lst_pa[7]}|{lst_pa[8]}
      ''')

    def name():
        f_name = input("What's your name mate?")
        s_name = input("What's your name, buddy?")
        return f_name, s_name

    def x_or_o():
        f_symbol_pa = "Undecided"
        s_symbol_pa = "Remain"

        while f_symbol_pa not in ["X", "O"]:
            f_symbol_pa = input("You go first so choose X or O").upper()
            if f_symbol_pa not in ["X", "O"]:
                clear_output()
                print("Hey choose again dude, it's supposed to be X or O only")
            elif f_symbol_pa == "X":
                s_symbol_pa = "O"
            else:
                s_symbol_pa = "X"

        return f_symbol_pa, s_symbol_pa

    def position_choice_1(f_name_pa, f_symbol_pa, new_lst_pa, lst_check_pa):
        f_choice = "Unchosen"

        while f_choice not in lst_check_pa:
            f_choice = int(input(f"It's your turn, {f_name_pa}. Choose from {lst_check_pa} to place {f_symbol_pa}"))
            if f_choice not in lst_check_pa:
                clear_output()
                print(f"Hey {lst_check_pa} only. Try again")

        new_lst_pa[int(f_choice) - 1] = f_symbol_pa
        lst_check_pa.remove(f_choice)

        return new_lst_pa, lst_check_pa

    def position_choice_2(s_name_pa, s_symbol_pa, new_lst_pa, lst_check_pa):
        s_choice = "Unchosen"
        while s_choice not in lst_check_pa:
            s_choice = int(input(f"It's your turn, {s_name_pa}. Choose from {lst_check_pa} to place {s_symbol_pa}"))
            if s_choice not in lst_check_pa:
                clear_output()
                print(f"Hey in {lst_check_pa} only. Try again")

        new_lst_pa[int(s_choice) - 1] = s_symbol_pa
        lst_check_pa.remove(s_choice)

        return new_lst_pa, lst_check_pa

    def check_win(f_name_pa, s_name_pa, new_lst_pa, lst_check_pa, s_symbol_pa, f_symbol_pa):
        if new_lst_pa[0] == new_lst_pa[1] == new_lst_pa[2] == f_symbol_pa \
                or new_lst_pa[3] == new_lst_pa[4] == new_lst_pa[5] == f_symbol_pa \
                or new_lst_pa[6] == new_lst_pa[7] == new_lst_pa[8] == f_symbol_pa \
                or new_lst_pa[0] == new_lst_pa[3] == new_lst_pa[6] == f_symbol_pa \
                or new_lst_pa[1] == new_lst_pa[4] == new_lst_pa[7] == f_symbol_pa \
                or new_lst_pa[2] == new_lst_pa[5] == new_lst_pa[8] == f_symbol_pa \
                or new_lst_pa[0] == new_lst_pa[4] == new_lst_pa[8] == f_symbol_pa \
                or new_lst_pa[2] == new_lst_pa[4] == new_lst_pa[6] == f_symbol_pa:
            result_returned = f"You did it {f_name_pa}. You win! Shame on you {s_name_pa}"
            return False, result_returned

        elif new_lst_pa[0] == new_lst_pa[1] == new_lst_pa[2] == s_symbol_pa \
                or new_lst_pa[3] == new_lst_pa[4] == new_lst_pa[5] == s_symbol_pa \
                or new_lst_pa[6] == new_lst_pa[7] == new_lst_pa[8] == s_symbol_pa \
                or new_lst_pa[0] == new_lst_pa[3] == new_lst_pa[6] == s_symbol_pa \
                or new_lst_pa[1] == new_lst_pa[4] == new_lst_pa[7] == s_symbol_pa \
                or new_lst_pa[2] == new_lst_pa[5] == new_lst_pa[8] == s_symbol_pa \
                or new_lst_pa[0] == new_lst_pa[4] == new_lst_pa[8] == s_symbol_pa \
                or new_lst_pa[2] == new_lst_pa[4] == new_lst_pa[6] == s_symbol_pa:
            result_returned = f'You did it {s_name_pa}. You win! Shame on you {f_name_pa}'
            return False, result_returned

        elif lst_check_pa == "":
            result_returned = "Out of space. It's a draw then"
            return False, result_returned

        else:
            result_returned = "Undecided"
            return True, result_returned

    def game_restart():
        choice = 'wrong'

        while choice not in ['Y', 'N']:
            choice = input("Would you like to keep playing? Y or N ")
            if choice not in ['Y', 'N']:
                clear_output()
                print("Sorry, I didn't understand. Please make sure to choose Y or N.")

        if choice == "Y":
            return True
        else:
            return False

    print("Welcome to Tic Tac Toe for 2")
    f_name_returned, s_name_returned = name()
    f_symbol, s_symbol = x_or_o()
    display(lst)
    while game_end:
        clear_output()
        lst, lst_check = position_choice_1(f_name_returned, f_symbol, lst, lst_check)
        clear_output()
        display(lst)

        game_end, result = check_win(f_name_returned, s_name_returned, lst, lst_check, s_symbol, f_symbol)
        if game_end is False:
            print(result)
            game_end = game_restart()
            if game_end is False:
                print("Thanks for playing. Have a nice day!")
                break
            else:
                lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                lst_check = lst[:]
                game_end = True
                continue

        lst, lst_check = position_choice_2(s_name_returned, s_symbol, lst, lst_check)
        clear_output()
        display(lst)

        game_end, result = check_win(f_name_returned, s_name_returned, lst, lst_check, s_symbol, f_symbol)
        if game_end is False:
            print(result)
            game_end = game_restart()
            if game_end is False:
                print("Thanks for playing. Have a nice day!")
                break
            else:
                lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                lst_check = lst[:]
                game_end = True
                continue


'War card game'


def war_card_game():
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
              'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

    class Card:
        def __init__(self, rank, suit):
            self.suit = suit
            self.rank = rank
            self.value = values[rank]

        def __str__(self):
            return f'{self.rank} of {self.suit}'

    class Deck:
        def __init__(self):
            self.all_cards = []
            for r in ranks:
                for s in suits:
                    self.all_cards.append(Card(r, s))

        def __str__(self):
            return f'The number of cards in the deck is {len(self.all_cards)}'

        def deal_card(self):
            return self.all_cards.pop()

        def shuffle(self):
            return shuffle(self.all_cards)

    class Player:
        def __init__(self, name):
            self.name = name
            self.player_deck = []
            self.player_table = []

        def play_card(self):
            return self.player_deck.pop(0)

        # you pop at the"top" because you append at the "bottom". Check example 6 at bottom
        # compared to 5 and 7 at other bottom
        def win_card(self, new_card):
            if isinstance(new_card, list):
                self.player_deck.extend(new_card)
            else:
                self.player_deck.append(new_card)

        def __str__(self):
            return f'is the {len(self.player_deck)}'

    player_one = Player("Yugi")
    player_two = Player("Kaiba")

    deck = Deck()
    deck.shuffle()

    for _ in range(26):
        player_one.win_card(deck.deal_card())
        player_two.win_card(deck.deal_card())

    game_start = True
    round_num = 0

    while game_start:
        round_num += 1
        print(f'{round_num} begins')

        if len(player_one.player_deck) == 0:
            print(f"{player_one.name} loses due to out of card")
            break
        if len(player_two.player_deck) == 0:
            print(f"{player_two.name} loses due to out of cards")
            break
        # prevent play card error in case you used exactly those last 5 cards for war and lost

        player_one.player_table = []
        player_one.player_table.append(player_one.play_card())
        player_two.player_table = []
        player_two.player_table.append(player_two.play_card())

        war_on = True
        while war_on:
            if player_one.player_table[-1].value > player_two.player_table[-1].value:
                player_one.win_card(player_one.player_table)
                player_one.win_card(player_two.player_table)
                war_on = False

            elif player_two.player_table[-1].value > player_one.player_table[-1].value:
                player_two.win_card(player_two.player_table)
                player_two.win_card(player_one.player_table)
                war_on = False
            else:
                print("It's war")
                if len(player_one.player_deck) < 5:
                    print(f"{player_one.name} loses due to inability to war")
                    game_start = False
                    break
                elif len(player_two.player_deck) < 5:
                    print(f'{player_two.name} loses due to inability to war')
                    game_start = False
                    break
                else:
                    for _ in range(5):
                        player_one.player_table.append(player_one.play_card())
                        player_two.player_table.append(player_two.play_card())


'Overly complicated blackjack'


def blackjack_overly_complicated():
    CARD_RANK = ("A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2")
    CARD_SUIT = ("♡", "♢", "♧", "♤")
    SYSTEM_COLORS = ['grey', 'white']
    PLAYER_COLORS = list(c for c in COLORS.keys() if c not in SYSTEM_COLORS)
    MAX_PLAYERS = len(PLAYER_COLORS)

    class Card(object):
        """Represents an individual playing card"""

        def __init__(self, rank, suit):
            assert rank in CARD_RANK
            self.rank = rank
            assert suit in CARD_SUIT
            self.suit = suit

        def __repr__(self):
            return "{:>2}{}".format(self.rank, self.suit)

        def value(self):
            """Computes the value of a card according to Blackjack rules"""
            if self.ace():
                value = 11
            else:
                try:
                    value = int(self.rank)
                except ValueError:
                    value = 10
            return value

        def ace(self):
            """Is this card an ace?"""
            return self.rank == "A"

    class Deck(object):
        """Represents deck of 52 cards to be dealt to the player and dealer"""

        def __init__(self):
            self.__new_deck()

        def __new_deck(self):
            """Create a new deck of 52 cards"""
            self.cards = list(Card(r, s) for r in CARD_RANK for s in CARD_SUIT)

        def shuffle(self):
            """Randomly shuffle the deck of cards"""
            random.shuffle(self.cards)

        def deal(self):
            """Deal from the end of the deck - if the deck is empty, start a new one"""
            if not self.cards:
                self.__new_deck()
                self.shuffle()
            return self.cards.pop()

    class Hand(object):
        """Represents the cards held by the player or the dealer"""

        def __init__(self, stake=0):
            self.cards = []
            self.stake = stake
            self.active = True

        def __repr__(self):
            return "  ".join(str(card) for card in self.cards)

        def first(self):
            """Returns the first card in the hand"""
            assert self.cards
            return self.cards[0]

        def last(self):
            """Returns the last card in the hand"""
            assert self.cards
            return self.cards[-1]

        def add_card(self, card):
            """Add the instance of card to the hand"""
            self.cards.append(card)

        def value(self):
            """Calculate the value of the hand, taking into account Aces can be 11 or 1"""
            aces = sum(1 for c in self.cards if c.ace())
            value = sum(c.value() for c in self.cards)
            while value > 21 and aces > 0:
                aces -= 1
                value -= 10
            return value

        def blackjack(self):
            """Determine if the hand is 'blackjack'"""
            return len(self.cards) == 2 and self.value() == 21

        def twenty_one(self):
            """Determine if the hand is worth 21"""
            return self.value() == 21

        def bust(self):
            """Determine if the hand is worth more than 21, known as a 'bust'"""
            return self.value() > 21

        def pair(self):
            """Determine if the hand is two cards the same"""
            return len(self.cards) == 2 and self.first().rank == self.last().rank

        def split(self):
            """Split this hand into two hands if it can be split"""
            assert self.pair()
            card = self.cards.pop()
            hand = Hand(self.stake)
            hand.add_card(card)
            return hand

    class Player(object):
        """Represents a player or the dealer in the game"""

        def __init__(self, name, chips, color='green'):
            assert chips > 0
            assert color in PLAYER_COLORS
            self.chips = chips
            self.hands = []
            self.insurance = 0
            self.name = name
            self.color = color
            self.results = {'wins': 0, 'ties': 0, 'losses': 0}

        def can_double_down(self, hand):
            """Is the player entitled to double down?"""
            return (self.has_chips(hand.stake) and
                    (len(hand.cards) == 2 or
                     hand.value() in (9, 10, 11)))

        def active_hands(self):
            """Generator of hands still active in this round"""
            for hand in self.hands:
                if hand.active:
                    yield hand

        def has_active_hands(self):
            """Does the player have any active hands?"""
            return list(h for h in self.hands if h.active)

        def can_split(self, hand):
            """Is the player entitled to split their hand?"""
            return self.has_chips(hand.stake) and hand.pair()

        def has_chips(self, amount=0):
            """Does the player have sufficient chips left?"""
            assert amount >= 0
            if amount == 0:
                return self.chips > 0
            return self.chips >= amount

        def push(self, bet):
            """Player bet is preserved"""
            assert bet > 0
            self.chips += bet
            self.results['ties'] += 1

        def win(self, bet, odds=1):
            """Player wins at the odds provided"""
            assert bet > 0
            assert odds >= 1
            self.chips += int(bet * (odds + 1))
            self.results['wins'] += 1

        def loss(self):
            """Player loses their bet"""
            self.results['losses'] += 1

        def bet(self, bet):
            """Player places a bet"""
            assert bet > 0
            assert self.has_chips(bet)
            self.chips -= bet
            return bet

    class Game(object):
        """Controls the actions of the game"""

        def __init__(self, names, chips):
            self.deck = Deck()
            self.deck.shuffle()
            self.colors = list(PLAYER_COLORS)
            self.players = list(Player(name, chips, self.__get_color()) for name in names)
            self.max_name_len = max(max(len(name) for name in names), len("Dealer"))
            self.playing = False
            self.dealer = None
            self.insurance = False

        def __get_color(self):
            """Obtain a random color from available termcolors"""
            assert self.colors
            colors = self.colors
            color = random.choice(colors)
            colors.remove(color)
            return color

        def __deal_card(self, name, hand, color="white", announce=True):
            """Take the next available card from deck and add to hand"""
            card = self.deck.deal()
            hand.add_card(card)
            if announce:
                time.sleep(1)
                prompt = "dealt {}  {:>2} : {}".format(card, hand.value(), hand)
                print(self.format_text(name, prompt, color))

        def __get_bet(self, player, question, minimum, multiple):
            """Ask player for their bet and check constraints on answer"""
            print()
            print(self.format_text(player.name, question.lower(), player.color))
            prompt = "{} available, {} minimum, multiples of {} only".format(
                player.chips, minimum, multiple)
            print(self.format_text(player.name, prompt, player.color))
            bet = -1
            while bet < minimum or bet > player.chips or bet % multiple != 0:
                bet = input(self.format_text(
                    player.name, "enter amount ({}): ".format(minimum), player.color))
                if bet == '':
                    bet = minimum
                else:
                    try:
                        bet = int(bet)
                    except ValueError:
                        pass
            return bet

        def format_text(self, name, text, color="white"):
            """Prefix output with player's name and colorize"""
            name = name.rjust(self.max_name_len)
            return colored("{} > {}".format(name, text), color)

        def players_with_chips(self, min=0):
            """Returns a list of players with chips remaining"""
            return list(p for p in self.players if p.has_chips(min))

        def active_players(self):
            """Generator of layers with active hands"""
            for player in self.players:
                if player.has_active_hands():
                    yield player

        def has_active_hands(self):
            """Are there any active hands remaining?"""
            return list(p for p in self.players if p.has_active_hands())

        def setup(self):
            """Obtain bets and deal two cards to the player and the dealer"""
            hands = []
            self.playing = True
            min_bet = 10
            random.shuffle(self.players)
            players = self.players_with_chips(min_bet)
            if not players:
                return
            for player in players:
                player.insurance = 0
                bet = self.__get_bet(player, "How much would you like to bet?", min_bet, 2)
                hand = Hand(bet)
                hands.append(hand)
                player.bet(bet)
                player.hands = [hand]
            dealer = Hand(0)
            for _ in range(2):
                for hand in hands:
                    self.__deal_card(_, hand, announce=False)
                self.__deal_card(_, dealer, announce=False)
            print()
            for player in players:
                hand = player.hands[0]
                prompt = "hand dealt {:>2} : {}".format(hand.value(), hand)
                print(self.format_text(player.name, prompt, player.color))
            print(self.format_text("Dealer", "face up card  : {}".format(dealer.first())))
            self.dealer = dealer

        def offer_insurance(self):
            """Offer insurance if applicable"""
            if self.dealer.first().ace():
                players = self.players_with_chips()
                for player in players:
                    bet = self.__get_bet(player, "would you like to take insurance?", 0, 2)
                    if bet > 0:
                        player.insurance = player.bet(bet)
                    else:
                        player.insurance = 0

        def check_for_dealer_blackjack(self):
            """Check if dealer has blackjack and settle bets accordingly"""
            dealer = self.dealer
            players = self.active_players()
            if dealer.blackjack():
                self.playing = False
                print()
                print(self.format_text("Dealer", "scored blackjack : {}".format(dealer)))
                for player in players:
                    for hand in player.active_hands():
                        if player.insurance:
                            print(self.format_text(
                                player.name, "you won your insurance bet!", player.color))
                            player.win(player.insurance, odds=2)
                        self.settle_outcome(dealer, player, hand)
            elif dealer.first().ace():
                print()
                print(self.format_text("Dealer", "did not score blackjack"))
                for player in players:
                    if player.insurance:
                        print(self.format_text(
                            player.name, "you lost your insurance bet!", player.color))
                        player.loss()

        def check_for_player_blackjack(self):
            """Check if any player has blackjack and settle bets accordingly"""
            dealer = self.dealer
            players = self.active_players()
            for player in players:
                for hand in player.active_hands():
                    if hand.blackjack():
                        print(self.format_text(player.name, "you scored blackjack!", player.color))
                        self.settle_outcome(dealer, player, hand)

        def settle_outcome(self, dealer, player, hand):
            """Decide the outcome of the player's hand compared to the dealer"""
            hand.active = False
            if hand.value() > dealer.value() or dealer.bust():
                outcome = "you beat the dealer! :)"
                if hand.blackjack():
                    odds = 1.5
                else:
                    odds = 1
                player.win(hand.stake, odds)
            elif hand.value() == dealer.value():
                outcome = "you tied with the dealer :|"
                player.push(hand.stake)
            else:
                outcome = "you lost to the dealer :("
                player.loss()
            print(self.format_text(player.name, outcome, player.color))

        def split_hand(self, player, hand):
            """Split player's hand if possible"""
            if hand.pair() and player.has_chips(hand.stake):
                prompt = "would you like to split your pair? (Y/n): "
                prompt = self.format_text(player.name, prompt, player.color)
                resp = get_response(prompt, ("Y", "N"), "Y")
                if resp == "Y":
                    new_hand = hand.split()
                    player.bet(hand.stake)
                    self.__deal_card(player.name, hand, player.color)
                    self.__deal_card(player.name, new_hand, player.color)
                    player.hands.append(new_hand)
                    self.show_hand(player.name, hand, player.color)

        def hit(self, player, hand):
            """Draw another card for player hand and determine outcome if possible"""
            self.__deal_card(player.name, hand, player.color)

        def bust(self, player, hand):
            """Handle a player's hand that has busted"""
            print(self.format_text(player.name, "busted! :(", player.color))
            player.loss()
            hand.active = False

        def double_down(self, player, hand):
            """Player wishes to double their bet and receive one more card"""
            player.bet(hand.stake)
            hand.stake += hand.stake
            self.__deal_card(player.name, hand, player.color)
            if hand.bust():
                self.bust(player, hand)

        def dealer_turn(self):
            """Controls the dealer's turn and determines the outcome of the game"""
            dealer = self.dealer
            print()
            prompt = "turns {}  {:>2} : {}".format(
                dealer.last(),
                dealer.value(),
                dealer)
            print(self.format_text("Dealer", prompt))
            while dealer.value() < 17:
                self.__deal_card("Dealer", dealer)
            if dealer.bust():
                print(self.format_text("Dealer", "busted!"))
            for player in self.active_players():
                for hand in player.active_hands():
                    self.settle_outcome(dealer, player, hand)

        def results(self):
            """Print player statistics"""
            print()
            players = sorted(self.players,
                             reverse=True,
                             key=lambda x: (x.chips,
                                            x.results['wins'] * 3 + x.results['ties'],
                                            -x.results['losses']))
            for player in players:
                results = ",  ".join("{}: {:>2}".format(k, v) for k, v in player.results.items())
                prompt = "chips: {:>3},  {}".format(player.chips, results)
                print(self.format_text(player.name, prompt, player.color))

        def show_hand(self, name, hand, color="white"):
            """Print player's current hand"""
            print()
            prompt = "hand value {:>2} : {}".format(hand.value(), hand)
            print(self.format_text(name, prompt, color))

        def play_hands(self):
            """Play any active hands until completed"""
            if self.playing:
                for player in self.active_players():
                    for hand in player.active_hands():
                        self.play_hand(player, hand)
                if self.has_active_hands():
                    self.dealer_turn()

        def play_hand(self, player, hand):
            """Play the hand until finished"""
            self.show_hand(player.name, hand, player.color)
            if player.can_split(hand):
                self.split_hand(player, hand)

            while hand.active:
                if hand.twenty_one():
                    print(self.format_text(player.name, "scored 21! :)", player.color))
                    break
                if hand.bust():
                    self.bust(player, hand)
                    break
                if player.can_double_down(hand):
                    question = "would you like to hit, stand or double down? (H/s/d): "
                    answers = ('H', 'S', 'D')
                else:
                    question = "would you like to hit or stand? (H/s): "
                    answers = ('H', 'S')

                prompt = self.format_text(player.name, question, player.color)
                resp = get_response(prompt, answers, default='H')
                if resp == 'H':
                    if self.hit(player, hand):
                        break
                elif resp == 'S':
                    break
                elif resp == 'D':
                    self.double_down(player, hand)
                    break
                else:
                    # should never get here!
                    raise ValueError

    def clear_screen():
        """Clear the screen for better view"""
        print("\033[H\033[J")

    def continue_prompt():
        """Clear the screen before starting a new round"""
        print()
        input("Hit enter to continue - ctrl-c to exit: ")
        clear_screen()

    def get_response(question, accepted, default):
        """Get input that matches the accepted answers"""
        while True:
            resp = input(question).upper()
            if resp == '':
                resp = default
            if resp in accepted:
                break
        return resp

    def start_game():
        """Obtain player names and starting chips"""
        while True:
            prompt = "Enter up to {} player names or return for single player game: "
            names = input(prompt.format(MAX_PLAYERS))
            if names == '':
                names = ["Player"]
            else:
                names = names.split(' ')
            if len(names) > MAX_PLAYERS:
                print("Maximum of {} players only please!".format(MAX_PLAYERS))
            else:
                break

        print()
        chips = input("Enter starting number of chips (100): ")
        if chips == '':
            chips = 100
        else:
            chips = int(chips)
        return Game(names, chips)

    def main():
        """Run the main game loop"""
        clear_screen()
        print("""
              Welcome to Blackjack!
              ---------------------
    This is the gambling game also known as 21
    where you and others can play against the
    computer dealer.
    There is one 52 pack of cards in the deck
    and the rules are documented here*. Purely
    for fun, the game tracks your results and
    and reports them at the conclusion.
    * https://en.wikipedia.org/wiki/Blackjack
        """)

        # collect names of the players and their starting chip balance
        # then cycle through game process:
        # - deal initial cards
        # - offer insurance if dealer up card is A
        # - check dealer blackjack and announce results if true
        # - then for each player:
        #   - for each hand
        #       - offer split, double down, hit or stand as appropriate
        #       - if player busts, mark as finished and move to next
        # - then dealer plays until busts or stands
        # - show results and settle bets
        # -> repeat
        # when game is complete show results for each player

        # collect names of the players and their starting chip balance

        try:
            print()
            game = start_game()

            while True:
                continue_prompt()
                if not game.players_with_chips(10):
                    print("No one with any chips remaining - game over")
                    break
                game.setup()
                game.offer_insurance()
                game.check_for_dealer_blackjack()
                game.check_for_player_blackjack()
                game.play_hands()

        except KeyboardInterrupt:
            print()
        finally:
            if game:
                game.results()
            print()
            print("Thanks for playing.")
            print()

    if __name__ == '__main__':
        main()
