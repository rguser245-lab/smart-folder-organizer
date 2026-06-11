# smart-folder-organizer(Windows)

Script Python otomatis untuk merapikan folder `Downloads` yang berantakan secara instan. Cukup jalankan sekali, file akan langsung dikelompokkan ke dalam folder khusus berdasarkan jenisnya (Musik, Video, Dokumen, Gambar, dll).

Script ini juga dilengkapi fitur **Auto-Startup**. Begitu dijalankan pertama kali, script akan otomatis berjalan di latar belakang (*background*) setiap kali PC dinyalakan, jadi kamu tidak perlu repot merapikan folder secara manual lagi.

---

## 🚀 Fitur Utama

* **Penyortiran Instan:** Mengelompokkan file secara otomatis ke folder:
  * 🎵 `musik` (.mp3, .wav, .flac, .m4a)
  * 🎬 `video` (.mp4, .mkv, .avi, .mov, dll)
  * 📦 `zip` (.zip, .rar, .7z, dll)
  * ⚙️ `aplikasi` (.exe, .msi, .apk)
  * 📄 `Dokumen` (.pdf, .docx, .xlsx, .txt, dll)
  * 🖼️ `Gambar` (.jpg, .png, .gif, .webp, dll)
  * 📁 `Lainnya` (Untuk file di luar ekstensi di atas)
* **Anti Overwrite:** Jika ada file dengan nama yang sama, script otomatis menambahkan angka di belakangnya (misal: `file (1).mp3`) agar file lama tidak terhapus.
* **Silent Background Run:** Otomatis membuat shortcut di folder Startup Windows agar script langsung berjalan tanpa memunculkan jendela hitam (*command prompt*).

---

## ⚙️ Cara Pakai & Kustomisasi (WAJIB BACA)

Sebelum menjalankan script, ada satu bagian kode yang **wajib** disesuaikan dengan jalur folder komputer kamu:

1. Buka file script Python ini menggunakan Notepad atau Text Editor lainnya.
2. Cari baris kode berikut di bagian atas (baris ke-5):
   ```python
   sortir_folder = r"C:\Users\rguse\Downloads"
