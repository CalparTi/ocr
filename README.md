
# PDF OCR Converter

This project is a Python script that converts PDF files to `.txt` using OCR (Optical Character Recognition).  
It automatically lists all PDF files in the current folder, allows the user to select one for processing, and saves the extracted text with the same name as the PDF.

---

## 🚀 Features

- Automatically lists all PDFs in the folder.
- Allows the user to select which PDF to process.
- Performs OCR on all pages.
- Saves the text as `.txt` with the same name as the PDF.
- Error handling with clear messages.
- Waits for confirmation (ENTER) before exiting.

---

## ⚙️ Dependencies

### ✅ Install Tesseract OCR

Download and install Tesseract for Windows from the official **UB Mannheim** link:

🔗 https://github.com/UB-Mannheim/tesseract/wiki

> During installation, **also select the Portuguese language**.

After installation, add the folder `C:\Program Files\Tesseract-OCR` to the system **PATH**, if necessary.

---

### ✅ Install Poppler

Download Poppler for Windows:  
🔗 https://github.com/oschwartz10612/poppler-windows/releases

**How to install:**

1. Download the latest `.zip` version.
2. Extract the contents to:  
   ```
   C:\poppler
   ```
   The structure should look like this:  
   `C:\poppler\Library\bin`  
   `C:\poppler\Library\include`  
   etc.

3. Add `C:\poppler\Library\bin` to the system **PATH**.

---

### ✅ Install Python libraries

```bash
pip install pytesseract pdf2image pillow
```

---

## 💻 How to use

1. Place the PDF files in the same folder as the script.
2. Run the script:

```bash
python ocr_script.py
```

3. Select which PDF to process by typing the corresponding number.
4. The `.txt` file will be generated in the same folder.

---

## 📦 Create Executable

Optionally, you can create a `.exe` using PyInstaller:

```bash
pip install pyinstaller
pyinstaller --onefile ocr_script.py
```

The executable will be in the `dist` folder.

---

## ❗ Notes

- Tesseract and Poppler must be installed and configured on the system.
- The script waits for you to press **ENTER** at the end to view messages or errors.

---

## 🛠️ Contributions

Contributions are welcome!  
Open an issue or submit a pull request.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
