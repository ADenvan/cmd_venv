import os
import sys
import requests

# Путь к интерпритатору
python_path = os.path.dirname(sys.executable)
# Версия python
python_version = sys.version


def main():
    respons = requests.get(url="https://google.com")
    return respons


# В терминал .\main.py
def print_version_info(python_path, python_version):
    print("...")
    print(f"ПИТЬ К ИНТЕРПРЕТАТОРУ {python_path}. \nВЕРСИЯ {python_version}")

if __name__ == "__main__":
    print_version_info(python_path, python_version)
    main()
    
