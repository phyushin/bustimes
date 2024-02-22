#!/usr/bin/env python3

from bs4 import BeautifulSoup, Tag as bs4Tag
import requests


base_url = "https://tfgm.com/public-transport/bus/stops"
sandersons_croft = "1800WK10281"


def parse_timetable(t):
    timetables = {}
    table = t
    for tr in table.find('tr'):
        if type(tr)==bs4Tag:
            bus_no = tr.find('h3', class_="bus-deps-h3")
            time = tr.find('span', class_="figure")
            print(bus_no)
            print(time)

    return timetables

def main():
    r = requests.get(f"{base_url}/{sandersons_croft}")
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.find('table')
    #,attr={'class':'departures-data'})
    times = parse_timetable(table.tbody)


if __name__ == "__main__":
    main()
