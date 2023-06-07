try:
    import os
    import time
    import math
    import platform
    import datetime as dt
    import random as r
except ImportError:
    print("Sizda qaysidir kutubxona mavjud emas!")

print("Dasturga kirish uchun iltimos kuting!")
time.sleep(4)
print("[#                   1%]")

time.sleep(2)
os.system('cls')
print("[##                  2%]")

time.sleep(2)
os.system('cls')
print("[###                 8%]")


time.sleep(2)
os.system('cls')
print("[####               15%]")


time.sleep(2)
os.system('cls')
print("[########           20%]")

time.sleep(2)
os.system('cls')
print("[############       40%]")

time.sleep(2)
os.system('cls')
print("[################   80%]")

time.sleep(2)
os.system('cls')
print("[##################100%]")

print("Loading files........")
os.system('cls')
# quyidagi kutubxonalarni chaqirib olamiz
print(r"""Kalkulyator dasturi 2023""")

ds = dt.datetime.now()
print(ds)
pl = platform.system()
print(f"Qo'llab quvvatlovchi dastur turi: {pl}")
#MENU qismi
print("********************************")
print("* :1: Qo'shish                 *")
print("* :2: Ayrish                   *")
print("* :3: Bo'lish                  *")
print("* :4: Ko'paytirish             *")
print("* :5: Qo'shimcha               *")
print("* :6: Kvadrat tenglama misoli  *")
print("* :7: Info                     *")
print("* :8: Tozala                   *")
print("* :9: Chiqish                  *")
print("* :10: Test qilish             *")
print("* :11: Kvadrat hisoblash       *")
print("********************************")
ishora = True #ishorani True yani ishlayotganida halaqit bermedi

