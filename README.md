# Service auto project.

## Installation
- install python libraries: `python3 -m pip install -r requirements.txt `
- run migrations: `python3 manage.py migrate`
- start the server: `python3 manage.py runserver`


### Mysql hints.

##### - Reuniune  (`Comenzi in desfasurare / plasate`)
  
    SELECT * FROM Comenzi WHERE stare_comanda = 'In desfasurare!'  
    UNION  
    SELECT * FROM Comenzi WHERE stare_comanda = 'Comanda plasata!'
      
##### - Diferenta (`Comenzi efectuate`)
    SELECT * FROM `Comenzi`
    EXCEPT
    SELECT * FROM `Comenzi` WHERE stare_comanda = 'In desfasurare!' OR stare_comanda= 'Comanda plasata!'

    
##### - Selectie (`Angajati`)  
    SELECT * FROM Specialisti WHERE specializare="Mecanic"  
    SELECT * FROM Specialisti WHERE specializare="Electromecanic"  
    SELECT * FROM Specialisti WHERE specializare="Electrician"
    
##### - Proiectie (`Probleme distincte comenzi`)
    SELECT DISTINCT descriere FROM `Comenzi`  
      
##### - Jonctiunea (I)  
    SELECT id_constatare, 
       c.nume, 
       c.prenume, 
       const.pret_lucrare 
    FROM   clienti c 
           INNER JOIN comenzi com 
                   ON c.id = com.cnp_client 
           INNER JOIN constatari const 
                   ON com.id_comanda = const.id_constatare   
  

##### - Jonctiunea (II)    
    



Pentru mai multe detalii: Click [aici](https://github.com/Elisei123/sgbd_proiect_service_auto/blob/master/web_interface/views.py).
