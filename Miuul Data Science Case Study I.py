#GÖREV 1 Verilen değerlerin veri yapılarını inceleyiniz

x=8
print(type(x))
y=3.2
print(type(y))
z=4j+10
print(type(z))

#Görev 2 Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız

text="The goal is to  turn data into information,and information into insight"
for i in text:
    text.upper().split( )
print(text.upper().split())

#Görev 3 Verilen listeye aşağıdaki adımları uygulayınız.
text=["D","A","T","A","S","C","I","E","C","E"]
print(len(text)) #Adım 1: Verilen listenin eleman sayısına bakınız
print(text[0])  #Adım 2: Sıfırıncı  indeksteki elemanları çağırınız.
print(text[10])  #Adım 2 :Onuncu indeksteki elemanları çağırınız
yeni_list=text[0:4] #Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
print(yeni_list)    #Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
print(text.pop(8))  #Adım 4: Sekizinci indeksteki elemanı siliniz.
text.insert(10,"apsdasd") #Adım 5: Yeni bir eleman ekleyiniz.
print(text) # Adım 5: Yeni bir eleman ekleyiniz.
text.insert(8,"N")
print(text) # Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.

#Görev 4 Verilen sözlük yapısına aşağıdaki adımları uygulayınız

dict={"Christian":["America",18],
      "Daisy":["England",12],
      "Antonio":["Spain",22],
      "Damte":["Italy",25]}
print(dict.keys()) #Adım 1: Key değerlerine erişiniz
print(dict.values()) #Adım 2: Value'lara erişiniz
dict.update({"Daisy" :["England" ,13]}) #Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
print(dict) #Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
dict.update({"Ahmet" :["Turkey" ,24]}) #Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
print(dict) #Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
dict.pop("Antonio") # Adım 5: Antonio'yu dictionary'den siliniz.
print(dict) #Adım 5: Antonio'yu dictionary'den siliniz.

#Görev 5: Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri

l=[2,13,18,93,22]
def liste (l):
    tek=[]
    cift=[]
    for index,i in enumerate(l):
        if index %2==0:
            cift.append(index)
        else:
            tek.append(index)
        return cift,tek
liste(l)
# Görev 6 Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri
# bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de
# tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.

ogrenciler=["Ali","veli","ayşe","talat","zeynep","ece"]
müh=[]
tıp=[]
for index,i in enumerate(ogrenciler):
    if index <3:
        müh.append(i)
        print(müh)
    else:
        tıp.append(i)
        print(tıp)

        #Görev 7 Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız

        ogrenciler = ["Ali", "veli", "ayşe", "talat", "zeynep", "ece"]
        ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
        kredi = [3, 4, 2, 4]
        kontenjan = [30, 75, 150, 25]
        print(list(zip(kredi, ders_kodu, kontenjan)))

        #Görev 8: Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarıneğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedi

        kume1=set(["data","python"])
        kume2=set(["data","function","qcut","lambda","python","miuul"])
        def küme #yapılamadı
