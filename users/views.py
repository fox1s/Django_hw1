from django.shortcuts import render

# Create your views here.
import os
import json

db_path = os.path.join('users', 'db.json')

list1 = []


# def create_users(request, **kwargs):
#     # with open(db_path, 'r') as file:
#     #     data = json.load(file)
#
#     list1.append(kwargs)
#
#     with open(db_path, "w") as file:
#         json.dump(list1, file)
#
#     # print(new_file)
#     return render(request, 'users/create_users.html')

def create_users(request, **kwargs):
    with open(db_path, 'r') as file:
        data = json.load(file)

    data.append(kwargs)

    with open(db_path, "w") as file:
        json.dump(data, file)

    return render(request, 'users/create_users.html')
