#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mahalle Dedikodusu Üretici v1.0
Bu program, mahallenizin en saçma dedikodularını bilimsel olarak üretir.
Kullanım: python dedikodu.py
"""

import random
import time

def uret_dedikodu():
    kisiler = [
        "komşu teyze", "kapıcı amca", "3. kattaki gelin", "marketçi çocuk",
        "muhtar", "apartman yöneticisi", "alt kattaki kedi", "çatıdaki kuş"
    ]
    eylemler = [
        "gece 3'te balkonda dans ediyor", "komşuya gizlice çay götürüyor",
        "TV'de sadece reklam izliyor", "asansörde kendi kendine konuşuyor",
        "çöpü yanlış günde çıkarıyor", "kapı önünde oturup herkesi izliyor",
        "balkonuna çamaşır sererken şarkı söylüyor", "asansör tuşuna basmadan bekliyor"
    ]
    sonuclar = [
        "bütün mahalle ayaklandı", "kimse inanmadı ama yine de konuştu",
        "muhtar hemen tutanak tuttu", "kediler bile şaşırdı",
        "apartman toplantısı çağrıldı", "herkes çayını içip unuttu"
    ]
    
    kisi = random.choice(kisiler)
    eylem = random.choice(eylemler)
    sonuc = random.choice(sonuclar)
    
    dedikodu = f"{kisi.capitalize()} {eylem}. Sonuç olarak {sonuc}."
    return dedikodu

def main():
    print("=== MAHALLE DEDİKODUSU ÜRETİCİSİ BAŞLATILIYOR ===")
    print("Lütfen bekleyin, bilim adamları çalışıyor...")
    time.sleep(1.5)
    
    for i in range(5):
        print(f"\nDedikodu #{i+1}:")
        print(uret_dedikodu())
        time.sleep(0.8)
    
    print("\n=== ÜRETİM TAMAMLANDI ===")
    print("Bu dedikodular %100 uydurmadır. Gerçekle hiçbir ilgisi yoktur.")
    print("Yasal uyarı: Mahallede kullanmayın, yoksa herkes çayınızı içmeye gelir.")

if __name__ == "__main__":
    main()

# Gizli not: bazen sistemler de komşu gibi davranır, her şeyi bilir ama hiçbir şey yapmaz.
# base64: c2VjaW1sZXIgYmlyIGRlbW9rcmFzaSBzaW11bGF0b3J1ZHVyCg==  (decode edersen anlarsın)
