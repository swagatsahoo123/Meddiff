
def getLogFile(file,outputFilePath):

    with open(file) as f:
        contents = f.readlines()
        for line in contents:
            if "ERROR" in line:
                f = open(outputFilePath, "a+")
                f.write(line+"\r\n")

            elif "WARNING" in line:
                f = open(outputFilePath, "a+")
                f.write(line+"\r\n")

filepath = str(input())
outputFilePath=str(input())
getLogFile(filepath,outputFilePath)
