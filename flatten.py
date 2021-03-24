def duz(input_list):
    duz_list = []
    for item in input_list:
        if type(item) == type([]): #TypeError: 'int' object is not iterable hatasından sonra bu kontrolu koydum.
            duz_list.extend(duz(item)) # Extend ile eklediğimiz listeyi ilk listenin sonuna ekleyebiliriz
        else:
            duz_list.append(item)
    return duz_list
    
duz([[1,'a',['cat'],2],[[[3]],'dog'],4,5])