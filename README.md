# 3. projekt do Python akademie

## O co jde?
Jedná se o 3. projekt k certifikaci v Python kurzu. Program scrapuje výsledky voleb do Poslanecké sněmovny Parlamentu České republiky konané ve dnech 20.10. – 21.10.2017 a ukládá je do .csv souboru.
Program pracuje s konkrétním územním celkem, nikoliv s celou ČR.

## Knihovny
Seznam potřebných knihoven je v souboru requirements.txt. Nainstalovat je lze příkazem "pip install -r requirements.txt"

## Spuštění
Soubor je třeba spustit se dvěma argumenty - první je link, druhý je název souboru. Link musí být v uvozovkách.
Příklad (Wind10, CMD): "python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" soubor.csv"
