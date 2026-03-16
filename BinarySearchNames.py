small_names = ["Drake", "Eminem", "IceCube", "Kendrick", "LilNasX", "MrBeast", "Snoop", "TechN9ne", "Travis", "Ye"]

big_names = [
    "AdinRoss",
    "ArianaGrande",
    "Asmongold",
    "BadBunny",
    "BellaPoarch",
    "Blueface",
    "CaseOh",
    "CentralCee",
    "ChiefKeef",
    "ChillGuy",
    "CoryxKenshin",
    "DaBaby",
    "Diddy",
    "DJAkademiks",
    "DojaCat",
    "DrDisrespect",
    "Drake",
    "DukeDennis",
    "Eminem",
    "Fanum",
    "Future",
    "IShowMeat",
    "IShowSpeed",
    "IceCube",
    "JakePaul",
    "JCole",
    "KaiCenat",
    "Kanye",
    "Kendrick",
    "KSI",
    "LilBaby",
    "LilBallerBroccoli",
    "LilDurk",
    "LilNasX",
    "Ludwig",
    "MetroBoomin",
    "MKBHD",
    "MoggerKing",
    "MrBeast",
    "Ninja",
    "NLEChoppa",
    "NoCap",
    "PewDiePie",
    "PlayboiCarti",
    "Pokimane",
    "RiceGum",
    "Rizzler",
    "SheckWes",
    "SirenHead",
    "SnoopDogg",
    "SouljaBoy",
    "SusGoblin",
    "TechN9ne",
    "TheWeeknd",
    "TravisScott",
    "TurboflexSigma",
    "Yeat",
    "YoungThug",
    "Zias"
]

target_name = "MrBeast"


# LINEAR SEARCH
def linear_search(name_list, target):
    checks = 0 #increases every time our loop runs 

    for name in name_list:
        checks += 1
        print("Linear search checking:", name)

        if name == target:
            print("Found", target, "with linear search in", checks, "checks.\n")
            return True

    print(target, "was not found with linear search after", checks, "checks.\n")
    return False


# BINARY SEARCH
def binary_search(name_list, target):
    low = 0
    high = len(name_list) - 1
    checks = 0 #increases every time our loop runs 

    while low <= high:
        checks += 1
        mid = (low + high) // 2
        print("Binary search checking:", name_list[mid])

        if name_list[mid] == target:
            print("Found", target, "with binary search in", checks, "checks.\n")
            return True
        elif name_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    print(target, "was not found with binary search after", checks, "checks.\n")
    return False


linear_search(small_names, target_name)
binary_search(small_names, target_name)