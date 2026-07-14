def rgb(red=0, green=0, blue=0):
    return f'rgb({red}, {green}, {blue})'


def get_colors():
    return {
        'red': rgb(red=255),
        'green': rgb(green=255),
        'blue': rgb(blue=255),
    }
    

colors = get_colors()
colors.keys()  # dict_keys(['red', 'green', 'blue'])
colors['red']  # 'rgb(255, 0, 0)'
colors['blue'] # 'rgb(0, 0, 255)'