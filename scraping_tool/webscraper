# import required library
import requests
from bs4 import BeautifulSoup
class Webscraper:
    """
    it is tool which will help you to save your time while working
    on data scraping related work
    """

    def __init__(self, url):
        self.url = url

    def request_data(self):

        try:
            response = requests.get(self.url)

            if response.status_code==200:
                print("request is successful and Response code is:",response.status_code,)
                print()
                return response

            else:
                print("request Not successful and Response code is:",response.status_code,)
                print()

            # Process the response
        except requests.Timeout as e:
            print(f"A timeout occurred: {e}")
            # Handle timeout error
        except requests.TooManyRedirects as e:
            print(f"Too many redirects: {e}")
            # Handle excessive redirects error
        except requests.ConnectionError as e:
            print(f"A connection error occurred: {e}")
            # Handle other connection errors
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            # Handle other request exceptions


    def soup_content(self):
        respons = Webscraper.request_data(self)
        soup = BeautifulSoup(respons.content, 'html.parser')
        return soup

    def soup_text(self):
        respons = Webscraper.request_data(self)
        soup1 = BeautifulSoup(respons.text, 'html.parser')
        return soup1.get_text()

    def soup_text_string(self):
        return str(Webscraper.soup_text(self))

    def soup_content_string(self):
        return str(Webscraper.soup_content(self))
