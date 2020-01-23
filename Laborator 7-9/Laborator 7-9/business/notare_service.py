from domain.StudentProblema import StudentProblema
from domain.Notare import notare

class notare_service(object):
    def __init__(self,__repo,__validator,Repo_st,Repo_pr):
        self.__repo = __repo
        self.__validator = __validator
        self.Repo_st = Repo_st
        self.Repo_pr = Repo_pr
        
    
    def adauga_nota(self,__student,__problema,__nota):
        '''
        Functie ce adauga o nota, o valideaza si o adauga in repository
        :param __student: student
        :param __problema:problema
        :param __nota: nota-float
        '''
        n =notare(__student,__problema,__nota)
        self.__validator.validate(n)
        self.__repo.adauga_repo_nota(n)
        
    def getNote(self):
        '''
        Functie ce retuneaza toate notele
        '''
        l = self.__repo.getToti()
        return l
    
    def sterge_notare(self,id):
        '''
        FUnctie care sterge o notare 
        '''
        self.__repo.sterge_repo_nota(id)
        
    def actualizeaza_notare(self,id,notaNoua):
        '''
        functie care actualizeaza o nota
        :param id: id-int
        :param notaNoua: int
        '''
        self.__repo.actualizeaza_notare(id,notaNoua)
    
    def sorteaza(self):
        '''
        functie care sorteaza afabetic si returneaza lista de studenti sortata
        '''
        l=self.getNote()
        self.__repo.sorteaza_alfabetic(l)
        return l
    def studenti_medie_note_5(self):
        '''
        Functie care returneaza lista de studenti ce au media notelor sub 5
        '''
        l=self.getNote()
        self.__repo.studenti_medie_note(l)
        return l
    
    
    def getAllDescInDescriere(self,desc):
        '''
        Functie care returneaza o lista de entitati StudentProblema pentru probleme ce contin descrierea desc
        :param desc: string- descrierea ceruta
        output: rez-lista de entitati
        '''
        rez=[]
        notari=self.getNote()
        for n in notari:
            if desc in n.get_problema().get_descriere():
                sp=StudentProblema(n.get_student().get_studentID(),1,n.get_student().get_nume())
                found=False
                for n in rez:
                    if n.get_studentID()==sp.get_studentID():
                        n.set_nr_problema(n.get_nr_problema()+1)
                        found=True
                if found==False:
                    rez.append(sp)
        return rez
    
    def entitateaXCuCeiMaiMultiY(self,desc):
        '''
        Metoda care returneaza entitatea StudentProblema cu cele mai multe probleme care contin descrierea desc
        Input: desc- string
        Output: sp-StudentProblema, daca s-a gasit un astfel de obiect
                None - in caz contrar
        '''
    
        sps=self.getAllDescInDescriere(desc)
        if len(sps)==0:
            return None
        maxim=-1
        sp = sps[0]
        for elem in sps:
            if elem.get_nr_probleme() > maxim:
                maxim = elem.get_nr_probleme()
                sp = elem
        return sp
            
    

