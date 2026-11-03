from PIL import Image

def transferir_histograma(image1, image2):
    """
    Função operacional simples para redimensionar e combinar/misturar duas imagens.
    Garante que ambas tenham o mesmo tamanho para que possam ser combinadas ou comparadas.
    """
    # Garante que as imagens estão no mesmo formato e tamanho
    img1 = image1.resize((500, 500))
    img2 = image2.resize((500, 500))
    
    # Exemplo de operação: misturar as duas imagens com transparência (blend)
    # alpha=0.5 significa 50% de cada imagem
    imagem_combinada = Image.blend(img1.convert("RGB"), img2.convert("RGB"), alpha=0.5)
    
    return imagem_combinada


def colar_imagem(imagem_fundo, imagem_overlay, posicao=(0, 0)):
    """
    Cola uma imagem (overlay) sobre uma imagem de fundo numa determinada coordenada (x, y).
    """
    fundo = imagem_fundo.copy()
    fundo.paste(imagem_overlay, posicao)
    return fundo