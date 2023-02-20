import random


def sontop(x=10):
    random_son = random.randint(1, x)
    print(f"Men 1 dan {x} gacha son o'yladim topa olasizmi", end='')
    qadam = 0
    while True:
        qadam+=1
        tahmin = int(input("Sonni kiriting: "))
        if tahmin < random_son:
            print("Adashdingiz, men o'ylagan son bundan kattaroq", end="")
        elif tahmin > random_son:
             print("Adashdingiz men o'ylagan son bundan kichikroq", end="")
        else:
             break
       
    print(f"Tabriklayman javob {random_son} edi, siz {qadam} ta urunish bilan topdingiz.")            
    return qadam



def sontop_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
    quyi = 0
    yuqori = x
    qadam = 0
    while True:
        qadam += 1
        if yuqori != quyi:
            tahmin = random.randint(quyi, yuqori)
        else : 
            tahmin = quyi
        javob = input(f"Siz {tahmin} sonini o'yladingiz, to'g'ri (t),"
                      f"Men o'ylagan son bundan kattaroq (+), yoki kichikroq(-)".lower())    
        if javob == '-':
            yuqori = tahmin-1
        elif javob == '+':
            quyi = tahmin+1
        else :
            break
    print(f"Men {qadam} ta tahmin bilan topdim.")
    return qadam    
        

def play(x=10):
    yana = True
    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)
        
        if taxminlar_user>taxminlar_pc:
            print(f"Men {taxminlar_pc} ta taxmin bilan topdim va Yutdim.")
        elif taxminlar_user<taxminlar_pc:
            print(f"Siz {taxminlar_user} ta taxmin bilan topdingiz va Yutdingiz.")
        else :
            print("Durrang!")
        yana = int(input("Yana o'ynaymizmi? Ha(1), Yoq(0): "))
        
play()        