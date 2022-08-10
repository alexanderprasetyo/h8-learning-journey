nilai = -1
if 0 <= nilai <= 100:
    if nilai >= 80:
        print('Nilai A')
    elif nilai >= 70:
        print('Nilai B')
    elif nilai >= 60:
        print('Nilai C')
    elif nilai >= 40:
        print('Nilai D')
    elif nilai >= 0:
        print('Nilai E')
else:
    print("Nilai di luar rentang")

cities = ['Pekanbaru','Jakarta','Depok','Bandung']
kota = 'LALALA'

if kota in cities:
    print(f'kota {kota} terdapat dalam list cities')
else:
    print(f'kota {kota} tidak terdapat dalam cities')



a = 1
b = 1

while a <= 10:
    print (f'perkalian {a}')
    while b <= 10:
        print(f'{a} x {b}={a * b}')
        b = b + 1
    print ('-' * 10)
    a = a + 1
    b = 1

print (cities)