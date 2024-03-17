with open('D:\\txt\s.txt', 'r') as file:

    cont = file.read()
    cont = cont.replace(',','')
    cont = cont.replace('.','')
    cont = cont.replace('?','')
    cont = cont.replace(';','')
    cont = cont.split()
    
    dict_char = {}
    for word in cont:
        if word not in dict_char:
            dict_char[word] = 1
        else:
            dict_char[word] += 1
    print(dict_char)
