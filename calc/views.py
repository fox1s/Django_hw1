from django.shortcuts import render

import os
import json

# Create your views here.
# db_path = os.path.join('calc', 'db.json')


# def calc(request, number1, oper, number2):
#     res = 0
#     if oper == '*':
#         res = number1 * number2
#     elif oper == '+':
#         res = number1 + number2
#     elif oper == '-':
#         res = number1 - number2
#     elif oper == 'div':
#         res = number1 / number2
#
#     with open(db_path, 'w') as file:
#         json.dump({'n1': number1, 'oper': oper, 'n2': number2, 'res': res}, file)
#     with open(db_path, 'r') as file:
#         result = json.load(file)
#
#     return render(request, 'calc/calc.html', {'result': result})
