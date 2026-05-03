import random

geraten= 0
print("""
Wähle einen Schwierigkeitsgrad:

  Einfach      (1 – 10)          → E
  Mittel       (1 – 100)         → M
  Schwer       (1 – 1'000)       → S
  Sehr schwer  (1 – 1'000'000)   → U

Gib ein: E, M, S oder U
""")
s = input("Welche Schwierigkeit willst du haben? ")
smiley = [
"                -------------------------",
"          -------                           -------",
"      --------                                     --------",
"   --------                                             --------",
" --------          |   |                   |   |              --------",
" --------          |   |                   |   |              --------",
" --------                                                       --------",
" --------                    ---------                          --------",
" --------                 ----           ----                   --------",
" --------                    ---------                          --------",
" --------                                                       --------",
" --------                                                       --------",
" --------                                                       --------",
"   --------                                                 --------",
"      --------                                         --------",
"          -------                               -------",
"                -------------------------"
]
if s == "E":
    while True:
        z = random.randint(1, 10)
        g = int(input("gib eine zahl zwischen 1 und 10 ein: "))

        if z < g:
            print("Zu gross, versuche es nochmals")
            geraten = geraten + 1
        else:
            if z > g:
                print("zu klein, versuche es nochmals")
                geraten = geraten + 1
            else:
                if z == g:
                    geraten = geraten + 1
                    print("Du hast die zahl in", geraten, "versuchen erraten")
                    print(smiley)
                    break
elif s == "M":
    while True:
        z = random.randint(1, 100)
        g = int(input("gib eine zahl zwischen 1 und 100 ein: "))

        if z < g:
            print("Zu gross, versuche es nochmals")
            geraten = geraten + 1
        else:
            if z > g:
                print("zu klein, versuche es nochmals")
                geraten = geraten + 1
            else:
                if z == g:
                    geraten = geraten + 1
                    print("Du hast die zahl in", geraten, "versuchen erraten")
                    print(smiley)
                    break
elif s == "S":
    while True:
        z = random.randint(1, 1000)
        g = int(input("gib eine zahl zwischen 1 und 1'000 ein: "))

        if z < g:
            print("Zu gross, versuche es nochmals")
            geraten = geraten + 1
        else:
            if z > g:
                print("zu klein, versuche es nochmals")
                geraten = geraten + 1
            else:
                if z == g:
                    geraten = geraten + 1
                    print("Du hast die zahl in", geraten, "versuchen erraten")
                    print(smiley)
                    break
elif s == "U":
    while True:
        z = random.randint(1, 1000000)
        g = int(input("gib eine zahl zwischen 1 und 1'000'000 ein: "))

        if z < g:
            print("Zu gross, versuche es nochmals")
            geraten = geraten + 1
        else:
            if z > g:
                print("zu klein, versuche es nochmals")
                geraten = geraten + 1
            else:
                if z == g:
                    geraten = geraten + 1
                    print("Du hast die zahl in", geraten, "versuchen erraten")
                    print(smiley)
                    break
