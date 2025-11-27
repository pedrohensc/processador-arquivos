from PIL import Image
import sys

def converter_imagem(input_path, output_path):
    try:
        img = Image.open(input_path)
        img.save(output_path)
        print(f"Imagem convertida com sucesso: {output_path}")
    except Exception as e:
        print(f"Erro ao converter imagem: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python converter.py <imagem_origem> <imagem_destino>")
    else:
        converter_imagem(sys.argv[1], sys.argv[2])
import os

def verificar_arquivo(caminho):
    if not os.path.exists(caminho):
        print("❌ Arquivo não encontrado!")
        return False
    return True
