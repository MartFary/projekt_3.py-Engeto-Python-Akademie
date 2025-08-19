# Projekt 3 Python akademie - Elections Scraper

## Popis projektu
Závěrečný projekt prověří nabyté znalosti z celého kurzu. Úkolem je vytvořit scraper výsledků voleb z roku 2017, který vytáhne data přímo z webu na:  
https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ

## Instalace knihoven

Knihovny, které jsou použity v kódu, jsou uložené v souboru requirements.txt. Pro instalaci se doporučuje použít nové virtuální prostředí.

## Spuštění projektu
Spuštění souboru main.py v rámci příkazového řádku požaduje dva povinné argumenty.  
  
*python main.py "URL" "vystup.csv"*  
  
kde:  
URL = odkaz, který územní celek chcete scrapovat  
vystup.csv = jméno výstupního souboru s příponou csv

## Ukázka projektu
Výsledky volebního hlasování pro okres Nový Jičín v Moravskoslezském kraji.  
  
První argument je zadání URL adresy: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8104  
Druhý argument je jméno vytvořeného csv, v mém případě vystup_nj.csv  

Spuštění programu vypadá následovně:  
python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8104" "vystup_nj.csv"  

Výsledkem je csv soubor, který obsahuje výsledky 54 obcí, které spadají do okresu Nový Jičín.  

Celý soubor v csv formátu je k dispozici zde (vystup_nj.csv)  

Částečná ukázka výstupu:  



