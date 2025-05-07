# 3. projekt do Python akademie

## O co jde?
Jedná se o 3. projekt k certifikaci v Python kurzu. Program scrapuje výsledky voleb do Poslanecké sněmovny Parlamentu České republiky konané ve dnech 20.10. – 21.10.2017 a ukládá je do .csv souboru.
Program pracuje s konkrétním územním celkem, nikoliv s celou ČR.

## Knihovny
Seznam potřebných knihoven je vypsán v souboru requirements.txt. Nainstalovat je lze příkazem "pip install -r requirements.txt"

## Spuštění
Program je třeba spustit se dvěma argumenty - první je link, druhý je název souboru, kam se výsledky uloží. Link musí být v uvozovkách, název souboru musí být .csv.
Příklad (Win 10, CMD): "python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" soubor.csv"

## Ukázka
Průběh (Win 10, CMD):
"D:\Users\krystof\Desktop\proj3>python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" test.csv
Budu sbírat z adresy: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103
Budu ukládat do souboru: test.csv
Pracuji - tato operace může trvat několik (desítek) sekund.
Ukončuji program - operace proběhla úspěšsně"

Výsledek (část):
code,location,registered,envelopes,valid,Občanská demokratická strana,Řádd národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,ROZUMNÍ-stop migraci,diktát.EU,Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
506761,Alojzov,205,145,144,29,0,0,9,0,5,17,4,1,1,0,0,18,0,5,32,0,0,6,0,0,1,1,15,0
589268,Bedihošť,834,527,524,51,0,0,28,1,13,123,2,2,14,1,0,34,0,6,140,0,0,26,0,0,0,0,82,1
589276,Bílovice-Lutotín,431,279,275,13,0,0,32,0,8,40,1,0,4,0,0,30,0,3,83,0,0,22,0,0,0,1,38,0
589284,Biskupice,238,132,131,14,0,0,9,0,5,24,2,1,1,0,0,10,2,0,34,0,0,10,0,0,0,0,19,0
589292,Bohuslavice,376,236,236,20,0,0,23,0,3,22,3,4,6,0,1,17,0,4,53,1,1,39,0,0,3,0,36,0
589306,Bousín,107,67,67,5,0,0,4,0,3,14,0,2,0,0,0,7,0,2,10,0,0,9,0,0,0,0,11,0
