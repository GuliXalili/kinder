gap = input("Soz kiriting: ")
lugat = {
    "apple": {
        "a": ["13 Pro Max", "1250$"],
        "b": ["Mackbook Pro 2022 M2", "1800$"],
        "c": ["Ipod touch 7", "900$"]
    },
    "huawei": {
        "d": ["Mate 30 Pro", "600$"],
        "e": ["Mate 20 X", "650$"],
        "f": ["Mate Xs", "500$"]
    },
    "artel": {
        "g": ["Artel Quadro Pro", "1250$"],
        "h": ["Mini-ovens", "250$"],
        "i": ["43H1400 Full HD", "400$"]
    }
}
tanla = input('''Apple:
              "a"-"13 Pro Max", "1250$"
              "b"-"Mackbook Pro 2022 M2", "1800$"
              "c"-Ipod touch 7", "900$
              Huawei:
              "d"-Mate 30 Pro", "600$
              "e"-Mate 20 X", "650$
              "f"-Mate Xs", "500$
              Artel:
              "g"-Artel Quadro Pro", "1250$
              "h"-"Mini-ovens", "250$"
              "i"-43H1400 Full HD", "400$
                Shulardan birini tanlang: ''')

if gap.lower() == "apple":
    # print(lugat["apple"])
    if tanla.lower() == "a":
        print(lugat["apple"]["a"])
    elif tanla.lower() == "b":
        print(lugat["apple"]["b"])
    elif tanla.lower() == "c":
        print(lugat["apple"]["c"])
    
    
elif gap.lower() == "huawei":
    # print(lugat["huawei"])
    if tanla.lower() == "d":
        print(lugat["huawei"]["d"])    
    elif tanla.lower() == "e":
        print(lugat["huawei"]["e"])
    elif tanla.lower() == "f":
        print(lugat["huawei"]["f"])

elif gap.lower() == "artel":
    # print(lugat["artel"])
    if tanla.lower() == "g":
        print(lugat["artel"]["g"])
    elif tanla.lower() == "h":
        print(lugat["artel"]["h"])    
    elif tanla.lower() == "i":
        print(lugat["artel"]["i"]) 



 




