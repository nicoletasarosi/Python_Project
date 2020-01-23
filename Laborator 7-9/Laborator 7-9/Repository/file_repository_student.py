from Repository.repository_student import repo_student
from domain.Student import student

class student_repo_file(repo_student):
    '''
    
    '''
    def __init__(self,fileName):
        repo_student.__init__(self)
        self.__fileName=fileName
        self.__loadFromFile()
        
    def __loadFromFile(self):
        
        try:
            f=open(self.__fileName,"r")
        except IOError:
            return 
        
        for line in f.readlines():
            line.strip()
            if line!="":
                data=line.split(" ")
                studentID=data[0]
                nume=data[1]
                grup=data[2]
                st=student(studentID, nume, grup)
                repo_student.adauga_repo_student(self,st)
        f.close()         
    
    def __appendToFile(self,st):
        f=open(self.__fileName,"a")
        f.write("\n")
        f.write(str(st.get_studentID())+" "+st.get_nume()+" "+str(st.get_grup()))
        f.close()
    
    def adauga_repo_student(self,st):
        repo_student.adauga_repo_student(self, st)
        self.__appendToFile(st)

        
    def sterge(self,elem):
        self.__loadFromFile()
        repo_student.sterge_repo_student(self, elem.get_studentID())
        
        
    def actualizeaza(self,elem,numeNou,grupNou):
        self.__loadFromFile()
        repo_student.actualizeaza_repo_student(self, elem.get_studentID(), numeNou, grupNou)

def test_repo():
    fileName="test.txt"
    repo=student_repo_file(fileName)
    assert repo.getNumar()==0
    repo.adauga_repo_student(student(5,"Andrei",9))
    assert repo.getNumar()==1
