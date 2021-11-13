def title(string, num):
    return string.center(num)
from platform import system as sus
if sus() == "Windows":
    from colorama import init
    init()
    from colorama import Back, Fore, Style
    clean = Style.RESET_ALL
    class txt:
        bold = ""
        italic = ""
        underline = ""
        cross = ""
    class fg:
        white = Fore.WHITE
        cyan = Fore.CYAN + Style.BRIGHT
        pink = Fore.MAGENTA + Style.BRIGHT
        blue = Fore.BLUE
        yellow = Fore.YELLOW + Style.BRIGHT
        green = Fore.GREEN + Style.BRIGHT
        red = Fore.RED + Style.BRIGHT
        dark_grey = Fore.BLACK + Style.BRIGHT
        black = Fore.BLACK
        dark_red = Fore.RED
        dark_green = Fore.GREEN
        orange = Fore.YELLOW
        dark_blue = Fore.BLUE
        purple = Fore.MAGENTA
        dark_cyan = Fore.CYAN
        light_grey = Fore.BLACK + Style.BRIGHT
        colorcode = [dark_blue, blue, dark_cyan, cyan, dark_green, green, orange, yellow, dark_red, red, purple, pink, black, dark_grey, light_grey, white]
    class bg:
        white = Back.WHITE
        cyan = Back.CYAN
        pink = Back.MAGENTA
        blue = Back.BLUE
        yellow = Back.YELLOW
        green = Back.GREEN
        red = Back.RED
        dark_grey = Back.BLACK
        black = Back.BLACK
        dark_red = Back.RED
        dark_green = Back.GREEN
        orange = Back.YELLOW
        dark_blue = Back.BLUE
        purple = Back.MAGENTA
        dark_cyan = Back.CYAN
        light_grey = Back.BLACK
        colorcode = [dark_blue, blue, dark_cyan, cyan, dark_green, green, orange, yellow, dark_red, red, purple, pink, black, dark_grey, light_grey, white]
else:
    def c(colorCode):
        return "\033[" + str(colorCode) + "m"
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
    