import matplotlib.pyplot as plt
from collections import Counter

çocuk_sayısı_2 = [10, 20, 25, 36, 40, 15, 90, 10, 20, 25, 36, 40, 15, 10, 20, 25, 36, 20,
                  25, 36, 40, 20, 25, 10, 20, 25, 36, 40, 15, 10, 10, 20, 36]



çocuk_sayıcı = Counter(çocuk_sayısı_2)  #çocuk sayısı saymak için
xs = range(92)
ys = [çocuk_sayıcı[x] for x in xs]

plt.bar(xs, ys, color="Green") #Histogramı çizmek
plt.xlabel("Çocuk Sayısı")
plt.ylabel("Tekrarlama Sayısı")
plt.title("çocuk_sayısı_2 Çocuk tekrarlama Histogramı")
plt.show()



çocuk_sayısı_3 = [50, 35, 40, 48, 41, 43, 42, 10, 52,  0, 29, 29, 50, 15,  8, 68,
       69, 27, 80, 10, 20, 69, 57, 28, 63, 32, 66, 75, 78, 37, 41, 79, 36,
       67, 45, 16, 65, 57, 55, 78, 41, 53, 26, 50, 79,  6, 69, 32, 53, 52,
       13, 41, 54, 66, 48, 15, 56, 32,  5, 19, 29, 72, 61, 15,  5, 17, 19,
       67, 47, 27, 24, 15, 45, 75, 25, 79, 77, 78,  4, 60, 22, 77, 50, 62,
        0, 47, 66, 61, 55, 30, 10, 12, 47, 24, 45, 67, 25, 64, 13, 22, 44,
       30, 35, 61, 55, 59, 47, 32, 75, 31, 65, 21, 24, 52, 64, 43, 45,  6,
       16, 36, 73, 70, 32, 28, 24, 37, 53, 70, 60, 79, 74, 47, 28, 11,
       38, 19, 16, 54, 59, 19, 32,  0, 11, 63, 50, 48, 78, 61, 27, 15,  3,
       25, 37, 10, 45, 47,  7,  1, 35, 22, 26, 60,  7, 33, 12, 17, 14, 71,
       43, 77, 33, 33, 73, 26,  4, 14, 63,  2, 33, 20, 14, 31,  4, 24, 77,
       56, 10, 44, 31, 27, 54, 31,  3, 12, 39, 73, 32, 11, 38, 12,  8,  3,
       30, 73, 63, 44,  8, 70, 24, 67, 25, 74, 57, 24, 12, 33, 32, 36, 59,
        7, 14, 74,  0,  4, 65, 27, 75,  4,  1, 41, 52, 10, 69, 67, 22, 50,
       24, 10, 41, 53, 47, 14, 59, 41, 25, 23, 69, 47, 65, 53, 17, 55, 47,
       72, 35, 14, 31, 45, 66, 36, 31, 64, 32, 63, 56, 40, 13, 27, 36, 68,
       26, 23, 42,  2, 35, 23,  2, 66, 27, 22, 71, 73, 29, 73,  6, 59, 42,
        6, 70, 67, 74, 54, 54,  9, 31, 57, 45, 79, 36, 36, 29, 77, 78,
       62, 79, 28, 57, 14, 55, 21, 22, 50, 61, 29, 68, 12, 73, 38, 40, 13,
       32, 28, 51,  4, 20, 48, 21, 30, 31, 75, 20, 12,  5, 41, 78, 40, 31,
       40, 51, 24, 48, 62, 37, 44, 59, 51, 35, 62, 28, 48, 71,  7, 62, 57,
       29, 22, 26, 47, 19, 15, 67, 67, 16, 62, 63,  2, 25, 44,  2, 40,
       11, 47, 13,  8,  5, 40,  3, 59, 53,  8, 52,  7,  1, 60, 17, 43, 14,
       55, 39, 64, 32, 74,  8, 24,  9, 21, 83, 80, 47, 47]



çocuk_sayıcı = Counter(çocuk_sayısı_3)  #çocuk sayısı saymak için
xs = range(92)
ys = [çocuk_sayıcı[x] for x in xs]

plt.bar(xs, ys, color="Red") #Histogramı çizmek
plt.xlabel("Çocuk Sayısı")
plt.ylabel("Tekrarlama Sayısı")
plt.title("çocuk_sayısı_3 Çocuk tekrarlama Histogramı")
plt.show()

print("Listenin toplam eleman sayısı: ",len(çocuk_sayısı_3))
print("listedeki en küçük eleman: ", min(çocuk_sayısı_3))
print("listedeki en büyük eleman: ", max(çocuk_sayısı_3))
print("Listedeki en çok tekrarlanan eleman: ", çocuk_sayıcı.most_common(1)[0][0])
print("Listedeki en az tekrarlanan eleman: ", min(çocuk_sayıcı, key=çocuk_sayıcı.get))



def Oratlama_bulma(x):
    return sum(x) / len(x)

def Ortanci_eleman(x):
    n = len(x)
    sirali =  sorted(x)
    print(sirali[1])
    ortanokta = n /2
    print(ortanokta)

    if n % 2 == 1 :
        return sirali[int(ortanokta)]
    else:
        nokta1 = ortanokta-1
        nokta2 = ortanokta

        return (sirali[int(nokta1)] + sirali[int(nokta2)]) / 2

print("mean", Oratlama_bulma(çocuk_sayısı_3))
print("ortancı", Ortanci_eleman(çocuk_sayısı_2))
