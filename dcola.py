mac128kMode = False
def c(colorCode):
    if mac128kMode:
        if int(colorCode / 10) == 4:
            return "\033[40m"
        elif int(colorCode / 10) == 3:
            return "\033[30m"
        elif int(colorCode / 10) == 10:
            return "\033[100m"
        elif int(colorCode / 10) == 9:
            return "\033[90m"
        else:
            return "\033[" + str(colorCode) + "m"
    else:
        return "\033[" + str(colorCode) + "m"
def title(string, num):
    return string.center(num)
clean = c(0)
class txt:
    bold = c(1)
    italic = c(3)
    underline = c(4)
    cross = c(9)
class fg:
    white = c(97)
    cyan = c(96)
    pink = c(95)
    blue = c(94)
    yellow = c(93)
    green = c(92)
    red = c(91)
    dark_grey = c(90)
    black = c(30)
    dark_red = c(31)
    dark_green = c(32)
    orange = c(33)
    dark_blue = c(34)
    purple = c(35)
    dark_cyan = c(36)
    light_grey = c(37)
    colorcode = [dark_blue, blue, dark_cyan, cyan, dark_green, green, orange, yellow, dark_red, red, purple, pink, black, dark_grey, light_grey, white]
class bg:
    white = c(107)
    cyan = c(106)
    pink = c(105)
    blue = c(104)
    yellow = c(103)
    green = c(102)
    red = c(101)
    dark_grey = c(100)
    black = c(40)
    dark_red = c(41)
    dark_green = c(42)
    orange = c(43)
    dark_blue = c(44)
    purple = c(45)
    dark_cyan = c(46)
    light_grey = c(47)
    colorcode = [dark_blue, blue, dark_cyan, cyan, dark_green, green, orange, yellow, dark_red, red, purple, pink, black, dark_grey, light_grey, white]