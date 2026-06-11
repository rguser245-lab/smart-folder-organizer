import os
import shutil
import sys

sortir_folder = os.path.join(os.path.expanduser("~"), "Downloads")
jadi_gini = {
    "musik": {".mp3", ".wav", ".flac", ".m4a"},
    "video": {".mp4", ".mkv", ".avi", ".mov", ".flv", ".webm", ".3gp"},
    "zip": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "aplikasi": {".exe", ".msi", ".apk"},
    "Dokumen": {".pdf", ".docx", ".xlsx", ".txt", ".pptx", ".csv"},
    "Gambar": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".svg", ".ico"},
}
DEFAULT_FOLDER = "Lainnya"
STARTUP_BATCH_NAME = "mulai_bersihkan.bat"


def ensure_folder(path):
    os.makedirs(path, exist_ok=True)


def get_target_folder(extension):
    extension = extension.lower()
    for folder, extensions in jadi_gini.items():
        if extension in extensions:
            return folder
    return DEFAULT_FOLDER


def unique_destination(path):
    base, ext = os.path.splitext(path)
    counter = 1
    unique_path = path
    while os.path.exists(unique_path):
        unique_path = f"{base} ({counter}){ext}"
        counter += 1
    return unique_path


def sort_downloads(download_folder=sortir_folder):
    if not os.path.isdir(download_folder):
        return

    for name in os.listdir(download_folder):
        source_path = os.path.join(download_folder, name)
        
        if not os.path.isfile(source_path):
            continue

        if name == STARTUP_BATCH_NAME:
            continue

        extension = os.path.splitext(name)[1].lower()
        target_folder_name = get_target_folder(extension)
        target_folder_path = os.path.join(download_folder, target_folder_name)
        ensure_folder(target_folder_path)

        destination_path = unique_destination(os.path.join(target_folder_path, name))
        try:
            shutil.move(source_path, destination_path)
        except Exception:
            continue


def create_startup_shortcut(script_path):
    startup_dir = os.path.join(
        os.environ.get("APPDATA", ""),
        "Microsoft",
        "Windows",
        "Start Menu",
        "Programs",
        "Startup",
    )
    if not startup_dir:
        return

    ensure_folder(startup_dir)
    batch_path = os.path.join(startup_dir, STARTUP_BATCH_NAME)
    pythonw_executable = sys.executable.lower().replace("python.exe", "pythonw.exe")
    command = f'start "" "{pythonw_executable}" "{script_path}"'

    try:
        with open(batch_path, "w", encoding="utf-8") as batch_file:
            batch_file.write("@echo off\r\n")
            batch_file.write(f'{command}\r\n')
    except Exception:
        pass


def main():
    try:
        current_script_path = os.path.abspath(__file__)
        create_startup_shortcut(current_script_path)
    except Exception:
        pass

    sort_downloads()


if __name__ == "__main__":
    main()