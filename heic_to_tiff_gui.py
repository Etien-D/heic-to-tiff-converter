import os

print("Starting script...")

try:
    from tkinter import Tk, filedialog, messagebox
    from pillow_heif import register_heif_opener
    from PIL import Image
except Exception as e:
    print("Πρόβλημα στα imports:", e)
    input("Πάτα Enter για έξοδο...")
    raise

print("Imports OK")

register_heif_opener()
print("HEIF registered")

root = Tk()
root.withdraw()
print("Tk init OK")

file_paths = filedialog.askopenfilenames(
    title="Επιλογή HEIC αρχείων",
    filetypes=[("HEIC files", "*.heic"), ("All files", "*.*")]
)

print("Επιλέχθηκαν αρχεία:", file_paths)

if not file_paths:
    try:
        messagebox.showinfo("Άκυρο", "Δεν επιλέχθηκαν αρχεία.")
    except:
        print("Δεν επιλέχθηκαν αρχεία.")
    input("Πάτα Enter για έξοδο...")
    raise SystemExit

count = 0

for file_path in file_paths:
    try:
        img = Image.open(file_path)
        base, _ = os.path.splitext(file_path)
        tiff_path = base + ".tiff"
        img.save(tiff_path, format="TIFF", compression="none")
        count += 1
        print(f"OK: {file_path} → {tiff_path}")
    except Exception as e:
        try:
            messagebox.showerror("Σφάλμα", f"{file_path}\n\n{e}")
        except:
            print(f"Σφάλμα σε {file_path}:", e)

try:
    messagebox.showinfo("Τέλος", f"Μετατράπηκαν {count} αρχεία.")
except:
    print(f"Μετατράπηκαν {count} αρχεία.")

print("Done.")
input("Πάτα Enter για έξοδο...")
