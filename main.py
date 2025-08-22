import os
import sys
import requests

# Путь к интерпритатору
python_path = os.path.dirname(sys.executable)
# Версия python
python_version = sys.version


def main():
    return requests.get(url="https://google.com")


# В терминал .\main.py
print("...")
print(f"ПИТЬ К ИНТЕРПРЕТАТОРУ {python_path}. \nВЕРСИЯ {python_version}")
if __name__ == "__main__":
    print(main())
