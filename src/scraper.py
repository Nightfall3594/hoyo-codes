import re
from typing import List, Literal

from bs4 import BeautifulSoup, ResultSet
import requests

from src.models import Code


class Scraper:

    @staticmethod
    def get_valid_codes() -> List[Code]:
        html = requests.get('https://honkai-star-rail.fandom.com/wiki/Redemption_Code')
        soup = BeautifulSoup(html.content, 'html.parser')

        table = soup.find('table')
        output = []

        # note: first row is skipped, because they're all titles and headers
        for row in table.find_all('tr')[1::]:
            cols = row.find_all('td')

            if re.findall(r'Valid', cols[3].text):
                code: str = cols[0].find('code').text if cols[0].find('code') else ''
                server: str = cols[1].text
                rewards: str = cols[2].text
                validity: Literal['Valid'] = re.findall(r'Valid', cols[3].text)[0]

                output.append(Code(code=code, server=server, rewards=rewards, validity=validity))

        return output


