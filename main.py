from PIL import Image, ImageDraw, ImageFont
from os import listdir

import MemeImage

def draw_text(image, imageText, font, x_axis_pos = 0, y_axis_pos = 0, rgb_text_color = (255, 255, 255), rgb_shadow_color = (0, 0, 0)):
    drawableImage = ImageDraw.Draw(image)

    # Draw the text over 4 times using the shadow color in order to create a border effect
    drawableImage.text((x_axis_pos-1, y_axis_pos), imageText, rgb_shadow_color, font=font) # Align the text slighty to left of the x axis point
    drawableImage.text((x_axis_pos+1, y_axis_pos), imageText, rgb_shadow_color, font=font) # Align the text slightly to the right of the x axis point
    drawableImage.text((x_axis_pos, y_axis_pos-1), imageText, rgb_shadow_color, font=font) # Aling the text slightly above the y axis point
    drawableImage.text((x_axis_pos, y_axis_pos+1), imageText, rgb_shadow_color, font=font) # Align the text slight below the y axis point

    # Draw the text over the shadow text
    drawableImage.text((x_axis_pos, y_axis_pos), imageText, rgb_text_color, font=font)

def get_text_position_x_axis(image_width, text_width):
    x_axis_position = (image_width / 2) - (text_width / 2)
    return x_axis_position

def split_text_into_lines(image, text, font):
    lines = []
    words = text.split(' ')
    i = 0

    while i < len(words):
        line = ''
        while i < len(words) and font.getsize(line + words[i])[0] <= image.size[0]:
            line = line + words[i] + " "
            i += 1
        if not line:
            line = words[i]
            i += 1
        lines.append(line)
    return lines

def get_font_size(image):
    # Based on experience the best case is for font size to cover 7% of the picture 
    PERCENTAGE_OF_FONT_SIZE = 0.07
    return int(PERCENTAGE_OF_FONT_SIZE * image.size[0])

def add_text_to_image(image, text, font):
    # Get width property of image
    image_width = image.size[0]
    # Find the width of the text in pixels
    text_width = font.getsize(text)[0]

    if image_width > text_width:
        image_center = get_text_position_x_axis(image_width, text_width)
        draw_text(image, text, font, image_center)
    else:
        y_axis = 0
        lines = split_text_into_lines(image, text, font)
        image_center = get_text_position_x_axis(image_width, font.getsize(lines[0])[0])
        for line in lines:
            draw_text(image, line, font, image_center, y_axis)
            y_axis += font.getsize(text)[1]

def add_text_to_panel(image, text, font):
    right_half = image.size[0] / 2
    lower_half = image.size[1] / 2

