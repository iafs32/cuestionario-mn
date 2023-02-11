from tkinter import *
from tkinter import ttk

def exam(window, actual_row, questions):

    options = []

    row_counter = actual_row
    value_counter = 1
    options_counter = 0
    final_score = StringVar()
    final_score.set('0')

    for _ in questions:
        options.append(IntVar())

    for question in questions:
        Label(window, text=question['Pregunta']).grid(column=0, row=row_counter)
        row_counter += 1
        for answer in question['Respuestas']:
            Radiobutton(window, text=answer, variable=options[options_counter],  value=value_counter).grid(column=0, row=row_counter)
            value_counter += 1
            row_counter += 1

        options_counter += 1
        row_counter += 1

    def get_score():
        score = 0
        options_counter = 0
        for question in questions:
            if question['Correcta'] == options[options_counter].get():
                score += 1
            options_counter += 1
        final_score.set(score)
        

    Label(window, textvariable=final_score).grid(row=row_counter, column=0)
    Button(window, text='Enviar', command=get_score).grid(row=row_counter+1, column=0)

