questions = [
    {
        'Pregunta': '¿Ella fuma mari sola?',
        'Respuestas': ['a) si', 'b) no', 'c) tal vez', 'd) popola'],
        'Correcta': 'd'
    },
    {
        'Pregunta': '¿Does she give a fo?',
        'Respuestas': ['a) si', 'b) no', 'c) tal vez', 'd) sabe que la quiero'],
        'Correcta': 'b'
    }
]

score = 0

for question in questions:
    print(question['Pregunta'])
    for answer in question['Respuestas']:
        print(answer)
    user_answer = input('Ingresa el inciso correcto: ').lower()
    if user_answer == question['Correcta']:
        print('Correcto')
        score += 1
    else:
        print('La respuesta correcta era:', question['Correcta'])
    
print('Tuviste', score, 'aciertos') if score != 1 else print('Tuviste', score, 'acierto')