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
blue_y_positions = set()

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
        blue_y_positions.add(y)

    elif color == black_color:
        number_of_black_pixels += 1
        black_pixels_positions.add((x, y))

meteors_on_lake = 0

for x, y in red_pixels_positions:
    if y in blue_y_positions:
        meteors_on_lake += 1

print(f'Number of Stars: {number_of_stars}')
print(f'Number of Meteors: {number_of_meteors}')
print(f'Number of Meteors on the Water: {meteors_on_lake}')

print(f'Number of blue pixels: {number_of_blue_pixels}')


def print_sky_dots(image, sky_dot_color):
    sky_dot_positions = []
    for y in range(image.height):
        for x in range(image.width):
            pixel_color = image.getpixel((x, y))
            if pixel_color == sky_dot_color:
                sky_dot_positions.append((x, y))

    if not sky_dot_positions:
        print("No sky dots found in the image.")
        return

    # Find the bounding box of the sky dots
    min_x = min(sky_dot_positions, key=lambda pos: pos[0])[0]
    max_x = max(sky_dot_positions, key=lambda pos: pos[0])[0]
    min_y = min(sky_dot_positions, key=lambda pos: pos[1])[1]
    max_y = max(sky_dot_positions, key=lambda pos: pos[1])[1]

    # Iterate through each position in the bounding box
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in sky_dot_positions:
                print("*", end="")
            else:
                print(" ", end="")
        print()  # Move to the next line after each row


# Example usage:
print_sky_dots(img, (255, 255, 255))
