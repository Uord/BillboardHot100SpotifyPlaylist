from bs4 import BeautifulSoup
import requests
import sys

def scrape_chart(date: str) -> list[tuple[str,str]]:
    response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")

    soup = BeautifulSoup(response.text, "html.parser")

    titles_tag = soup.select("div li ul li h3")
    titles = [titles.text.strip() for titles in titles_tag]
    artists_tag = soup.find_all("span", class_="a-no-trucate")
    artists = [artists.text.strip() for artists in artists_tag]

    return [(artist,title) for artist,title in zip(artists,titles)]

if __name__ == "__main__":
    print(scrape_chart(sys.argv[1]))
