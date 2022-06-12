from bs4 import BeautifulSoup
import requests
from time import sleep
from csv import writer

#If getting module not found error --> Go to Python packages --> search bs4 --> INSTALL IT. Next search beautifulsoup4 --> INSTALL IT. Now, Run the Program.
base_url = "http://quotes.toscrape.com"
url = "/page/1/"  #At Starting we pass page 1 url link as shown in left
all_quotes = []
while url:  #when url is none, i.e, when page ends, the while loop stops as we have executed if next button class does not exist, then do Nothing (None)
    response = requests.get(f"{base_url}{url}")
    print(f"Now Scraping {base_url}{url}... ")
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup)

    quotes_all = soup.find_all(class_="quote")

    for quote in quotes_all:
        quote_text_form = quote.find("span").get_text()
        print(f"Quote :{quote_text_form}")
        author = quote.find("small").get_text()
        print(f"Author :{author}")
        bio_link = quote.find("a")["href"]
        print(f"Bio-Link :{bio_link}")
        next_button = soup.find(class_="next")   # Can Also do this combined --> soup.find(class_="next").find("a")["href"]
        url = next_button.find("a")["href"] if next_button else None  #Check if next_button class exists if exists then execute the same line code. ie., Give me the page link, if it doesnt exists then do nothing. (None)
        # print(url)
        sleep(1)  #sleep for 1 second after every loop/request so that we dont overload the server.
        all_quotes.append([quote_text_form, author, bio_link])
print(all_quotes)

#Writing CSV File :
with open("quotes.csv", "w") as file:  #Will create a new file, if not exists, otherwise, overwrite the file if exists.
    csv_writer = writer(file)
    csv_writer.writerow(["Quote","Author", "Bio-Link"])
    for quote_data in all_quotes:
        try:
            csv_writer.writerow(quote_data)  #Iterating List of all_quotes one by one and writing it to csv.
        except UnicodeEncodeError as e:   #Since getting an error so raised an exception.
            csv_writer.writerow("Error")



