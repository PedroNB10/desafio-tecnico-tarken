from PIL import Image

# Abre a imagem
img = Image.open('meteor_challenge_01.png')

# Converte para RGB se necessário
if img.mode != 'RGB':
    img = img.convert('RGB')

# Obtém os dados de cada pixel
pixels_data = img.getdata()

# Define a cor que você está procurando (em RGB)
white_color = (255, 255, 255)
red_color = (255, 0, 0)
blue_color = (0, 0, 255)
black_color = (0, 0, 0)

# Define os conjuntos para armazenar as posições dos pixels

white_pixels_positions = set()
black_pixels_positions = set()
red_pixels_positions = set()
blue_x_positions = set()

# Contadores
number_of_stars = 0
number_of_meteors = 0
number_of_black_pixels = 0
number_of_blue_pixels = 0


# Itera sobre cada pixel para verificar a cor
for i, color in enumerate(pixels_data):
    # Calcula a posição x e y baseado no índice do pixel
    y = i // img.width
    x = i % img.width

    if color == white_color:
        number_of_stars += 1
        white_pixels_positions.add((x, y))

    elif color == red_color:
        number_of_meteors += 1
        red_pixels_positions.add((x, y))

    elif color == blue_color:
        number_of_blue_pixels += 1
        blue_x_positions.add(x)

    elif color == black_color:
        number_of_black_pixels += 1
        black_pixels_positions.add((x, y))

meteors_on_lake = 0

for x, y in red_pixels_positions:

    if x in blue_x_positions:
        meteors_on_lake += 1

print(f'Number of Stars: {number_of_stars}')
print(f'Number of Meteors: {number_of_meteors}')
print(f'Number of Meteors on the Water: {meteors_on_lake}')

print(f'Number of blue pixels: {number_of_blue_pixels}')
