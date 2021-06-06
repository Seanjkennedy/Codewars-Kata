#Convert A Hex String To RGB

"""When working with color values it can sometimes be useful to extract the individual red, green, and blue (RGB)
component values for a color. Implement a function that meets these requirements:

Accepts a case-insensitive hexadecimal color string as its parameter (ex. "#FF9933" or "#ff9933")
Returns an object with the structure {r: 255, g: 153, b: 51} where r, g, and b range from 0 through 255
Note: your implementation does not need to support the shorthand form of hexadecimal notation (ie "#FFF")"""

def hex_string_to_RGB(hex_string):
    return {'r': int(hex_string[1:3], 16), 'g': int(hex_string[3:5], 16), 'b': int(hex_string[5:], 16)}

def hex_string_to_RGB(hex_string):
    hex_dict = dict()
    hex_dict['r'] = int(hex_string[1:3], 16)
    hex_dict['b'] = int(hex_string[3:5], 16)
    hex_dict['g'] = int(hex_string[5:], 16)

    return hex_dict

print(hex_string_to_RGB("#FF9933"))
