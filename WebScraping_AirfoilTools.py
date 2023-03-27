import requests
from bs4 import BeautifulSoup

url = "http://airfoiltools.com/search/airfoils"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html5lib")

links = soup.find_all("td", class_="link")
Airfoils = []

for i in range(0, len(links)):
    link = links[i]
    Link_href = link.find_all("a", href=True, text = True)
    TagElem = str(Link_href[0])
    Link = TagElem[9:].split('"', 1)[0]
    Airfoils.append("http://airfoiltools.com"+Link)

ReynoldsNumberDict = {
    "50,000": "row0",
    "100,000": "row1",
    "200,000": "row0",
    "500,000": "row1",
    "1,000,000": "row0",
    }

DesReynolds = "500,000"
#Des_Cl_Cd = input("Enter the desired aerodynamic efficiency ((L/D)_max): ")
Des_Cl_Cd = 120

for airfoil in Airfoils[1:3]:           #change 3 to len(airfoils) to search through all airfoils
    res = requests.get(airfoil)
    soup = BeautifulSoup(res.text, "html5lib")
    titleList = soup.find_all("h1")
    titleList = str(titleList[0])
    airfoilName = titleList[4:].split("<", 1)[0]
    TableRows = soup.find_all("tr", class_= ReynoldsNumberDict[DesReynolds])
    for i in range(0, len(TableRows)):
        ReynoldsNumberRow = TableRows[i].find_all("td", class_="cell2")
        ReynoldsNumberRow = str(ReynoldsNumberRow)
        ReynoldsNumber = ReynoldsNumberRow[19:].split("<", 1)[0]
        if ReynoldsNumber == DesReynolds:
            Max_Cl_Cd_Row = TableRows[i].find_all("td", class_="cell4")
            Max_Cl_Cd_Row = str(Max_Cl_Cd_Row)
            Max_Cl_Cd_Info = Max_Cl_Cd_Row[19:].split("<", 1)[0]
            Max_Cl_Cd = Max_Cl_Cd_Info.split(" ", 1)[0]
            Aoa = Max_Cl_Cd_Info.split("=", 1)[1][:-1]
            print(Aoa)

            # cast the aoa into a 4sf sting with 5 characters
            
            
            N_Crit_Row = TableRows[i].find_all("td", class_="cell3")
            N_Crit_Row = str(N_Crit_Row)
            N_Crit = N_Crit_Row[19:].split("<", 1)[0]

            DetailsURL_String = TableRows[i].find_all("td", class_="cell7")
            #print(DetailsURL_String)
            DetailsURL = str(DetailsURL_String)[28:].split(">", 1)[0][:-1]
            #print(DetailsURL)

            AirfoilDetailsURL = "http://airfoiltools.com/" + DetailsURL

            DetailsRequest = requests.get(AirfoilDetailsURL)
            DetailsSoup = BeautifulSoup(DetailsRequest.text, "html5lib")
            TableText = DetailsSoup.find_all("pre")


            # go to big string of data and use string.find to find the index of the first character matches, then pull out the relevant characters

TableTextElem = str(TableText[0])
alpha_elem = TableTextElem.find("alpha")
print(alpha_elem)
TableText_afteralpha = str(TableText[0])[alpha_elem:]
#print(TableText_afteralpha[alpha_elem:])
print(TableText_afteralpha)


zero_elem = TableText_afteralpha.find("0.000")
TableText_afterZero = str(TableText_afteralpha[zero_elem:])
print(TableText_afterZero)
