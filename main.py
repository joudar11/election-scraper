"""
main.py: třetí projekt do Engeto Online Python Akademie

author: Kryštof Klika
email: krystofklika@pm.me
"""

import sys
import csv
import requests
import bs4

def fetch_soup(link) -> bs4:
    """Pomocí chňapače vrací htmlko v beautifulsoup objektu"""
    chnapac = requests.get(link)
    polevka = bs4.BeautifulSoup(chnapac.text, "html.parser")
    return polevka

def fetch_towns(link) -> list:
    """vrací seznam obcí v okresu"""
    obce = []
    obce_hledac = fetch_soup(link).find_all("td", "overflow_name")
    for o in obce_hledac:
        obce.append(o.text)
    return obce

def fetch_link(link) -> list:
    """vrací list url adres obcí v okresu"""
    urls = []
    url_hledac = fetch_soup(link).find_all("td", "cislo", "href")
    for link_obec in url_hledac:
        link_obec_insert = link_obec.a["href"]
        urls.append(f"https://volby.cz/pls/ps2017nss/{link_obec_insert}")
    return urls

def fetch_ids(link) -> list:
    """Vrací list idček obcí v okresu"""
    ids = []
    idcka = fetch_soup(link).find_all("td", "cislo")
    for i in idcka:
        ids.append(i.text)
    return ids

def fetch_voters(link):
    """fce vkládá data do globálních proměnných pro použití při zápisu do tabulky"""
    urls = fetch_link(link)
    for url in urls:
        html = bs4.BeautifulSoup(requests.get(url).text, "html.parser")
        voters_local = html.find_all("td", headers="sa2")
        for voter in voters_local:
            voter = voter.text
            voters.append(voter.replace('\xa0', ' '))
        turnouts = html.find_all("td", headers="sa3")
        for turnout in turnouts:
            turnout = turnout.text
            voter_turnout.append(turnout.replace('\xa0', ' '))
        valids = html.find_all("td", headers="sa6")
        for valid in valids:
            valid = valid.text
            valid_votes.append(valid.replace('\xa0', ' '))

def fetch_votes(link) -> list:
    """vrací list listů s  výsledky stran v každé obci"""
    links = fetch_link(link)
    votes = []
    for url in links:
        votes_chnapac = fetch_soup(url).find_all("td", "cislo", headers=["t1sa2 t1sb3", "t2sa2 t2sb3"])
        hlasy = []
        for vote in votes_chnapac:
            hlasy.append(vote.text)
        votes.append(hlasy)
    return votes

def fetch_parties(link) -> list:
    """vrací seznam stranv okresu"""
    parties = []
    html = requests.get(fetch_link(link)[0])
    html_obce = bs4.BeautifulSoup(html.text, "html.parser")
    parties_polevka = html_obce.find_all("td", "overflow_name")
    for party in parties_polevka:
        parties.append(party.text)
    return parties

def rows_creator(link) -> list:
    """vrací list - obsah tabulky"""
    rows = []
    fetch_voters(link)
    obce = fetch_towns(link)
    ids = fetch_ids(link)
    votes = fetch_votes(link)
    zipped = zip(ids, obce, voters, voter_turnout, valid_votes)
    temp = []
    for i, o, v, vt, vv in zipped:
        temp.append([i, o, v, vt, vv])
    zipped2 = zip(temp, votes)
    for a, b in zipped2:
        rows.append(a + b)
    return rows

def main():
    """Hlavní funkce, která volá ostatní a tvoří tabulku"""
    try:
        link = sys.argv[1]
        filename = sys.argv[2]
        if not link.startswith("http"):
            print("Neplatný link. Ukončuji se")
            quit()
        if not filename.endswith("csv"):
            print("Neplatný název souboru. Ukončuji se")
            quit()
        
        print("Budu sbírat z adresy:", link)
        print("Budu ukládat do souboru:", filename)
        print("Pracuji - tato operace může trvat několik (desítek) sekund.")

        header = ['code', 'location', 'registered', 'envelopes', 'valid']
        content = rows_creator(link)
        parties = fetch_parties(link)
        for party in parties:
            header.append(party)

        with open(filename, "w", newline="") as fi:
            f_writer = csv.writer(fi)
            f_writer.writerow(header)
            f_writer.writerows(content)

        print("Ukončuji program - operace proběhla úspěšsně")
    except IndexError:
        print("Nastala chyba - nebyl dodržen počet argumentů. URL adresa musí být uvedena v uvozovkách. Ukončuji se.")
        quit()

if __name__ == "__main__":
    voter_turnout = []
    voters = []
    valid_votes = []
    if len(sys.argv) == 3:
        main()
    else:
        print("Nastala chyba - nebyl dodržen počet argumentů. URL adresa musí být uvedena v uvozovkách. Ukončuji se.")
        quit()