from tkinter import *
from tkinter import ttk
from prueba import exam

questions = [
    {
        'Pregunta': '¿Ella fuma mari sola?',
        'Respuestas': ['a) si', 'b) no', 'c) tal vez', 'd) popola'],
        'Correcta': 4
    },
    {
        'Pregunta': 'Does she give a fo?',
        'Respuestas': ['a) si', 'b) no', 'c) tal vez', 'd) sabe que la quiero'],
        'Correcta': 6
    },
    {
        'Pregunta': 'No se que poner',
        'Respuestas': ['a) ama', 'b) me', 'c) mie', 'd) si'],
        'Correcta': 9
    }
]


prueba = Tk()

prueba.geometry('1250x630+10+10')

frm = ttk.Frame(prueba, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World").grid(column=0, row=0)
ttk.Button(frm, text='Quit', command=prueba.destroy).grid(column=1, row=0)

exam(prueba, 2, questions)

prueba.mainloop()