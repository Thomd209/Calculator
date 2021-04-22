from tkinter import *
from math import pi, e, log, factorial


class Calculator:
    def __init__(self):
        self.ent = Entry(width=195)

        self.one = Button(text='1', width=20, command=lambda: self.ent.insert(END, '1'))
        self.two = Button(text='2', width=20, command=lambda: self.ent.insert(END, '2'))
        self.three = Button(text='3', width=20, command=lambda: self.ent.insert(END, '3'))
        self.add = Button(text='+', width=20, command=lambda: self.ent.insert(END, '+'))
        self.sub = Button(text='-', width=20, command=lambda: self.ent.insert(END, '-'))
        self.mul = Button(text='*', width=20, command=lambda: self.ent.insert(END, '*'))
        self.del_last_char = Button(text='<-', width=20, command=lambda: self.ent.delete(len(self.ent.get()) - 1))

        self.four = Button(text='4', width=20, command=lambda: self.ent.insert(END, '4'))
        self.five = Button(text='5', width=20, command=lambda: self.ent.insert(END, '5'))
        self.six = Button(text='6', width=20, command=lambda: self.ent.insert(END, '6'))
        self.div = Button(text='/', width=20, command=lambda: self.ent.insert(END, '//'))
        self.div_rem = Button(text='%', width=20, command=lambda: self.ent.insert(END, '%'))
        self.exp = Button(text='x^n', width=20, command=lambda: self.ent.insert(END, '**'))
        self.exp_2 = Button(text='x^2', width=20, command=lambda: self.ent.insert(END, '**2'))

        self.seven = Button(text='7', width=20, command=lambda: self.ent.insert(END, '7'))
        self.eight = Button(text='8', width=20, command=lambda: self.ent.insert(END, '8'))
        self.nine = Button(text='9', width=20, command=lambda: self.ent.insert(END, '9'))
        self.square_root = Button(text='x^0.5', width=20, command=lambda: self.ent.insert(END, '**0.5'))
        self.const_pi = Button(text='pi', width=20, command=lambda: self.ent.insert(END, 'pi'))
        self.const_e = Button(text='e', width=20, command=lambda: self.ent.insert(END, 'e'))
        self.log = Button(text='log', width=20, command=lambda: self.ent.insert(END, 'log('))

        self.all_clear = Button(text='AC', width=20, command=lambda: self.ent.delete(0, END))
        self.zero = Button(text='0', width=20, command=lambda: self.ent.insert(END, '0'))
        self.dot = Button(text='.', width=20, command=lambda: self.ent.insert(END, '.'))
        self.fact = Button(text='x!', width=20, command=lambda: self.ent.insert(END, 'factorial('))
        self.comma = Button(text=',', width=20, command=lambda: self.ent.insert(END, ','))
        self.open_bracket = Button(text='(', width=20, command=lambda: self.ent.insert(END, '('))
        self.close_bracket = Button(text=')', width=20, command=lambda: self.ent.insert(END, ')'))

        self.result = Button(text='=', width=20, command=self.find_result)

        self.ent.grid(row=0, rowspan=1, columnspan=7, ipadx=10, ipady=10)

        self.one.grid(row=1, column=0, ipadx=10, ipady=10)
        self.two.grid(row=1, column=1, ipadx=10, ipady=10)
        self.three.grid(row=1, column=2, ipadx=10, ipady=10)
        self.add.grid(row=1, column=3, ipadx=10, ipady=10)
        self.sub.grid(row=1, column=4, ipadx=10, ipady=10)
        self.mul.grid(row=1, column=5, ipadx=10, ipady=10)
        self.del_last_char.grid(row=1, column=6, ipadx=10, ipady=10)

        self.four.grid(row=2, column=0, ipadx=10, ipady=10)
        self.five.grid(row=2, column=1, ipadx=10, ipady=10)
        self.six.grid(row=2, column=2, ipadx=10, ipady=10)
        self.div.grid(row=2, column=3, ipadx=10, ipady=10)
        self.div_rem.grid(row=2, column=4, ipadx=10, ipady=10)
        self.exp.grid(row=2, column=5, ipadx=10, ipady=10)
        self.exp_2.grid(row=2, column=6, ipadx=10, ipady=10)

        self.seven.grid(row=3, column=0, ipadx=10, ipady=10)
        self.eight.grid(row=3, column=1, ipadx=10, ipady=10)
        self.nine.grid(row=3, column=2, ipadx=10, ipady=10)
        self.square_root.grid(row=3, column=3, ipadx=10, ipady=10)
        self.const_pi.grid(row=3, column=4, ipadx=10, ipady=10)
        self.const_e.grid(row=3, column=5, ipadx=10, ipady=10)
        self.log.grid(row=3, column=6, ipadx=10, ipady=10)

        self.all_clear.grid(row=4, column=0, ipadx=10, ipady=10)
        self.zero.grid(row=4, column=1, ipadx=10, ipady=10)
        self.dot.grid(row=4, column=2, ipadx=10, ipady=10)
        self.fact.grid(row=4, column=3, ipadx=10, ipady=10)
        self.comma.grid(row=4, column=4, ipadx=10, ipady=10)
        self.open_bracket.grid(row=4, column=5, ipadx=10, ipady=10)
        self.close_bracket.grid(row=4, column=6, ipadx=10, ipady=10)

        self.result.grid(row=5, column=0, ipadx=10, ipady=10)

    def find_result(self):
        try:
            result = eval(self.ent.get())
            self.ent.delete(0, END)
            self.ent.insert(0, result)
        except NameError:
            self.ent.delete(0, END)
            self.ent.insert(0, 'Error!')
        except SyntaxError:
            self.ent.delete(0, END)
            self.ent.insert(0, 'Error!')


root = Tk()
Calculator()
root.mainloop()