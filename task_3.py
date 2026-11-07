import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)


def show_folder_structure(directory, indent=""):
    for item in directory.iterdir():
        if item.is_dir():
            print(f"{indent}{Fore.BLUE}{item.name}/")
            show_folder_structure(item, indent + "    ")
        else:
            print(f"{indent}{Fore.GREEN}{item.name}")


if len(sys.argv) < 2:
    print("укажите путь к папке")
    sys.exit()

path = Path(sys.argv[1])

if not path.exists():
    print("указанный путь не существует")
    sys.exit()

if not path.is_dir():
    print("указанный путь не является папкой")
    sys.exit()

print(Fore.BLUE + path.name)
show_folder_structure(path, "    ")


