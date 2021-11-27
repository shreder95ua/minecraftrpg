'''       Вітаємо в коді Minecraft RPG.
Це гра Minecraft, яку всі ми так добре знаємо.
Та що якщо ми б її знали ще з дитинства? 
Особисто це ще не перший мій "рогалик" (rogue-like),
бо я пробував і раніше, навіть тоді прикольно виглядало,
але потім я отримав новий комп. Я перекинув всі файли,
все було нормально, але потім появилися проблеми:
файл "My FIRST RPG.py" так і не зберігся через
мої часті перевстановлення. Хоча... Можливо він досі
є на минулому Raspberry Pi 400? Та про нього вже всі забули,
як і я про той пайтоновський файл. Хоч потім 22 жовтня, мій
брат щось розказував про майнкрафт. І ТУТ - В МЕНЕ ПОЯВИЛАСЯ ІДЕЯ,                          #IGOTTABELIEVE!
Що якщо створити майнкрафт RPG? І я почав програмувати!
Я забув той код, що я зробив рік тому, тож довелося все робити
з початку. Сьогодні 23 жовтня 2021 рік. Мій любий щоденнику))).
                                                Сидорчук Дмитро, Shreder95ua, 10 років.
'''
verNum = 0.25
ver = "Alpha 0.25" 
altVer = "Player Ver."
#           Імпортування модулів
try: 
    from keyboard import *
except:
    try:
        import os
        os.system("pip install keyboard")
        del os
        from keyboard import *
    except:
        raise ModuleNotFoundError("ЗАВАНТАЖТЕ МОДУЛЬ KEYBOARD! (ЯКЩО ВИ ЗНАЄТЕ ЯК!)")
from dcola import *
import random
import importlib
from time import sleep as wait
try:
    from winsound import Beep
except ModuleNotFoundError:
    def Beep(a, b):
        pass
#     Початок: створення змінних, команд.
time = "noon"
chat = ""
def clear(): # Очищення
    import platform as pl
    if pl.system() == "Windows":  # Якщо у вас вінда:
        print("\n" * 100)  #        Просто вводьте
    else: #                        Інакше:
        os.system("clear") #        Очистити екран командою
    del pl
def beep(sit): #          Звуки:
    if type(sit) is int:
        Beep(sit, 250)
    elif sit == "input":
        Beep(600 + random.randint(-100, 100), 250)
    elif sit == "mapGen":
        Beep(750 + random.randint(-150, 50), 75)
    elif sit == "username":
        Beep(750 + random.randint(-20, 20), 750)
    elif sit == "error":
        Beep(750, 400)
        Beep(600, 550)
    elif sit == "nomove":
        beep("error")
        print(fg.red + "ВИ НЕ МОЖЕТЕ РУХАТИСЬ КРІЗЬ ВОДУ БЕЗ ЧОВНА!" + clean)
    elif sit == "bsod":
        beep("error")
        while True:
            Beep(600 + random.randint(-15, 15), 300)
            if random.randint(0, 15) == 7:
                print(bg.dark_red + fg.light_grey + "FATAL WINDOWS ERROR:", random.randint(10000, 99999))
            print(bg.dark_blue + fg.light_grey + "WINDOWS ERROR:", random.randint(10000, 99999))
            if random.randint(0, 30) == 15:
                print(bg.dark_grey + fg.light_grey + "Y0U 4R3 C0N!")
            if random.randint(0, 25) == 5:
                print(bg.green + fg.white + "EVERYTHINGS FINE!")
                print(clean)
                return
def chatCom():
    global chat
    print(chat)
    message = input(">")
    if not message == "":
        chat = chat + "\n " + username + ": " + message.upper()
def rw():
    wait(random.randint(1, 5) / 10)
def printl(string):
    print(string)
    wait(0.1)
def splash():
    return random.choice(splashes)
wait(0.2)
print(fg.dark_green + "       MINECRAFT " + fg.dark_blue + "RPG" + txt.italic + txt.bold + fg.red + "!" + clean)
wait(0.5)
usernames = []
while True:
    username = input(fg.dark_blue + "ВАШЕ ІМ'Я: ").upper()
    usernames.append(username.lower())
    if username == "":
        print(fg.red + "ВВЕДІТЬ ІМ'Я!" + clean)
        beep("error")
    elif usernames == ["m ", "a ", "r ", "i ", "o "]:
        import mariomusic
    elif " " in username:
        print(fg.red + "ІМ'Я НЕ ПОВИННО МАТИ ПРОБІЛІВ!" + clean)
        beep("error")
    elif len(username) > 11:
        print(fg.red + "ІМ'Я МАЄ БУТИ МЕНШЕ 12 СИМВОЛІВ!" + clean)
        beep("error")
    elif not username.isascii():
        print(fg.red + "ІМ'Я МАЄ БУТИ ASCII! (ХЄХЄ, БОЙ!))" + clean)
        beep("error")
    elif username.lower() == "con":
        beep("bsod")
    elif username.lower() == "macuser":
        mac128kMode = True
    else:
        beep("username")
        break
