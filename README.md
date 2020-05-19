# Service auto project.

## Installation
- activate venv: `source venv/bin/activate`
- install mysql: `sudo apt-get install python-dev default-libmysqlclient-dev`
- install python libraries: `pip install -r requirements.txt `
- run migrations: `python manage.py migrate`
- start the server: `python manage.py runserver 0.0.0.0:8000`


### Mysql hints.

##### - Reuniune  (`def-name: StareComenzi` )
  
    SELECT * FROM Comenzi WHERE stare_comanda = 'In desfasurare!'  
    UNION  
    SELECT * FROM Comenzi WHERE stare_comanda = 'Comanda plasata!'
      
##### - Diferenta (`def-name: ComenziEfectuate`)
    SELECT * FROM `Comenzi`
    EXCEPT
    SELECT * FROM `Comenzi` WHERE stare_comanda = 'In desfasurare!' OR stare_comanda= 'Comanda plasata!'

    
##### - Selectie (`def-name: especialisti`)  
    SELECT id_specialist, nume, prenume, specializare, nume_echipa FROM Specialisti s INNER JOIN Echipe e WHERE s.id_echipa=e.id_echipa AND specializare="Mecanic"
    SELECT id_specialist, nume, prenume, specializare, nume_echipa FROM Specialisti s INNER JOIN Echipe e WHERE s.id_echipa=e.id_echipa AND specializare="Electromecanic"
    SELECT id_specialist, nume, prenume, specializare, nume_echipa FROM Specialisti s INNER JOIN Echipe e WHERE s.id_echipa=e.id_echipa AND specializare="Electrician"
    
##### - Proiectie (`def-name: ComenziDistincte`)
    SELECT DISTINCT descriere FROM Comenzi GROUP BY descriere 
      
##### - Jonctiunea (I)  (`def-name: incasari`)
    SELECT id_constatare, 
       c.nume, 
       c.prenume, 
       const.pret_lucrare 
    FROM   clienti c 
           INNER JOIN comenzi com 
                   ON c.id_client = com.id_client 
           INNER JOIN constatari const 
                   ON com.id_comanda = const.id_comanda   
  

##### - Jonctiunea (II)  (`def-name: ConstatariCuPiese`)  
    SELECT p.id_piesa, 
           p.nume_piesa, 
           com.data_comanda, 
           com.stare_comanda, 
           com.descriere 
    FROM   piese p 
           INNER JOIN constatari const 
                   ON p.id_constatare = const.id_constatare 
           INNER JOIN comenzi com 
                   ON const.id_comanda = com.id_comanda 
    

###### P.S: Def-name = function name in [views.py](https://github.com/Elisei123/sgbd_proiect_service_auto/blob/master/web_interface/views.py).
