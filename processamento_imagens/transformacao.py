from PIL import Image

def redimensionar_imagem(image, largura, altura):
    """
    Redimensiona uma imagem mantendo ou ajustando para as dimensões especificadas (largura, altura).
    """
    return image.resize((largura, altura))


def converter_escala_cinza(image):
    """
    Converte uma imagem colorida para escala de cinzento (muito útil para pré-processamento de OCR ou documentos).
    """
    return image.convert("L")


def rotacionar_imagem(image, angulo):
    """
    Rotaciona uma imagem com base num ângulo em graus.
    """
    return image.rotate(angulo, expand=True)