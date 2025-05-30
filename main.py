import os
import sys
from pdf2image import convert_from_path
import pytesseract

def main():
    try:
        # Configurações do caminho
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        poppler_path = r'C:\poppler\Library\bin'

        # Listar todos os PDFs na pasta atual
        pdf_files = [f for f in os.listdir() if f.lower().endswith('.pdf')]

        if not pdf_files:
            print("Nenhum arquivo PDF encontrado na pasta.")
            return  # Sai da função, sem erro

        # Mostrar lista de PDFs
        print("Arquivos PDF encontrados:")
        for idx, pdf in enumerate(pdf_files, start=1):
            print(f"{idx}. {pdf}")

        # Escolher o arquivo
        choice = input("Digite o número do PDF que deseja processar: ")

        try:
            choice_idx = int(choice) - 1
            pdf_file = pdf_files[choice_idx]
        except (ValueError, IndexError):
            print("Escolha inválida.")
            return  # Sai da função, sem erro

        # Processamento
        pages = convert_from_path(pdf_file, dpi=300, poppler_path=poppler_path)

        ocr_text = ""
        for page in pages:
            text = pytesseract.image_to_string(page, lang='por')
            ocr_text += text + "\n\n"

        # Nome do arquivo de saída
        output_file = os.path.splitext(pdf_file)[0] + '.txt'

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(ocr_text)

        print(f"OCR concluído e salvo como {output_file}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    finally:
        input("Aperte ENTER para sair...")

if __name__ == '__main__':
    main()
