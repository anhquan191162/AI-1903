dict1 = {
    'Ten' : 10,
    'Twenty': 20,
    'Thirty' : 30, 
}

dict2 = {
    'Thirty':30,
    'Fourty':40,
    'Fifty':50

}

dict3 = {**dict1, **dict2}
print(dict3)

sample_dict = {
    'class':{
        "student":{
            "name": "Mike",
            "mark": {
                "physics" : 70,
                "history": 80
            }
        }
    }
}

print(sample_dict['class']["student"]["mark"]["history"])


employees = ['Kelly', 'Emma']

defaults = {"designation": "Developer", 'salary': 8000}

newdict = {i :defaults for i in employees}

print(newdict)