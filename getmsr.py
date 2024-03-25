import csv
import getpass
import time

import requests
from requests.auth import HTTPBasicAuth


def get_config():
    try:
        with open('../../json/pythonProject/.venv/getmsr.cfg', 'r') as f:
            ip_address = f.readline().strip()
            return ip_address
    except FileNotFoundError:
        print("Konfigurační soubor 'getmsr.cfg' nebyl nalezen.")
        return None


def main():
    ip = get_config()
    if ip is None:
        return

    name = input("Zadejte uživatelské jméno: ")
    passwd = getpass.getpass("Zadejte heslo: ")

    while True:
        myurl = f"https://{ip}:5002/msr"
        try:
            response = requests.get(myurl, verify=False, auth=HTTPBasicAuth(name, passwd))
            response.raise_for_status()

            # Zkontrolovat typ dat
            if 'application/json' in response.headers.get('content-type', ''):
                data = response.json()
            else:
                data = response.text

            # Uložit data do CSV souboru
            with open('data.csv', 'a', newline='') as csvfile:
                fieldnames = ['Timestamp', 'CO2']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                if csvfile.tell() == 0:
                    writer.writeheader()
                if isinstance(data, list):
                    for entry in data:
                        writer.writerow({'Timestamp': entry.get('timestamp'), 'CO2': entry.get('CO2')})
                else:
                    print("Přijatá data nejsou ve správném formátu:", data)

            # Filtr na CO2 > 1500 ppm
            if isinstance(data, list):
                filtered_data = [entry for entry in data if entry.get('CO2', 0) > 1500]
                if filtered_data:
                    # Uložit filtrovaná data do CSV souboru
                    with open('filtered_data.csv', 'a', newline='') as csvfile:
                        fieldnames = ['Timestamp', 'CO2']
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        if csvfile.tell() == 0:
                            writer.writeheader()
                        for entry in filtered_data:
                            writer.writerow({'Timestamp': entry.get('timestamp'), 'CO2': entry.get('CO2')})
            else:
                print("Nelze filtrovat data, přijatá data nejsou ve správném formátu:", data)

            print("Data úspěšně načtena a uložena do CSV.")

        except Exception as e:
            print("Chyba při načítání dat:", e)

        # Počkej 2 minuty před načtením dat znovu
        time.sleep(120)


if __name__ == "__main__":
    main()