wait(0.75)
print(fg.dark_green + title("СТВОРЕННЯ ТЕКСТУР...", 45))
field = fg.dark_green + bg.green + "░"
rw()
print(field + clean + " ПОЛЕ")
beep(600)
rw()
field2 = fg.dark_green + bg.green + "▒"
print(field2 + clean + " ПОЛЕ №2")
beep(650)
rw()
water = bg.blue + fg.white + "/"
print(water + clean + " ВОДА")
beep(700)
rw()
snow = fg.blue + bg.white + "░"
print(snow + clean + " СНІГ")
beep(750)
rw()
sand = bg.yellow + fg.orange + "▒"
print(sand + clean + " ПІСОК")
beep(800)
rw()
woods = bg.green + fg.orange + "░"
print(woods + clean + " ЛІС")
beep(850)
rw()
printl(fg.dark_green + "ВИБЕРІТЬ КОЛІР ГРАВЦЯ:")
printl(bg.dark_blue + fg.white + "1" + clean + " " * 8 + bg.blue + fg.black + "2" + clean)
printl(bg.dark_cyan + fg.white + "3" + clean + " " * 8 + bg.cyan + fg.black + "4" + clean)
printl(bg.dark_green + fg.white + "5" + clean + " " * 8 + bg.green + fg.dark_grey + "6" + clean)
printl(bg.orange + fg.white + "7" + clean + " " * 8 + bg.yellow + fg.dark_grey + "8" + clean)
printl(bg.dark_red + fg.white + "9" + clean + " " * 8 + bg.red + fg.white + "10" + clean)
printl(bg.purple + fg.white + "11" + clean + " " * 7 + bg.pink + fg.white + "12" + clean)
printl(bg.black + fg.white + "13" + clean + " " * 7 + bg.dark_grey + fg.white + "14" + clean)
printl(bg.light_grey + fg.dark_grey + "15" + clean + " " * 7 + bg.white + fg.black + "16" + clean)
numcodes = []
for num in range(0, 17):
    numcodes.append(str(num))
while True:
    colorcode = input(">")
    if colorcode in numcodes:
        break
    print(fg.red + "ВИБЕРІТЬ ЧИСЛО ВІД 1 ДО 16!" + clean)
    beep("error")
playerColor = fg.colorcode[int(colorcode) - 1]
wait(0.75)
print(fg.dark_green + title("ГЕНЕРАЦІЯ МАПИ...", 45))
try:
    filemap = open("maps.txt", "r")
    namaps = filemap.read()
    filemap.close()
    namap = random.choice(namaps.split("n")).split("/")
except:
    print(fg.red + "НЕМОЖЛИВО ВІДКРИТИ РЕСУРС СВІТІВ! МОЖЛИВО ВИ ВИДАЛИЛИ ФАЙЛ MAPS.TXT")
    raise FileNotFoundError("НЕ ЗНАЙДЕНО ФАЙЛ MAPS.TXT!!!")
map = []
for row in range(0, len(namap)):
    map.append([])
    x = 0
    for col in namap[row]:
        col = int(col)
        row = int(row)
        if col == 1:
            if random.randint(0,1) == 0:
                map[row].append(field)
            else:
                map[row].append(field2)
        elif col == 2:
            map[row].append(water)
        elif col == 3:
            map[row].append(sand)
        elif col == 4:
            map[row].append(woods)
        elif col == 5:
            map[row].append(snow)
        beep("mapGen")
        x = x + 1
player = {"x": 5, "y": 3}
def showMap(showInst = 0):
    mapWithPlayers = []
    for row in range(0, len(map)):
        mapWithPlayers.append([])
        for col in range(0, len(map[row])):
            colt = map[row][col]
            if player["x"] == col and player["y"] == row:
                if colt == field:
                    pt = bg.green + "☻"
                elif colt == field2:
                    pt = bg.dark_green + "☻"
                elif colt == sand:
                    pt = bg.yellow + "☻"
                elif colt == water:
                    pt = bg.blue + "☺"
                mapWithPlayers[row].append(playerColor + pt)
            else:
                mapWithPlayers[row].append(colt)
    for row in range(0, len(map)):
        print(fg.dark_blue + str(row + 1) + " "  + "".join(mapWithPlayers[row]) + clean)
    wait(0.075)
    if showInst == 1:
        wait(0.1)
        print(fg.dark_green + "W - ВГОРУ, S - НАЗАД, A - ВЛІВО, S - ВПРАВО, E - ІНВЕНТАР, T - ЧАТ, V - РОЗЗИРНУТИСЯ, EXIT - ВИЙТИ З ГРИ")
        wait(0.2)
        print("ПІСЛЯ ВВОДУ НАТИСНІТЬ КЛАВІШУ ENTER")
        wait(0.2)
showMap(1)
while True:
    if is_pressed("a") or is_pressed("left"):
        if map[player["y"]][player["x"] - 1] == water:
            beep("nomove")
        elif player["x"] == 0:
            beep("nomove")
        else:
            player["x"] = player["x"] - 1
        clear()
        showMap()
    if is_pressed("s") or is_pressed("down"):
        try:
            if map[player["y"] + 1][player["x"]] == water:
                beep("nomove")
            else:
                player["y"] = player["y"] + 1
        except:
            beep("nomove")
        clear()
        showMap()
    if is_pressed("d") or is_pressed("right"):
        try:
            if map[player["y"]][player["x"] + 1] == water:
                beep("nomove")
            else:
                player["x"] = player["x"] + 1
        except IndexError:
            beep("nomove")
        clear()
        showMap()
    if is_pressed("w") or is_pressed("up"):
        if map[player["y"] - 1][player["x"]] == water:
            beep("nomove")
        elif player["y"] == 0:
            beep("nomove")
        else:
            player["y"] = player["y"] - 1
        clear()
        showMap()
        
    wait(0.1)
try:
    splf = open("splashes.txt")
    splashes = splf.read().split("\n")
except FileNotFoundError:
    splashes = ["ЙОЙ, ХТОСЬ ВИДАЛИВ СПЛЕШІ!", "ТИ ТУПАПЕ!"]
printl(bg.dark_green + fg.light_grey + title("MINECRAFT", 90))
printl(fg.yellow + splash())
printl("\n" * 5)
printl("Shreder95ua! 1986 (+35!)")