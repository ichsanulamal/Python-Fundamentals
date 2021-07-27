import turtle

print("Selamat datang di latihan menggambar menggunakan turtle anti plagiarsime!")
q = input("Masukkan bentuk yang ingin digambar!(‘lingkaran’ atau ‘segitiga’)")

if q == "segitiga":

    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    

if q == "lingkaran":
    turtle.circle(50)

turtle.mainloop()
