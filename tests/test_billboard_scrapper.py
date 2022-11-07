from src.billboard_scrapper import scrape_chart

data = [('Mariah Carey', 'All I Want For Christmas Is You'), ('Brenda Lee', "Rockin' Around The Christmas Tree"), ('Bobby Helms', 'Jingle Bell Rock'), ('Burl Ives', 'A Holly Jolly Christmas'), ('Adele', 'Easy On Me'), ('Andy Williams', "It's The Most Wonderful Time Of The Year"), ('Wham!', 'Last Christmas'), ('Jose Feliciano', 'Feliz Navidad'), ('The Kid LAROI & Justin Bieber', 'Stay'), ('The Ronettes', 'Sleigh Ride')]

def test_scrape_chart():
    assert scrape_chart("2022-01-01")[0:10] == data