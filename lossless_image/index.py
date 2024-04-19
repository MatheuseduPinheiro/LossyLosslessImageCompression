from PIL import Image

import matplotlib.pyplot as plt

def compress_image(input_image_path, output_image_path):
    image = Image.open(input_image_path)
    image.save(output_image_path, format='PNG')

# Defina os paths das imagens de entrada e saída para a compressão lossless
input_image_path_lossless = "lossless_image/entrada/input_image.jpg"
output_image_path_lossless = "lossless_image/saida/output_image_compressed.png"

# Comprima a imagem com compressão lossless
compress_image(input_image_path_lossless, output_image_path_lossless)

# Carregue as imagens comprimidas
input_image_lossless = Image.open(input_image_path_lossless)
output_image_lossless = Image.open(output_image_path_lossless)

# Exiba as imagens lado a lado para a compressão lossless
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(input_image_lossless)
axes[0].set_title('Imagem Original (Lossless)')
axes[0].axis('off')
axes[1].imshow(output_image_lossless)
axes[1].set_title('Imagem Comprimida (Lossless)')
axes[1].axis('off')
plt.show()
