# 📸 HEIC to TIFF Converter (Lossless)

A simple open-source tool that converts **HEIC** images to **lossless TIFF**.  
Supports selecting one or multiple files through a Windows file dialog.  
The repository includes both the Python source code and a standalone `.exe` build.

---

## ✨ Features
- Select one or many HEIC files  
- Converts all images to **uncompressed TIFF** (100% lossless)  
- Preserves original resolution and quality  
- Standalone `.exe` works **without Python**  
- Minimal and clean GUI file picker (Tkinter)

---

## 🧰 Technologies Used
- Python 3  
- Pillow  
- pillow-heif  
- Tkinter  
- PyInstaller (for packaging the `.exe`)

---

## 🐍 Running the Python Version

### 1. Install dependencies
pip install pillow pillow-heif

### 2. Run the script
python heic_to_tiff_gui.py

A file chooser window will appear where you can select your `.heic` images.

---

## 🖥️ Standalone Windows EXE

A compiled `.exe` version is available under **Releases**.  
It works on any Windows PC — **no Python installation required**.

---

## 🔧 Build the EXE Yourself
pyinstaller --onefile --noconsole heic_to_tiff_gui.py

The final executable will appear inside the `dist/` folder.

---

## 📄 License
This project is open source under the **MIT License**.
