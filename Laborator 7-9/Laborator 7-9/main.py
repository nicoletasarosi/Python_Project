from Repository.repository_student import repo_student
from Repository.repository_problema import repo_problema
from Repository.repository_notare import repo_notare
from domain.validare_student import valid_student
from domain.validare_problema import valid_problema
from domain.validare_notare import valid_notare
from business.student_service import student_service
from business.problema_service import problema_service
from business.notare_service import notare_service
from UI.ui import ui
from Repository.file_repository_student import student_repo_file

def main():
    repo_st=student_repo_file("student.txt")
    repo_pr=repo_problema()
    repo_not=repo_notare()
    valid_st=valid_student()
    valid_pr=valid_problema()
    valid_not=valid_notare()
    serv_student=student_service(repo_st,valid_st)
    serv_problema=problema_service(repo_pr,valid_pr)
    serv_notare=notare_service(repo_not,valid_not,repo_st,repo_pr)
    ui_main=ui(serv_student,serv_problema,serv_notare)
    ui_main.run()
main()