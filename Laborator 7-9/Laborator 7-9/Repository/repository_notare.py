class RepoError(Exception):
    pass
class repo_notare(object):
    
    def __init__(self):
        self._elems =[]
    
    def getNumar(self):
        return len(self._elems)

    def getToti(self):
        return self._elems
    
    def getById(self, id):
        for i in range(self.getNumar()):
            if self._elems[i].get_id() == id:
                return self._elems[i]
        return None
    
    def sorteaza_alfabetic(self,_elems):
        '''
        Functie care sorteaza alfabetic dupa studenti, dupa medie
        :param elems: lista 
        '''
        for i in range(self.getNumar()-1):
            j=i+1
            for j in range(self.getNumar()):
                if self._elems[i].get_student().get_nume() > self._elems[j].get_student().get_nume():
                    aux=self._elems[i]
                    self._elems[i]=self._elems[j]
                    self._elems[j]=aux
                elif self._elems[i].get_student().get_nume() == self._elems[j].get_student().get_nume():
                    if self._elems[i].get_nota() > self._elems[j].get_nota():
                        aux=self._elems[i]
                        self._elems[i]=self._elems[j]
                        self._elems[j]=aux
        return _elems           
    def medie_note(self,student):
        '''
        Functie care calculeaza media notelor unui student
        :param student:
        '''
        suma = 0
        numar = 0
        for i in range(len(self._elems)):
            if self._elems[i].get_student() == student:
                suma += int(self._elems[i].get_nota())
                numar += 1
        if numar == 0:
            return -1
        else:
            return suma/numar
        
    def studenti_medie_note(self,__elems):
        '''
        Functie care returneaza o lista cu studentii care au media notelor de la laborator sunt mai mici ca 5
        :param __elems:
        '''
        studenti=[]
        for i in range(len(self._elems)):
            if self.medie_note(self._elems[i].get_student()) < 5 : 
                studenti.append(self._elems[i])
        return studenti
        
    def adauga_repo_nota(self,elem):
        '''
        Functie ce adauga o nota in repository
        :param elem:lista de note
        '''
        if elem in self._elems:
            raise RepoError("Elementul exista!")
        self._elems.append(elem)
        
    def sterge_repo_nota(self, id):
        notare=self.getById(id)
        if (self._elems.__contains__(notare)):
            self._elems.remove(notare)  
              
    def actualizeaza_repo_nota(self, id, notaNoua):
        '''
        Functie ce actualizeaza o nota in repository
    
        '''
        notare=self.getById(id)
        notare.set_nota(notaNoua)