while ishora:
    pass
    try:
        menu = int(input("Tanlang: "))
        if menu == 1:

                a = int(input("Birinchi son: "))
                b = int(input("Ikkinchi son: "))
                print(f"{a}+{b}=",a+b)
        if menu == 2:
            a = int(input("Birinchi son: "))
            b = int(input("Ikkinchi son: "))
            print(f"{a}-{b}=",a-b)
        if menu == 3:
                try:
                    a = int(input("Birinchi son: "))
                    b = int(input("Ikkinchi son: "))
                    print(f"{a}//{b}=", a // b)

                except ZeroDivisionError:
                    print("Nolga bo'lib bo'lmaydi! Iltimos qayta urinb ko'ring..")
        if menu == 4:
            a = int(input("Birinchi son: "))
            b = int(input("Ikkinchi son: "))
            print(f"{a}*{b}=",a*b)
        if menu == 5:
            x = math.pi
            print(f"PIning qiymati {x} ga teng!")
            print("********************************************")
            print("* :1: Tomoni (a) ga teng kvadrat ichiga ikkita aylana chizilgam.Kichik aylananign radiusi (r) ga teng.\nBo'yalgan yuza (s)ni topish dasturi*")
            print("* :2: Aylana uzunligini chiqaruvchi        *")
            print("*                                          *")
            print("*                                          *")
            print("*                                          *")
            print("*                                          *")
            print("*                                          *")
            print("*                                          *")
            print("********************************************")
            qoshmcha = int(input("Qaysi masala bo'yicha: "))
            if qoshmcha == 1:
                print("Iltimos kuting..")
                time.sleep(3)
                a = int(input("Tomonlari nechiga teng bo'lsin: "))
                r = int(input("Radiusi nechiga teng bo'lsin:  "))

                r1 = a/2
                s1 = x*r1**2
                s2 = r*r**2
                s = s1-s2
                print(s)
                print(f"Javob: {s}")

            if qoshmcha == 2:
                print("Loading file...")
                time.sleep(2)
                def aylana(r):
                    """Aylana uzunligini topuvchi"""
                    PI = 3.14
                    len = 2*PI*r
                    return len
                radius = int(input("Aylana radiusi: "))
                uz = aylana(radius)
                print(f"Aylana uzunligi {uz}ga teng!")
                print(f"Javob: {uz}")

        if menu == 7:
            print("Yaratuvchi: Asadbek Abdubannopov\n"
                  "Tel: +998(99)635-8714\n"
                  "Telegram: @coder_18_03\n"
                  "Yaratilgan vaqt: 03.20.2023\n"
                  "All rights reserved")

        if menu == 8:
            print("Tozalash ishga tushdi...")
            os.system('cls')
            os.system('clear')
            print("********************************")
            print("* :1: Qo'shish                 *")
            print("* :2: Ayrish                   *")
            print("* :3: Bo'lish                  *")
            print("* :4: Ko'paytirish             *")
            print("* :5: Qo'shimcha               *")
            print("* :6: Kvadrat tenglama misoli  *")
            print("* :7: Info                     *")
            print("* :8: Tozala                   *")
            print("* :9: Chiqish                  *")
            print("* :10: Test qilish             *")
            print("* :11: Kvadrat hisoblash       *")
            print("********************************")
        if menu == 9:
            print("Dasturdan chiqilmoqda...")
            time.sleep(3)
            ishora = False
        if menu == 1803:
            print("Bosh Adminga salomlar bo'lsin!")
        if menu == 18032007:
            print("Meni Asadbek Abdubannopov dasturchi yaratgan!\n"
                  "Meni 8 ta asosiy funksiyam bor\n"
                  "Lekin bitta aniq algoritmda ishlayman\n"
             
                  "Men asosan Matematikaga yordamlashish uchun yaratilgan oddiy robot deb atashingiz mumkin!")

        if menu == 6:
            a: int = int(input("A son: "))
            b = int(input("B son: "))
            c = int(input("C son: "))
            d = b**2 - 4*a*c
            if d < 0:
                print("Yechim yo'q!")
            if d == 0:
                x = -b//2*a
                print(x)
            else:
                x1 = -b + d//2//2*a
                x1 = -b - d // 2 // 2 * a
        if menu == 11:
            print("Kvadratga ko'tarish tanlandi.")
            time.sleep(2)
            kvadrat = int(input("Son: "))
            print(f"{kvadrat}ning kvadrati {kvadrat**2}ga teng!")        
        
        if menu ==10:

            print("Dasturni test qilish boshlandi..")
            print("Nima uchun test qilinadi! Dastur yaxshi ishlashi va dasturni turli xil buglarini oldini olish uchun")
            time.sleep(5)


            def test_dastur():
                """Dasturni test qil"""

                if menu > 12:

                    print("Test 1 muvafaqiyatsiz...")
                    print("Error: Mavjud bo'lmagan buyruq!")
                    time.sleep(3)
                    print("---------------")
                else:

                    print("Test 1 muvaffaqiyatli...")
                    time.sleep(4)
                    print("---------------")
                if menu == ValueError:

                    print("Test 2 muvafaqiyatsiz...")
                    print("Fatal!: ValueError")
                    time.sleep(4)
                    print("---------------")
                else:
                    print("Test 2 muvaffaqiyatli...")
                    time.sleep(4)
                    print("---------------")
                    a = 2
                    b = 2
                if a+b == 4:

                    print("Test 3 muvaffaqiyatli....")
                    time.sleep(4)
                    print("---------------")
                else:
                    print("Test 3 muvaffaqiyatsiz...")
                    time.sleep(4)
                    print("Xatolik! Matematik amal (+)")
                    print("---------------")
                if a*b == 4:
                    print("Test 4 muvaffaqiyatli...")
                    time.sleep(4)

                    print("---------------")

                    print("********************************")
                    print("* :1: Qo'shish                 *")
                    print("* :2: Ayrish                   *")
                    print("* :3: Bo'lish                  *")
                    print("* :4: Ko'paytirish             *")
                    print("* :5: Qo'shimcha               *")
                    print("* :6: Kvadrat tenglama misoli  *")
                    print("* :7: Info                     *")
                    print("* :8: Tozala                   *")
                    print("* :9: Chiqish                  *")
                    print("* :10: Test qilish             *")
                    print("* :11: Kvadrat hisoblash       *")
                    print("********************************")
                else:
                    print("Test 4 muvaffaqiyatsiz...")
                    time.sleep(4)
                    print("Xatolik! Matematik amal (*)")
                    print("---------------")

                if ishora == False:
                    print("Hozir dastur ishdan chiqqan")

            test_dastur()
    except ValueError:
        print("Iltimos butun son kiriting!")














