import qrcode
import os

def generate_qr_code(data, filename="qrcode.png"):
    # Gera o QR code com os dados fornecidos
    qr = qrcode.make(data)
    
    # Define o diretório e o caminho do arquivo para salvar o QR code
    save_path = os.path.join("static", "qrcodes")
    os.makedirs(save_path, exist_ok=True)
    file_path = os.path.join(save_path, filename)
    
    # Salva a imagem do QR code
    qr.save(file_path)
    return file_path  # Retorna o caminho do arquivo gerado

generate_qr_code("https://triade3d.com/produto/abs-cobre-metalizado-com-glitter-1kg-triade3d/#tab-additional_information:~:text=Temperatura%20de%20Extrus%C3%A3o%20(%C2%BAC)")