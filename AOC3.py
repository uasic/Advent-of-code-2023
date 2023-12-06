
vsota = 0

def aliJeVMatriki(matrika, i, j):
    return i >= 0 and j >= 0 and i < len(matrika) and j < len(matrika[i])

def ceJeStevilka(matrika, i, j):
    if (not aliJeVMatriki(matrika, i, j)):
        return False
    return matrika[i][j] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def ceJeSimbol(matrika, i, j):
    if (not aliJeVMatriki(matrika, i, j)):
        return False
    return (not (ceJeStevilka(matrika, i, j))) and matrika[i][j] != "."

def preveriRob(matrika, i, zacetek, konec):
    while(zacetek <= konec):
        if (ceJeSimbol(matrika, i, zacetek)):
            return True
        zacetek += 1
    return False


def imavaZacetekInKonec(matrika, i, zacetek, konec):
    global vsota
    # i = 2
    # zacetek = 2
    # konec   = 3

    aliSeDotikaSimbola = False

    # preveriva zgornjo levo dialonalo
    if (ceJeSimbol(matrika, i - 1, zacetek - 1)):
        aliSeDotikaSimbola = True

    if (ceJeSimbol(matrika, i - 1, konec + 1)):
        aliSeDotikaSimbola = True

    if (ceJeSimbol(matrika, i + 1, konec + 1)):
        aliSeDotikaSimbola = True

    if (ceJeSimbol(matrika, i + 1, zacetek - 1)):
        aliSeDotikaSimbola = True

    if (ceJeSimbol(matrika, i, zacetek - 1)):
        aliSeDotikaSimbola = True

    if (ceJeSimbol(matrika, i, konec + 1)):
        aliSeDotikaSimbola = True

    # preveriva zgornji rob
    if (preveriRob(matrika, i - 1, zacetek, konec)):
        aliSeDotikaSimbola = True
    
    # preveriva spodnji rob
    if (preveriRob(matrika, i + 1, zacetek, konec)):
        aliSeDotikaSimbola = True

    # od te tocke naprej veva, da je aliSeDotikaSimbola pravilno nastavljen
    if (aliSeDotikaSimbola == True):
        a = int("".join(matrika[i][zacetek:(konec + 1)]))
        print("nasla sva stevilko ki se dotika simbola:", a)
        vsota += a
        pass



def obdelajElement(matrika, i, j):
    if (ceJeStevilka(matrika, i, j)):
        zacetek = j
        j += 1
        konec = -1
        while(j < len(matrika[i])):
            if (ceJeStevilka(matrika, i, j)):
                konec = j
                j += 1
            else:
                break
        if (konec == -1):
            print(matrika[i][zacetek])
            konec = zacetek

        # od te tocke naprej veva, da imava pravi konec in zacetek       
        imavaZacetekInKonec(matrika, i, zacetek, konec)
        return (konec - zacetek) + 1
    return 1


def pojdiCezMatriko(matrika, funkcijo):
    i = 0
    while (i < len(matrika)):

        j = 0
        while (j < len(matrika[i])):
            j += funkcijo(matrika, i, j)

        i += 1


a = [
    ["4","6","7",".",".","1","1","4",".","."],
    [".",".",".","*",".",".",".",".",".","."],
    [".",".","3","5",".",".","6","3","3","."],
    [".",".",".",".",".",".","#",".",".","."],
    ["6","1","7","*",".",".",".",".",".","."],
    [".",".",".",".",".","+",".","5","8","."],
    [".",".","5","9","2",".",".",".",".","."],
    [".",".",".",".",".",".","7","5","5","."],
    [".",".",".","$",".","*",".",".",".","."],
    [".","6","6","4",".","5","9","8",".","."]
]

filename = "input3.1.txt"
a = []
with open(filename) as file:
    for line in file:
        vrstica = line.rstrip()
        a.append(list(vrstica))

pojdiCezMatriko(a, obdelajElement)

print(vsota)