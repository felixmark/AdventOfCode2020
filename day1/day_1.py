def uwu2(owo):
    for w in range(0, len(owo)):
        for o in range(w, len(owo)):
            qt = owo[w]
            qt2 = owo[o]
            if (2020 - qt) == qt2:
                print("Found " + str(qt) + " and " + str(qt2) + " making out behind the corner.")
                return qt * qt2
    return None
    
def uwu3(owo):
    for w in range(0, len(owo)):
        for o in range(w, len(owo)):
            for n in range(o+1, len(owo)):
                qt = owo[w]
                qt2 = owo[o]
                qt3 = owo[n]
                if (2020 - qt - qt2) == qt3:
                    print("Found " + str(qt) + ", " + str(qt2) + " and " + str(qt3) + " playing DnD.")
                    return qt * qt2 * qt3
    return None
    
with open("input.txt", "r") as kissu:
    owoo = kissu.read()
    nya = list(map(int, owoo.split('\n')))
    print("Product: " + str(uwu2(nya)))
    print("Product: " + str(uwu3(nya)))
