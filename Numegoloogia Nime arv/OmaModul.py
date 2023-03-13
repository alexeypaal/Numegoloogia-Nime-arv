def number(nimi:str):
    tähestik = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
'j': 1, 'k': 2, 'l': 3, 'm': 4, 'n': 5, 'o': 6, 'p': 7, 'q': 8, 'r': 9,
's': 1, 't': 2, 'u': 3, 'v': 4, 'w': 5, 'x': 6, 'y': 7, 'z': 8}

    x="ru"
    for f in nimi:
        if f.isalpha():
            if f.lower() in tähestik:
                x="eng"
            number_nimi =0 
            for i in nimi:
                if f.isalpha():
                    number_nimi+=tähestik[f.lower()]

            if number_nimi > 9:
                numbrid = [int(numbri) for numbri in str(number_nimi)]
                number_nimi = sum(numbrid)

            return number_nimi
        else:
            print("Viga")
            
                
