import tkinter as tk
from tkinter import ttk, messagebox

WARNA_BG = "#E8F0FE"     
WARNA_JUDUL = "#1A4D8F"     
WARNA_TEKS = "#131313"     
WARNA_SIMPAN = "#2E7D32"    
WARNA_RESET = "#F9A825"    
WARNA_KELUAR = "#C62828"    
WARNA_HASIL_BG = "#FFFFFF"

FONT_JUDUL = ("Arial", 16, "bold")
FONT_LABEL = ("Arial", 11)
FONT_TOMBOL = ("Arial", 10, "bold")

root = tk.Tk()
root.title("Formulir Identitas Mahasiswa")
root.geometry("480x560")
root.configure(bg=WARNA_BG)
root.resizable(False, False)

tk.Label(
    root, text="FORMULIR IDENTITAS MAHASISWA",
    font=FONT_JUDUL, bg=WARNA_BG, fg=WARNA_JUDUL
).pack(pady=15)

form = tk.Frame(root, bg=WARNA_BG)
form.pack(padx=20, pady=5)

tk.Label(form, text="Nama", font=FONT_LABEL, bg=WARNA_BG, fg=WARNA_TEKS)\
    .grid(row=0, column=0, sticky="w", pady=6)
nama = tk.Entry(form, width=32, font=FONT_LABEL)
nama.grid(row=0, column=1, pady=6, padx=10)

tk.Label(form, text="NIM", font=FONT_LABEL, bg=WARNA_BG, fg=WARNA_TEKS)\
    .grid(row=1, column=0, sticky="w", pady=6)
nim = tk.Entry(form, width=32, font=FONT_LABEL)
nim.grid(row=1, column=1, pady=6, padx=10)

tk.Label(form, text="Program Studi", font=FONT_LABEL, bg=WARNA_BG, fg=WARNA_TEKS)\
    .grid(row=2, column=0, sticky="w", pady=6)
prodi = ttk.Combobox(
    form,
    values=["Informatika", "Sistem Informasi", "Teknologi Informasi"],
    state="readonly",
    width=30
)
prodi.grid(row=2, column=1, pady=6, padx=10)

tk.Label(form, text="Alamat", font=FONT_LABEL, bg=WARNA_BG, fg=WARNA_TEKS)\
    .grid(row=3, column=0, sticky="nw", pady=6)
alamat = tk.Text(form, width=32, height=4, font=FONT_LABEL)
alamat.grid(row=3, column=1, pady=6, padx=10)

hasil = tk.Label(
    root, text="", font=FONT_LABEL, bg=WARNA_HASIL_BG, fg=WARNA_TEKS,
    justify="left", anchor="w", width=48, height=7,
    relief="groove", padx=8, pady=5
)
hasil.pack(pady=12)


def simpan():
    """Validasi input, lalu tampilkan hasilnya pada label."""
    v_nama = nama.get().strip()
    v_nim = nim.get().strip()
    v_prodi = prodi.get()
    v_alamat = alamat.get("1.0", tk.END).strip()

    if not v_nama or not v_nim:
        messagebox.showwarning("Validasi", "Nama dan NIM tidak boleh kosong!")
        return
    if not v_prodi:
        messagebox.showwarning("Validasi", "Silakan pilih Program Studi!")
        return

    hasil.config(
        text=f"Nama          : {v_nama}\n"
             f"NIM            : {v_nim}\n"
             f"Program Studi : {v_prodi}\n"
             f"Alamat         : {v_alamat if v_alamat else '-'}"
    )


def reset():
    """Kosongkan semua input dan label hasil."""
    nama.delete(0, tk.END)
    nim.delete(0, tk.END)
    prodi.set("")
    alamat.delete("1.0", tk.END)
    hasil.config(text="")
    nama.focus()


def keluar():
    """Konfirmasi lalu tutup aplikasi."""
    if messagebox.askyesno("Keluar", "Yakin ingin keluar dari aplikasi?"):
        root.destroy()


tombol = tk.Frame(root, bg=WARNA_BG)
tombol.pack(pady=5)

tk.Button(tombol, text="Simpan", command=simpan, width=10,
          bg=WARNA_SIMPAN, fg="white", font=FONT_TOMBOL)\
    .grid(row=0, column=0, padx=6)
tk.Button(tombol, text="Reset", command=reset, width=10,
          bg=WARNA_RESET, fg="black", font=FONT_TOMBOL)\
    .grid(row=0, column=1, padx=6)
tk.Button(tombol, text="Keluar", command=keluar, width=10,
          bg=WARNA_KELUAR, fg="white", font=FONT_TOMBOL)\
    .grid(row=0, column=2, padx=6)

root.mainloop()