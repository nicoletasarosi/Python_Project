from Repository.repository_problema import repo_problema
from domain.Problema import problema

class problemaFileRepo(repo_problema):
    
    def __init__(self,fileName):
        self.__fileName=fileName
        self.__loadFromFile()
        
    def __loadFromFile(self):
        try:
            f=open(self.__fileName,'r')
        except IOError:
            return
        
        for line in f.readlines():
            if line!="":
                line=line.strip()
                data=line.split(" ")
                nrPr_nrLab=data[0]
                descriere=data[1]
                deadline=data[2]
                pr=problema(nrPr_nrLab,descriere,deadline)
                repo_problema.adauga_repo_problema(self, pr)
        f.close()
        
    def __appendToFile(self,pr):
        f=open(self.__fileName,"a")
        f.write("\n")
        f.write(pr.get_nrLab_nrPr()+" "+pr.get_descriere()+" "+pr.get_deadline())
        f.close()
    
    def adauga(self,elem):
        repo_problema.adauga_repo_problema(self, elem)
        self.__appendToFile(elem)
        
    def sterge(self,elem):
        self.__loadFromFile()
        repo_problema.sterge_repo_problema(self, elem.get_nrLab_nrPr())
        
    def actualizeaza(self,elem,descriereNoua, deadlineNou):
        self.__loadFromFile()
        repo_problema.actualizeaza_repo_problema(self, elem.get_nrLab_nrPr(), descriereNoua, deadlineNou)
    
        