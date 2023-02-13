import os

questions = [
    {
        'Pregunta': '1° Este método emplea fórmulas matemáticas\n para obtener soluciones, en las que\n se definen variables de entrada para el\n cálculo de una o más variables de salida:',
        'Respuestas': ['a) Método analítico', 'b) Método grafico', 'c) Método de tanteo', 'd) Ninguno de los anteriores'],
        'Correcta': 'a'
    },
    {
        'Pregunta': '2° Es un método simple para obtener\n una aproximación a la raíz de una ecuación,\n consiste en graficar la función y\n observar en donde cruzan los ejes:',
        'Respuestas': ['a) Método de tanteo', 'b) Método gráfico', 'c) Método analítico', 'd) Ninguno de los anteriores'],
        'Correcta': 'b'
    },
    {
        'Pregunta': '3° Es lo cerca que se encuentra\n el valor real del valor medido:',
        'Respuestas': ['a) Precisión', 'b) Imprecisión', 'c) Inexactitud', 'd) Exactitud'],
        'Correcta': 'd'
    },
    {
        'Pregunta': '4° Es la diferencia entre el valor\n experimental y el valor real:',
        'Respuestas': ['a) Valor medido', 'b) Error relativo', 'c) Error absoluto', 'd) Valor absoluto'],
        'Correcta': 'c'
    },
    {
        'Pregunta': '5° Es el grado de alejamiento entre si\n a las diferentes aproximaciones a un valor verdadero. Se\n representa por medidas cuantitativas o afirmaciones cualitativas:',
        'Respuestas': ['a) Sesgo', 'b) Truncamiento', 'c) Error absoluto', 'd) Incertidumbre'],
        'Correcta': 'd'
    },
    {
        'Pregunta': '6° Este error se origina en el momento\n de realizar cortes en las cifras significativas después\n del punto decimal:',
        'Respuestas': ['a) Error absoluto', 'b) Error relativo', 'c) Error por redondeo', 'd) Error por truncamiento'],
        'Correcta': 'c'
    },
    {
        'Pregunta': '7° Es el resultado de dividir el\n error absoluto y el valor real:',
        'Respuestas': ['a) Error relativo', 'b) Valor experimental', 'c) Aproximación', 'd) Ninguno de los anteriores'],
        'Correcta': 'a'
    },
    {
        'Pregunta': '8° Las _____ proporcionan un instrumento para\n realizar operaciones más o menos complicadas,\n que no son tan accesibles al cálculo manual: ',
        'Respuestas': ['a) Computadoras', 'b) Aplicaciones', 'c) Calculadoras y reglas de cálculo', 'd) Herramientas de software'],
        'Correcta': 'b'
    },
    {
        'Pregunta': '9° Permite solucionar problemas matemáticos usando\n operaciones de aritmética menos complejas, así\n como saber diseñar métodos y poder interpretarlos',
        'Respuestas': ['a) Conocimiento lógico', 'b) Conocimiento analítico', 'c) Conocimiento físico', 'd) Conocimiento del entorno'],
        'Correcta': 'c'
    },
    {
        'Pregunta': '10° Los métodos numéricos nos permiten:',
        'Respuestas': ['a) Encontrar una solución aproximada al problema, usando algoritmos y secuencias', 'b) Pasa la carrera de ingeniería fácilmente', 'c) Copiar en un examen', 'd) Ninguna de los anteriores'],
        'Correcta': 'a'
    },
]

score = 0

for question in questions:
    os.system("cls")
    print(question['Pregunta'])
    for answer in question['Respuestas']:
        print(answer)
    user_answer = input('Ingresa la respuesta correcta: ')
    if user_answer == question['Correcta']:
        score += 1

print(score)