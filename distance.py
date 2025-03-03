import json

import requests
from bs4 import BeautifulSoup


class Distance():
    def __init__(self, departure_city, destination_city, path: str = 'config.json'):
        with open(path, 'r') as f:
            config = json.loads(f.read())

        self.departure_city = departure_city
        self.destination_city = destination_city
        self.km = self.calculate_km(config.get('distance_url'))

    def calculate_km(self,url):
        try:
            html_text = ''
            response = requests.get(url+self.departure_city+'/')
            if response.status_code == 200:
                html_text = response.text
            distance_soup = BeautifulSoup(html_text, features='html.parser')
            distances = distance_soup.find(string=self.destination_city).parent.parent
            for distance in distances:
                if "km" in distance.text.lower():
                    return distance.text
            print()
        except Exception as e:
            print(f"Exeption on getting gas distances {e}")


if __name__ == '__main__':
    path = 'config.json'
    with open(path, 'r') as f:
        config = json.loads(f.read())
    # dist = Distance("Bucuresti" ,"Iasi")
    # print(dist.km)
    # dist2 = Distance("Oradea", "Sibiu")
    # print(dist2.km)

        dist2 = Distance("Oradeadas", "Sibiu")
        print(dist2.km)
        print()