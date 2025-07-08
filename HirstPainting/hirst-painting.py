import turtle as t
import colorgram 
import random

# def extract_colors(image_path, num_colors):
#     """Extract colors from an image using colorgram."""
#     colors = colorgram.extract(image_path, num_colors)
#     return [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

# rgb_colors = extract_colors('Day18\HirstPainting\hirst.webp', 30)

color_list = [(234, 225, 83), (195, 8, 69), (231, 54, 132), (194, 164, 15), (112, 178, 214), (199, 77, 15), (216, 162, 101), (34, 187, 112), (29, 104, 167), (14, 23, 64), (20, 29, 168), (212, 136, 175), (231, 224, 7), (197, 34, 130), (15, 181, 210), (231, 167, 197), (126, 189, 163), (10, 48, 29), (40, 131, 75), (141, 217, 203), (61, 22, 10), (60, 13, 27), (108, 91, 210), (235, 64, 34), (131, 217, 230), (183, 17, 9)]
marissa = t.Turtle()
marissa.speed("fastest")
t.colormode(255)

def draw_hirst_painting(rows, cols, dot_size):
    marissa.heading()
    marissa.penup()

    move_length = dot_size * 2.5
    x = -1 * round(cols/2) * move_length
    y = -1 * round(rows/2) * move_length
 
    for row in range(rows):
        marissa.goto(x, y)
        marissa.dot(dot_size, random.choice(color_list))

        y += move_length
        for col in range(cols):
            marissa.forward(move_length)
            marissa.dot(dot_size, random.choice(color_list))
    
    marissa.hideturtle()

draw_hirst_painting(12, 20, 20)

t.Screen().exitonclick()