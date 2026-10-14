import tkinter as tk
from tkinter import filedialog, messagebox
from securecrypto import aes_utils

def encrypt():
    file = filedialog.askopenfilename()
    if not file:
        return
    pw = password_entry.get()
    if not pw:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập mật khẩu!")
        return
    key = aes_utils.encrypt_file_aes(file, pw)
    result_label.config(text=f"Key: {key}")

def decrypt():
    file = filedialog.askopenfilename()
    if not file:
        return
    pw = password_entry.get()
    if not pw:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập Key/Password để giải mã!")
        return
    try:
        out = aes_utils.decrypt_file_aes(file, pw)
        result_label.config(text=f"Output: {out}")
    except Exception as e:
        messagebox.showerror("Lỗi giải mã", str(e))

root = tk.Tk()
root.title("SecureCrypto GUI")
root.geometry("450x200")

password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=10)

tk.Button(root, text="Encrypt", command=encrypt, width=15).pack(pady=5)
tk.Button(root, text="Decrypt", command=decrypt, width=15).pack(pady=5)

result_label = tk.Label(root, text="", wraplength=400)
result_label.pack(pady=10)

if __name__ == '__main__':
    root.mainloop()
