from Repository.repository_notare import repo_notare
from domain.Notare import notare
class NotareFileRepository(repo_notare):

    def __init__(self,fileName):
        self.__fileName=fileName
        self.__loadFromFile()
        
    def __loadFromFile(self):
        self.__elems.clear()
        try:
            f=open(self.__fileName,"r")
        except IOError:
            return
        for line in f.readlines():
            if line!="":
                line=line.strip()
                data=line.split(",")
                student=data[0]
                problema=data[1]
                nota=data[2]
                Notare=notare(student,problema,nota)
                
                
                
    
    