# Service auto project.

## Installation
- install python libraries: `python3 -m pip install -r requirements.txt `
- run migrations: `python3 manage.py migrate`
- start the server: `python3 manage.py runserver`


### Mysql hints.

#####- Reuniune  (`Comenzi in desfasurare / plasate`)
  
    SELECT * FROM Comenzi WHERE stare_comanda = 'In desfasurare!'  
    UNION  
    SELECT * FROM Comenzi WHERE stare_comanda = 'Comanda plasata!'
##### - Diferenta
##### - Selectie (`Angajati`)  
    SELECT * FROM Specialisti WHERE specializare="Mecanic"  
    SELECT * FROM Specialisti WHERE specializare="Electromecanic"  
    SELECT * FROM Specialisti WHERE specializare="Electrician"
##### - Proiectie
##### - J1
##### - J2


Pentru mai multe detalii: Click [aici](https://github.com/Elisei123/sgbd_proiect_service_auto/blob/master/web_interface/views.py).