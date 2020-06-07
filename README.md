# Service auto project.

## Installation
- activate venv: `source venv/bin/activate`
- install mysql: `sudo apt-get install python-dev default-libmysqlclient-dev`
- install python libraries: `pip install -r requirements.txt `
- run migrations: `python manage.py migrate`
- start the server: `python manage.py runserver 0.0.0.0:8000`


### Mysql hints.

##### - Reuniune  (`def-name: comenzi_cu_piese_si_sarcini` )
		SELECT id_constatare_piesa, id_constatare, id_piesa FROM Constatari_Piese
		UNION
		SELECT id_sarcina, id_constatare, Task FROM Sarcini
      
##### - Diferenta (`def-name: Comenzi_fara_constatare`)
        SELECT * FROM Comenzi WHERE id_comanda  
		NOT IN (SELECT id_comanda FROM 	Constatari)

    
##### - Selectie (`def-name: clienti`)  
    SELECT * FROM Clienti ORDER BY id_client DESC;
    
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
  

##### - Jonctiunea (II)  (`def-name: especialisti`)  
	SELECT    id_specialist,
	          nume,
			prenume, 
			specializare, 
			nume_echipa 
	FROM		specialisti s 
	INNER JOIN echipe e 
	where	s.id_echipa=e.id_echipa	
	AND		specializare="Mecanic"
    

###### P.S: Def-name = function name in [views.py](https://github.com/Elisei123/sgbd_proiect_service_auto/blob/master/web_interface/views.py).
