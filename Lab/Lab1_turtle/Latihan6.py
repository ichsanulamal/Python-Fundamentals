import turtle
import math


print("Selamat datang di latihan menggambar menggunakan turtle anti plagiarsime!")
q = input("Masukkan bentuk yang ingin digambar (lingkaran/segitiga):")
w = int(input("Masukkan panjang keliling gambar:"))
e = input("Masukkan warna gambar(gunakan bahasa inggris!):")
r = input("Apakah anda ingin memasukkan warna ke dalam gambar?(ya/tidak)")

a = w/3
b = w/3
c = w/3
d = w / 2 * math.pi


if q == "segitiga":
    if r == "ya":
        turtle.color(e)
        turtle.begin_fill()
        turtle.forward(a)
        turtle.left(120)
        turtle.forward(b)
        turtle.left(120)
        turtle.forward(c)
        turtle.end_fill()
        turtle.hideturtle()
    else:
        turtle.color(e)
        turtle.forward(a)
        turtle.left(120)
        turtle.forward(b)
        turtle.left(120)
        turtle.forward(c)
        turtle.hideturtle()


if q == "lingkaran":
    if r == "ya":
        turtle.color(e)
        turtle.begin_fill()
        turtle.circle(d)
        turtle.end_fill()
        turtle.hideturtle()
    else:
        turtle.color(e)
        turtle.circle(d)
        turtle.hideturtle()
        

turtle.penup()
turtle.goto(-200,-200)
turtle.pendown()
turtle.write("Copyright: M Ichsanul Amal, NPM:1906353454", move=False, font=("Arial", 20, "bold"))

turtle.penup()
turtle.goto(0,100)
turtle.pendown()
turtle.write("Program menggambar untuk anak", move=False, align="center",font=("Arial", 20, "bold"))


turtle.mainloop()
