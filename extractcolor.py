import colorgram


def get_rgb_color(image, num):
    lst = []
    for color in colorgram.extract(image, num):
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        if all(x < 245 for x in [r, g, b]):
            lst.append((r, g, b))
    return lst
