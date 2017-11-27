Instant run-off voting stemtel programma voor het kiezen van besturen
more info: https://en.wikipedia.org/wiki/Instant-runoff_voting
Gemaakt door: Yannick Vinkesteijn


#How to run
- python 3 nodig
- stemmen worden ingeladen via CSV

#stemmen
- Blanco; wordt in CSV aangegeven als 'bl', tellen niet mee met het quorum en worden gezien als niet uitgebracht.

- Onthouden; wordt in CSV aangegeven als 'gv', tellen als het hebben van geen voorkeur en tellen wel mee met het quorum.

- Foutstemmen; (bijv. niet alle besturen ranken, een bestuur op meerdere plekken.) worden gezien als blanco.

#procedure
- Bestuur wint indien de meeste eerste keus stemmen heeft en absolute meerderheid van het totaal aantal stemmen.
- Bij gelijkspel vallen alle besturen met het minst aantal stemmen af, de eerste keus stemmen van deze besturen worden verdeeld naar de nog overgebleven besturen.

#scripts
runoff_count.py; script voor het uitvoeren van run-off voting
gen.py; maakt random stembiljetten met besturen om te testen
functions_old.py; oud script
randvote.py, votes.csv; test CSVs

# To Do:
- vote log
- implement pyforms (interface)
