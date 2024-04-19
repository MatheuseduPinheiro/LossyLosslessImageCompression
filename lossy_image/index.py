from PIL import Image
import matplotlib.pyplot as plt

def compress_image(input_image_path, output_image_path, quality=2):
    image = Image.open(input_image_path)
    image.save(output_image_path, quality=quality)

# Defina os path`s das imagens de entrada e saída
input_image_path = "lossy_image/entrada/input_image.jpg"
output_image_path = "lossy_image/saida/output_image_compressed.jpg"

# Comprima a imagem
compress_image(input_image_path, output_image_path)

# Carregue as imagens
input_image = Image.open(input_image_path)
output_image = Image.open(output_image_path)

# Exiba as imagens lado a lado
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(input_image)
axes[0].set_title('Imagem Original')
axes[0].axis('off')

axes[1].imshow(output_image)
axes[1].set_title('Imagem Comprimida')
axes[1].axis('off')
plt.show()
