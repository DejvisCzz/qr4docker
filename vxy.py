import platform
import sys

# Získejte informace o operačním systému
os_platform = platform.platform()
os_version = platform.version()

# Získejte informace o verzi Pythonu
python_version = sys.version

# Uložte informace do souboru oss.txt
with open("../../PycharmProjects/qr4docker/oss.txt", "w") as file:
    file.write(f"OS: {os_platform}\n")
    file.write(f"Verze OS: {os_version}\n")
    file.write(f"Verze Pythonu: {python_version}\n")
