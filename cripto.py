def encrypt_caesar(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():  # Memeriksa apakah karakter adalah huruf
            # Menghitung posisi baru dengan pergeseran
            shift_base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += new_char
        else:
            encrypted_text += char  # Menambahkan karakter non-huruf tanpa perubahan
    return encrypted_text

def decrypt_caesar(ciphertext, shift):
    return encrypt_caesar(ciphertext, -shift)  # Dekripsi dengan pergeseran negatif

# Contoh penggunaan
pesan_asli = "Hello, World!"
shift = 3

# Enkripsi
pesan_enkripsi = encrypt_caesar(pesan_asli, shift)
print("Pesan terenkripsi:", pesan_enkripsi)

# Dekripsi
pesan_dekripsi = decrypt_caesar(pesan_enkripsi, shift)
print("Pesan terdekripsi:", pesan_dekripsi)