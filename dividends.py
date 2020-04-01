import os 
import json
import requests
import config

#Switch environment
ENV = "sandbox"
#ENV = "cloud"

def isSandbox(): return (ENV == "sandbox")

def getListOfSymbols():
    #Current directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    #Read ticker symbols file
    symbols = open("symbols.txt","r")
    symbols.close

    #Strip newline and create object
    ListOfSymbols = [line.rstrip() for line in symbols]

    return ListOfSymbols

def getDataForListOfSymbols(ListOfSymbols):
    data = []
    for symbol in ListOfSymbols:
        #Endpoint for next dividend date
        url = f"https://{ENV}.iexapis.com/stable/data-points/{symbol}/NEXTDIVIDENDDATE?token={config.API_TOKEN}"
        ex_div_date = getTickerData(url)
        data.append([symbol, ex_div_date])
    
    #Return sorted by date
    return sorted(data, key=lambda r: r[1])


#Retrieve data from url endpoint
def getTickerData(url):
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))

listOfSymbols = getListOfSymbols()

#Separate list for Sandbox testing
if (isSandbox()):
    filename = "output-test.txt"
else:
    filename = "output.txt"

output = open(filename,"w+")

data = getDataForListOfSymbols(listOfSymbols)

for line in data:
    #print(line[0], line[1])
    output.writelines(f"{line[0]},{line[1]}\n")





          

