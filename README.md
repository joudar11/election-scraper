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
code,location,registered,envelopes,valid,Ob�ansk� demokratick� strana,��d n�roda - Vlasteneck� unie,CESTA ODPOV�DN� SPOLE�NOSTI,�esk� str.soci�ln� demokrat.,Radostn� �esko,STAROSTOV� A NEZ�VISL�,Komunistick� str.�ech a Moravy,Strana zelen�ch,"ROZUMN�-stop migraci,dikt�t.EU",Strana svobodn�ch ob�an�,Blok proti islam.-Obran.domova,Ob�ansk� demokratick� aliance,�esk� pir�tsk� strana,Referendum o Evropsk� unii,TOP 09,ANO 2011,Dobr� volba 2016,SPR-Republ.str.�sl. M.Sl�dka,K�es�.demokr.unie-�s.str.lid.,�esk� strana n�rodn� soci�ln�,REALIST�,SPORTOVCI,D�lnic.str.soci�ln� spravedl.,Svob.a p�.dem.-T.Okamura (SPD),Strana Pr�v Ob�an�
506761,Alojzov,205,145,144,29,0,0,9,0,5,17,4,1,1,0,0,18
589268,Bediho��,834,527,524,51,0,0,28,1,13,123,2,2,14,1,0,34
589276,B�lovice-Lutot�n,431,279,275,13,0,0,32,0,8,40,1,0,4,0,0,30
589284,Biskupice,238,132,131,14,0,0,9,0,5,24,2,1,1,0,0,10
589292,Bohuslavice,376,236,236,20,0,0,23,0,3,22,3,4,6,0,1,17
589306,Bous�n,107,67,67,5,0,0,4,0,3,14,0,2,0,0,0,7
