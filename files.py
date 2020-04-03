import os

TEST_ONLY = False   #Only used for list of test symbols (symbols-test.txt)

def getListOfSymbols():
    #Current directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(os.curdir)

    if (TEST_ONLY):
        filename = "symbols-test.txt"
    else:
        filename = "symbols.txt"

    #Read ticker symbols file - default file contains options with high IV
    symbols = open(filename,"r")
    symbols.close

    #Strip newline and create object
    ListOfSymbols = [line.rstrip() for line in symbols]
    
    return ListOfSymbols

def exportToFile(symbols,sandbox):
    if (sandbox):
        filename = "output-test.txt"
    else:
        filename = "output.txt"

    output_file = open(filename, "w")

    for line in symbols:
        output_file.writelines(f"{line['symbol']}, {line['ex_div_date']}, {line['div_yield']}\n")