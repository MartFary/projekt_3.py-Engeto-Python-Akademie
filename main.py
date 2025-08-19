
#projekt_3.py: třetí projekt do Engeto Online Python Akademie
#
#author: Martina Farkavcová
#email: martinafarkavcova@gmail.com

import sys
import csv
import requests
from bs4 import BeautifulSoup

def nacti_html(url):
    """Stáhne HTML stránku a vrátí BeautifulSoup."""
    try:
        odpoved = requests.get(url)
        odpoved.raise_for_status()
    except requests.exceptions.RequestException as e:
        sys.exit(f"Chyba při stahování {url}: {e}")
    return BeautifulSoup(odpoved.text, "html.parser")


def najdi_obce(hlavni_url):
    """Z hlavní stránky získáme seznam obcí (kód, název, URL detailu)."""
    soup = nacti_html(hlavni_url)
    seznam_obci = []
    zaklad = "https://www.volby.cz/pls/ps2017nss/" 

    for odkaz in soup.find_all("a", href=True):
        if odkaz.text.isdigit():  # číslo obce
            kod_obce = odkaz.text.strip()
            nazev_td = odkaz.find_parent("td").find_next_sibling("td")
            nazev_obce = nazev_td.text.strip()
            detail_url = zaklad + odkaz["href"]  
            seznam_obci.append((kod_obce, nazev_obce, detail_url))
    return seznam_obci


def ziskej_data_obce(detail_url):
    """Z detailní stránky obce získá základní údaje a hlasy pro strany."""
    soup = nacti_html(detail_url)

    registrovani = soup.find("td", {"headers": "sa2"}).text.strip()
    obalky = soup.find("td", {"headers": "sa3"}).text.strip()
    platne_hlasy = soup.find("td", {"headers": "sa6"}).text.strip()

    strany_a_hlasy = {}

    # první tabulka stran
    for td_strana, td_hlasy in zip(
        soup.find_all("td", {"headers": "t1sa1 t1sb2"}),
        soup.find_all("td", {"headers": "t1sa2 t1sb3"})
    ):
        strany_a_hlasy[td_strana.text.strip()] = td_hlasy.text.strip()

    # druhá tabulka stran
    for td_strana, td_hlasy in zip(
        soup.find_all("td", {"headers": "t2sa1 t2sb2"}),
        soup.find_all("td", {"headers": "t2sa2 t2sb3"})
    ):
        strany_a_hlasy[td_strana.text.strip()] = td_hlasy.text.strip()

    return registrovani, obalky, platne_hlasy, strany_a_hlasy


def main():
    if len(sys.argv) != 3:
        sys.exit("Zadej: <URL> <vystup.csv>")

    hlavni_url = sys.argv[1]
    vystup_csv = sys.argv[2]

    print(f"Stahuje hlavní stránku: {hlavni_url}")
    obce = najdi_obce(hlavni_url)
    print(f"Nalezeno obcí: {len(obce)}")

    vsechna_data = []
    hlavicka_stran = None

    for idx, (kod, nazev, detail_url) in enumerate(obce, 1):
        print(f"[{idx}/{len(obce)}] {kod} - {nazev}")
        registrovani, obalky, platne_hlasy, strany_a_hlasy = ziskej_data_obce(detail_url)

        if hlavicka_stran is None:
            hlavicka_stran = list(strany_a_hlasy.keys())

        jeden_radek = [kod, nazev, registrovani, obalky, platne_hlasy] + list(strany_a_hlasy.values())
        vsechna_data.append(jeden_radek)

    hlavicka = ["kód_obce", "obec", "registrovaní", "vydané_obálky", "platné_hlasy"] + hlavicka_stran
    with open(vystup_csv, "w", newline="", encoding="utf-8") as f:
        zapisovac = csv.writer(f)
        zapisovac.writerow(hlavicka)
        zapisovac.writerows(vsechna_data)

    print(f"Data uložena do: {vystup_csv}")


if __name__ == "__main__":
    main()