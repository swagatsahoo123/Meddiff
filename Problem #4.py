class Path:
    def __init__(self, path):
        self.current_path = path

    def cd(self, new_path):
        newP = new_path.split('/')
        oldP = self.current_path.split('/')
        lnCount=0
        for str in newP:
            if str == "..":
                lnCount += 1
        length = len(oldP)
        strOut = ""

        for i in range(length-lnCount):
            strOut = strOut + oldP[i] + "/"

        length = len(newP)

        for i in range(length):
            if newP[i] != "..":
                strOut = strOut + newP[i] + "/"

        CurrentPath = strOut[:len(strOut)]
        print(CurrentPath)
        if CurrentPath.index("/") < 0:
           raise "Directory not found"
           return this


path = Path('D:/New folder (2)')
path = path.cd('../New folder (3)')
