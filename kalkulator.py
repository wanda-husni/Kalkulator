from tkinter import*

window=Tk()

def tombol_klik(item):
	global ekspresi
	ekspresi=ekspresi+str(item)
	input_teks.set(ekspresi)
	
def tombol_hapus():
	global ekspresi
	ekspresi=""
	input_teks.set("")
	
def tombol_hasil():
     global ekspresi 
     hasil = str(eval(ekspresi))
     input_teks.set(hasil)
     ekspresi = ""
     
ekspresi=""
input_teks=StringVar()

header = Frame(window, bg='red', height=30)
header.pack(side=TOP, fill=X)

label=Label(header, text="Halo ini adalah label", font=("Arial", 12))
label.pack()

label2=Label(header, text="Ahmad PPLG 1", textvariable=input_teks)
label2.pack()

footer = Frame(window, bg='green')
footer.pack(padx=3, pady=3 )

tombol_c= Button(footer, text='C', width=8, bg="black", fg="white", command=lambda:tombol_hapus())
tombol_c.grid(row=0, column=0, columnspan=2)
tombol_kali = Button(footer, text='*',bg="gray", command=lambda:tombol_klik("*"))
tombol_kali.grid(row=0, column=2)
tombol_bagi = Button(footer, text='/', bg="gray", command=lambda:tombol_klik("/"))
tombol_bagi.grid(row=0, column=3)

tombol_7= Button(footer, text='7', command=lambda:tombol_klik("7"))
tombol_7.grid(row=1, column=0)
tombol_8 = Button(footer, text='8', command=lambda:tombol_klik("8"))
tombol_8.grid(row=1, column=1)
tombol_9 = Button(footer, text='9', command=lambda:tombol_klik("9"))
tombol_9.grid(row=1, column=2)
tombol_tambah = Button(footer, text='+', bg="gray", command=lambda:tombol_klik("+"))
tombol_tambah.grid(row=1, column=3)

tombol_4= Button(footer, text='4', command=lambda:tombol_klik("4")) 
tombol_4.grid(row=2, column=0)
tombol_5 = Button(footer, text='5', command=lambda:tombol_klik("5"))
tombol_5.grid(row=2, column=1)
tombol_6 = Button(footer, text="6", command=lambda:tombol_klik("6"))
tombol_6.grid(row=2, column=2)
tombol_kurang= Button(footer, text='-', bg="gray", command=lambda:tombol_klik("-"))
tombol_kurang.grid(row=2, column=3)

tombol_1= Button(footer, text='1', command=lambda:tombol_klik("1"))
tombol_1.grid(row=3, column=0)
tombol_2 = Button(footer, text='2', command=lambda:tombol_klik("2"))
tombol_2.grid(row=3, column=1)
tombol_3 = Button(footer, text="3", command=lambda:tombol_klik("3"))
tombol_3.grid(row=3, column=2)
tombol_samadengan = Button(footer, text='=', height=4, bg="gray", command=lambda:tombol_hasil())
tombol_samadengan.grid(row=3, column=3,  rowspan=2)

tombol_0= Button(footer, text='0', width=8, command=lambda:tombol_klik("0"))
tombol_0.grid(row=4, column=0, columnspan=2)
tombol_titik = Button(footer, text='.', command=lambda:tombol_klik("."))
tombol_titik.grid(row=4, column=2)

window.mainloop()