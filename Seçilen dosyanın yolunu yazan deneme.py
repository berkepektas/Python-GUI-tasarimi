import tkinter as tk
from tkinter import filedialog

#Fonksiyon oluşturuyoruz
def dosya_sec():
    dosya_yolu=filedialog.askopenfilename(
        title="Şifrelenecek dosyayı seç",
        filetypes=[("Tüm dosyalar","*.*")]#ikinci yazılan *.* tüm dosya yolları için filtre eklemek için bunu değiştirmek lazım
    )
    if dosya_yolu:
        etiket.config(text=f"Seçilen dosya:\n{dosya_yolu}")
        #print("Seçilen dosya:",dosya_yolu)#Terminalde yaz

pencere=tk.Tk()
pencere.title("Dosya yolu seçme öreneği")
pencere.geometry("500x200")

buton=tk.Button(pencere,text="Dosya Seç",command=dosya_sec)
buton.pack(pady=20)

etiket=tk.Label(pencere,text="Henüz doya seçilmedi.")
etiket.pack(pady=10)

pencere.mainloop()