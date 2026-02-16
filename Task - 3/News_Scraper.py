import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"
try :
    responce = requests.get(url)
    if responce.status_code != 200 :
        print("Failed to retrive webpage.")
        exit()

    headlines = BeautifulSoup(responce.text, "html.parser").find_all("h2")
    with open("HeadLines.txt","w") as file :
        file.write("----------Top HeadLines----------\n\n")
        for index, line in enumerate(headlines, start = 1) :
            title = line.get_text()
            if title :
                file.write(f"{index}.{title}\n")
        print(f"{len(headlines)} Headlines saved to 'HeadLine.txt' file.")
except Exception as e:
    print("Error in website : ",e)