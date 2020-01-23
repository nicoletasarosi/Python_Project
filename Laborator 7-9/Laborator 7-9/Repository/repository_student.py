from domain.Student import student

class DuplicatedIdError(Exception):
    pass
class repo_student(object):
    
    def __init__(self):
        self.__elems 
    
    def getNumar(self):
        return len(self.__elems)

    def getToti(self):
        return self.__elems

    def adauga_repo_student(self,elem):
        
        l=self.getToti()
        for el in l:
            if el.get_studentID()==elem.get_studentID():
                errors="Id-ul trebuie sa fie unic"
                raise DuplicatedIdError(errors)
        
        self.__elems.append(elem)
        
    def actualizeaza_repo_student(self, studentID, numeNou,grupNou):
        student=self.getById(studentID)
        student.set_nume(numeNou)
        student.set_grup(grupNou) 
    
    def sterge_repo_student(self, studentID):
        student=self.getById(studentID)
        if (self.__elems.__contains__(student)):
            self.__elems.remove(student)

    def getById(self, studentID):
        for i in range(self.getNumar()):
            if self.__elems[i].get_studentID() == studentID:
                return self.__elems[i]
        return None
    
    def cauta_repo_student(self,elem):
        if elem not in self.__elems:
            raise RepoError("Element inexistent!")
        for x in self.__elems:
            if x == elem:
                return x


    
        

