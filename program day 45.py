i=0
while i < 30:
    i+=1
    if i % 2 ==1 :
        print(i)
print("perulangan while dengan data list")
kota=["majene","polewali","mamuju","palu","makassar"]
cari=input("masukkan kota yang anda cari :")
i=0
while i< len(kota):
    if kota[i]  == cari:
        print("anda sudah menemukan kota anda barada pada indeks",i,"yaitu kota",cari)
        break
    print("bukan:",kota[i])
    i+=1
else :
     print("anda masukkan tdk terdapat")

        

kota=["majene","polewali","mamuju","palu","makassar"]
i=0
while i < len(kota):
    i+=1
    if  i % 2 ==0:
        print("skip")
        continue
    print(i)
   
    
        


   
