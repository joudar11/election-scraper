# Třetí projekt – Analýza volebních dat (Engeto Online Python Akademie)

Tento Python skript slouží k automatizovanému stažení a zpracování dat z voleb do Poslanecké sněmovny ČR 2017 na úrovni obcí. Výsledkem je CSV soubor obsahující volební výsledky včetně počtu hlasů pro jednotlivé strany.

## 🧠 Autor

**Kryštof Klika**  

## 📝 Popis

Skript `main.py` načítá:
- seznam obcí v zadaném okresu,
- jejich volební kódy (ID),
- počet registrovaných voličů, účastníků a platných hlasů,
- a počet hlasů pro jednotlivé politické strany.

Výstupem je tabulka ve formátu `.csv`, kterou lze snadno otevřít např. v Excelu nebo LibreOffice Calc.

## ▶️ Spuštění

Skript se spouští z příkazové řádky a vyžaduje **2 argumenty**:
1. URL adresa konkrétního okresu (např. `https://volby.cz/pls/ps2017nss/okres?xjazyk=CZ&xkraj=14&xnumnuts=3205`)
2. Název výstupního CSV souboru (např. `vysledky.csv`)

```bash
python main.py "URL_ADRESA_OKRESU" vysledky.csv

