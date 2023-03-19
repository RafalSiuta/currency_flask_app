from bs4 import BeautifulSoup
import requests
import datetime


class Scrapper:

    def __init__(self):
        self.data = "https://www.nbp.pl/home.aspx?f=/kursy/kursya.html"

    # def get_flags(self):
    #     data = "https://www.flagi-panstw.pl/rejestr"
    #     res = requests.get(data)
    #     soup = BeautifulSoup(res.text, "html.parser")
    #     flag_container = soup.find(name='ul', attrs={'class': 'flag-grid'})
    #     rows = flag_container.find_all('li')
    #     print(len(rows))
    #     flags = []
    #
    #     for row in rows:
    #         dict = {
    #             "name": row.find(name="span",).text,
    #             "img": "static/flags/af.png" #row.find(name="img",).text  # attrs={'type': 'image/png', }).get('srcset') #.split('.png,')[1]
    #         }
    #         print(dict)
    #         flags.append(dict)
    #     return flags

    def get_data(self):

        flags = [
            {
                "country_name": "Tajlandia",
                "value_name": "bat",
                "qty": 1,
                "symbol": "THB",
                "flag_img": "static/flags/th.png",
                # "currency_value": []
            },
            {
                "country_name": "USA",
                "value_name": "dolar",
                "qty": 1,
                "symbol": "USD",
                "flag_img": "static/flags/us.png",
                # "currency_value": []
            },
            {
                "country_name": "Australia",
                "value_name": "dolar",
                "qty": 1,
                "symbol": "AUD",
                "flag_img": "static/flags/au.png",
                # "currency_value": []
            },
            {
                "country_name": "Hongkong \n(dolar Hongkongu)",
                "value_name": "dolar",
                "qty": 1,
                "symbol": "HKD",
                "flag_img": "static/flags/hk.png",
                # "currency_value": []
            },
            {
                "country_name": "Kanada",
                "value_name": "dolar",
                "qty": 1,
                "symbol": "CAD",
                "flag_img": "static/flags/ca.png",
                # "currency_value": []
            },
            {
                "country_name": "Nowa Zelandia",
                "value_name": "dolar",
                "qty": 1,
                "symbol": "NZD",
                "flag_img": "static/flags/nz.png",
                # "currency_value": []
            },
            {
                "country_name": "Singapur \n(dolar Singapurski)",
                "value_name": "dolar",
                "qty": 1,
                "symbol": "SGD",
                "flag_img": "static/flags/sg.png",
                # "currency_value": []
            },
            {
                "country_name": "euro",
                "value_name": "euro",
                "qty": 1,
                "symbol": "EUR",
                "flag_img": "static/flags/eu.png",
                # "currency_value": []
            },
            {
                "country_name": "Węgry",
                "value_name": "forint",
                "qty": 1,
                "symbol": "HUF",
                "flag_img": "static/flags/hu.png",
                # "currency_value": []
            },
            {
                "country_name": "Szwajcaria",
                "value_name": "frank",
                "qty": 1,
                "symbol": "CHF",
                "flag_img": "static/flags/ch.png",
                # "currency_value": []
            },
            {
                "country_name": "Wielka Brytania",
                "value_name": "funt szterling",
                "qty": 1,
                "symbol": "GBP",
                "flag_img": "static/flags/gb.png",
                # "currency_value": []
            },
            {
                "country_name": "Ukraina",
                "value_name": "hrywna",
                "qty": 1,
                "symbol": "UAH",
                "flag_img": "static/flags/ua.png",
                # "currency_value": []
            },
            {
                "country_name": "Japonia",
                "value_name": "jen",
                "qty": 100,
                "symbol": "JPY",
                "flag_img": "static/flags/jp.png",
                # "currency_value": []
            },
            {
                "country_name": "Czechy",
                "value_name": "korona",
                "qty": 1,
                "symbol": "CZK",
                "flag_img": "static/flags/cz.png",
                # "currency_value": []
            },
            {
                "country_name": "Dania",
                "value_name": "korona",
                "qty": 1,
                "symbol": "DKK",
                "flag_img": "static/flags/dk.png",
                # "currency_value": []
            },
            {
                "country_name": "Islandia",
                "value_name": "korona",
                "qty": 100,
                "symbol": "ISK",
                "flag_img": "static/flags/is.png",
                # "currency_value": []
            },
            {
                "country_name": "Norwegia",
                "value_name": "korona",
                "qty": 1,
                "symbol": "NOK",
                "flag_img": "static/flags/no.png",
                # "currency_value": []
            },
            {
                "country_name": "Szwecja",
                "value_name": "korona",
                "qty": 1,
                "symbol": "SEK",
                "flag_img": "static/flags/se.png",
                # "currency_value": []
            },
            {
                "country_name": "Chorwacja",
                "value_name": "kuna",
                "qty": 1,
                "symbol": "HRK",
                "flag_img": "static/flags/hr.png",
                # "currency_value": []
            },
            {
                "country_name": "Rumunia",
                "value_name": "lej",
                "qty": 1,
                "symbol": "RON",
                "flag_img": "static/flags/ro.png",
                # "currency_value": []
            },
            {
                "country_name": "Bułgaria",
                "value_name": "lew",
                "qty": 1,
                "symbol": "BGN",
                "flag_img": "static/flags/bg.png",
                # "currency_value": []
            },
            {
                "country_name": "Turcja",
                "value_name": "lira",
                "qty": 1,
                "symbol": "TRY",
                "flag_img": "static/flags/tr.png",
                # "currency_value": []
            },
            {
                "country_name": "Izrael",
                "value_name": "szekel",
                "qty": 1,
                "symbol": "ILS",
                "flag_img": "static/flags/il.png",
                # "currency_value": []
            },
            {
                "country_name": "Chile",
                "value_name": "peso",
                "qty": 100,
                "symbol": "CLP",
                "flag_img": "static/flags/cl.png",
                # "currency_value": []
            },
            {
                "country_name": "Filipiny",
                "value_name": "peso",
                "qty": 1,
                "symbol": "PHP",
                "flag_img": "static/flags/ph.png",
                # "currency_value": []
            },
            {
                "country_name": "Meksyk",
                "value_name": "peso",
                "qty": 1,
                "symbol": "MXN",
                "flag_img": "static/flags/mx.png",
                # "currency_value": []
            },
            {
                "country_name": "RPA",
                "value_name": "rand",
                "qty": 1,
                "symbol": "ZAR",
                "flag_img": "static/flags/za.png",
                # "currency_value": []
            },
            {
                "country_name": "Brazylia",
                "value_name": "real",
                "qty": 1,
                "symbol": "BRL",
                "flag_img": "static/flags/br.png",
                # "currency_value": []
            },
            {
                "country_name": "Malezja",
                "value_name": "ringgit",
                "qty": 1,
                "symbol": "MYR",
                "flag_img": "static/flags/my.png",
                # "currency_value": []
            },
            {
                "country_name": "Indonezja",
                "value_name": "rupia",
                "qty": 10000,
                "symbol": "IDR",
                "flag_img": "static/flags/id.png",
                # "currency_value": []
            },
            {
                "country_name": "Indie",
                "value_name": "rupia",
                "qty": 100,
                "symbol": "INR",
                "flag_img": "static/flags/in.png",
                # "currency_value": []
            },
            {
                "country_name": "Korea Południowa",
                "value_name": "won",
                "qty": 100,
                "symbol": "KRW",
                "flag_img": "static/flags/kr.png",
                # "currency_value": []
            },
            {
                "country_name": "Chiny",
                "value_name": "yuan",
                "qty": 1,
                "symbol": "CNY",
                "flag_img": "static/flags/cn.png",
                # "currency_value": []
            },
            {
                "country_name": "SDR (MFW)",
                "value_name": "SDR",
                "qty": 1,
                "symbol": "XDR",
                "flag_img": "static/flags/pl.png",
                # "currency_value": []
            },
        ]
        print(len(flags))

        return flags

    def get_nbp_values(self):
        res = requests.get(self.data)
        soup = BeautifulSoup(res.text, "html.parser")
        table = soup.find(name='table', attrs={'class': 'nbptable'})
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')
        date = datetime.datetime.now().strftime("%a %d %b %y")
        data_list = []
        print(len(rows))
        for row in rows:
            cols = row.find_all('td')
            dict = {
                "date": date,
                "currency_name": cols[0].text,
                "symbol": cols[1].text,
                "value": cols[2].text
            }
            #print(dict)
            data_list.append(dict)

        return data_list


