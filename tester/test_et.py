import time
import the3
import maker
import sys
start = int(sys.argv[1])
stop = int(sys.argv[2])
yancilar = int(sys.argv[3])
limit = 1 if len(sys.argv) == 4 else sys.argv[4]
sadece_hata = False if len(sys.argv) < 6 else True
sayac = int(0)
if limit == "sonsuz": limit = 999999999999999999
limit = int(limit)

while sayac < limit:
    sayac += 1
    for i in range(start,stop):
        start_time = time.time()
        a = maker.design(i,yancilar)
        b = the3.place_words(a[0])
        if (b==a[1] or b==a[2]) == True:
            if sadece_hata == False:
                print i,"elemanli islem. dogru yaptik mi = ", b==a[1] or b==a[2]
                print("--- %s seconds ---" % (time.time() - start_time))
        else:   
            print i,"elemanli islem. dogru yaptik mi = ", b==a[1] or b==a[2]
            print("--- %s seconds ---" % (time.time() - start_time))
            print "bizim sonuc = ", b
            print "onun sonuclar = ", a[1],a[2]
            print "girdiler = ", a[0]
            print "_____________________________________________"
            break
            print("--- %s seconds ---" % (time.time() - start_time))
