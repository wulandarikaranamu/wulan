#rekursif
def factorial (n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
n = 4

print("nilai adalah {}! adalah {}".format(n,factorial(n)))

#fungsi
def persegi_panjang (panjang,lebar):
    luas = panjang*lebar
    return luas
panjang = int(input("masukkan panjang :"))
lebar = int(input("masukkan lebar :"))

hasil = persegi_panjang (panjang,lebar)
print(hasil)

#linear search
nilai  = [13,15,5,6,7,92,33,100]

cari = 92

k = 0
f = len(nilai)-1

while k <= f:
    if cari == nilai[k]:
        print("nilai ditemukan pada index ke",k)
    k = k + 1


