arraySayi = []
dusuk = []
esit = []
yuksek = []

print("kac deger olacak : ")

deger = input()
for i in range(deger):
    print ('{0} inci deger'.format(i))
    sayi = input()
    arraySayi.append(sayi)


print arraySayi
if len(arraySayi)>1:
    pivot = arraySayi[0]
    for x in arraySayi:
        if x<pivot:
            dusuk.append(x)
        if x==pivot:
            esit.append(x)
        if x>pivot:
            yuksek.append(x)
    print(sorted(dusuk) + esit + sorted(yuksek))


