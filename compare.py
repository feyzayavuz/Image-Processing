#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scipy.misc import imread
from scipy.linalg import norm
import os, sys

def normalize(arr):
    rng = arr.max()-arr.min()
    amin = arr.min()
    return (arr-amin)*255/rng

klasoryolu = "/home/feyza/Desktop/KNN/"
klasor = os.listdir(klasoryolu)
#print (klasor)
karsilastirilacak_resim = "/home/feyza/Desktop/KNN/B_3.bmp"
dosya_uzaklik_listesi = []

print("K DEGERINI GIRINIZ: ")
k = input()

for dosya in klasor:
    im1 = imread(klasoryolu + dosya)
    im2 = imread(karsilastirilacak_resim)
    im1 = normalize(im1)
    im2 = normalize(im2)
    diff = im2 - im1
    uzaklik = norm(diff.ravel(), 0) #zero norm uzaklığı deniyor, resimler arasındaki piksel farkına denk
    dosya_uzaklik = [dosya.split('_')[0], uzaklik] #liste elemanı olacak, sınıfı tutuyor
    dosya_uzaklik_listesi.append(dosya_uzaklik) #dosya adı ile uzaklığını tutan liste
dosya_uzaklik_listesi = sorted(dosya_uzaklik_listesi, key = lambda x: x[1]) #2. sütuna göre sırala küçükten büyüğe
print(dosya_uzaklik_listesi)

verisinifi_tekrarsayisi = [['A',0],['B',0],['C',0],['D',0],['E',0],['F',0],['G',0]]

for i in range(0, k):
    sinif = dosya_uzaklik_listesi[i][0]
    for eleman in dosya_uzaklik:
        if(eleman[0] == sinif):
            eleman[1] = eleman[1]+1
en_cok_bulunan_sinif = ""
en_cok_tekrar = 0
for eleman in verisinifi_tekrarsayisi:
    if(eleman[1] > en_cok_tekrar):
        en_cok_bulunan_sinif = eleman[0]
print(en_cok_bulunan_sinif)