import tkinter as tk
from tkinter import filedialog, messagebox
from vigenere import vigenere_encrypt, vigenere_decrypt
from playfair import playfair_encrypt, playfair_decrypt
from hill import hill_encrypt, hill_decrypt

def upload_file():
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filename:
        with open(filename, 'r') as file:
            text = file.read()
        plaintext_entry.delete(0, tk.END)
        plaintext_entry.insert(0, text)

def encrypt():
    text = plaintext_entry.get().replace(" ", "").upper()  # Menghapus spasi dan mengubah ke huruf kapital
    key = key_entry.get()
    
    if len(key) < 12:
        messagebox.showerror("Error", "Kunci harus minimal 12 karakter!")
        return
    
    if cipher_var.get() == "Vigenere":
        result = vigenere_encrypt(text, key)
    elif cipher_var.get() == "Playfair":
        result = playfair_encrypt(text, key)
    elif cipher_var.get() == "Hill":
        key_matrix = [[2, 3], [1, 4]]  # Contoh matriks kunci 2x2
        result = hill_encrypt(text, key_matrix)
    
    result_entry.delete(0, tk.END)
    result_entry.insert(0, result)

app = tk.Tk()
app.title("Cryptography")

cipher_var = tk.StringVar(value="Vigenere")

tk.Label(app, text="Pilih Cipher:").pack()
tk.Radiobutton(app, text="Vigenere", variable=cipher_var, value="Vigenere").pack()
tk.Radiobutton(app, text="Playfair", variable=cipher_var, value="Playfair").pack()
tk.Radiobutton(app, text="Hill", variable=cipher_var, value="Hill").pack()

# Label dan entry untuk plaintext
tk.Label(app, text="Masukkan plaintext:").pack()
plaintext_entry = tk.Entry(app, width=50)
plaintext_entry.pack()

# Tombol untuk upload file
tk.Button(app, text="Upload File", command=upload_file).pack()

# Label dan entry untuk key
key_label = tk.Label(app, text="Masukkan kunci (min. 12 karakter):")
key_label.pack()
key_entry = tk.Entry(app, width=50)
key_entry.pack()

tk.Button(app, text="Enkripsi", command=encrypt).pack()
result_entry = tk.Entry(app, width=50)
result_entry.pack()
result_entry.insert(0, "Hasil enkripsi akan muncul di sini")

app.mainloop()
