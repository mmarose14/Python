import api
import files
import config

#Load list of symbols
listOfSymbols = files.getListOfSymbols()

#Retrieve and organize the data
data = api.getDividendDataForListOfSymbols(listOfSymbols)

#Export to file
files.exportToFile(data, api.isSandbox)





          

