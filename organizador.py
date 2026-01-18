import os
import shutil
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askdirectory


root = tk.Tk()
root.withdraw()

caminho = askdirectory(title="Selecione uma pasta para organizar")


if not caminho:
    messagebox.showwarning("Aviso", "Nenhuma pasta foi selecionada!")
    exit()

locais = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".tiff", ".bmp", ".svg", ".heic", ".ico"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".rtf", ".odt", ".pages", ".epub"],
    "Planilhas": [".xlsx", ".xls", ".csv", ".ods", ".tsv"],
    "Apresentacoes": [".pptx", ".ppt", ".odp", ".key"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".wmv", ".flv", ".webm", ".m4v"],
    "Musicas": [".mp3", ".wav", ".flac", ".m4a", ".aac", ".ogg", ".wma"],
    "Compactados": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"],
    "Executaveis": [".exe", ".msi", ".bat", ".sh", ".app", ".com", ".gadget"],
    "Desenvolvimento": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".cs", ".go", ".php", ".rb", ".json", ".xml", ".sql", ".yaml"],
    "Design_e_Edicao": [".psd", ".ai", ".xd", ".fig", ".sketch", ".cdr", ".indd", ".sketch", ".raw"],
    "Fontes": [".ttf", ".otf", ".woff", ".woff2"],
    "ISO_e_Disco": [".iso", ".vmdk", ".dmg", ".bin", ".cue"],
    "Torrents": [".torrent"],
    "CAD_e_3D": [".dwg", ".dxf", ".stl", ".obj", ".fbx", ".blend"]
}

lista_arquivos = os.listdir(caminho)

for arquivo in lista_arquivos:
    caminho_original = os.path.join(caminho, arquivo)
    
    
    if os.path.isdir(caminho_original):
        continue

    nome, extensao = os.path.splitext(arquivo)
    extensao = extensao.lower() 

    for pasta, extensoes in locais.items():
        if extensao in extensoes:
            pasta_destino = os.path.join(caminho, pasta)
            
            
            os.makedirs(pasta_destino, exist_ok=True)
            
            
            try:
                shutil.move(caminho_original, os.path.join(pasta_destino, arquivo))
            except Exception as e:
                print(f"Erro ao mover {arquivo}: {e}")
            break

messagebox.showinfo("Sucesso", "Pasta organizada com sucesso!")