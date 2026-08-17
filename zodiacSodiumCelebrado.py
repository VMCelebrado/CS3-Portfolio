import time

print("\033[36mInitializing...\033[0m")

for i in range(11):
    bar = "█" * i + "░" * (10 - i)
    print(f"\r\033[33m[{bar}] {i * 10}%\033[0m", end="")
    time.sleep(0.3)

print("\n")

print("======================================")
print("       🐉\033[33m CHINESE ZODIAC FINDER\033[0m 🐉")
print("======================================")

birth_year = int(input("Enter your birth year: "))

# If loop
if birth_year < 1900:
    print("\nInvalid Year, it should not be earlier than 1900")
else:
    zodiac_signs = [
        "Rat (鼠 / Shǔ)",
        "Ox (牛 / Niú)",
        "Tiger (虎 / Hǔ)",
        "Rabbit (兔 / Tù)",
        "Dragon (龙 / Lóng)",
        "Snake (蛇 / Shé)",
        "Horse (马 / Mǎ)",
        "Goat (羊 / Yáng)",
        "Monkey (猴 / Hóu)",
        "Rooster (鸡 / Jī)",
        "Dog (狗 / Gǒu)",
        "Pig (猪 / Zhū)"
    ]

    zodiac_index = (birth_year - 1900) % 12
    zodiac = zodiac_signs[zodiac_index]

    print("\n\033[36m======================================\033[0m")
    print(f"\033[33mBirth Year:\033[0m {birth_year}")
    print(f"\033[32mYour Chinese Zodiac Sign is:\033[0m \033[35m{zodiac}\033[0m")
    print("\033[36m======================================\033[0m")
    print("\033[33m✨ The zodiac cycle repeats every 12 years!\033[0m")