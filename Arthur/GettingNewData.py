import requests
from astroquery.simbad import Simbad
from astropy.table import Table, vstack
from astropy.io import fits


#Get list of center black holes
neu3 = ['3c273', 'Arp 151', 'IC 1459', 'M104', 'M105', 
        'M106', 'M31', 'M32', 'M51', 'M60', 'M77', 'M81', 
        'M84', 'M87', 'Sagittarius A', 'NGC 1023', 'NGC 1194', 
        'NGC 1277', 'NGC 1365', 'NGC 2273', 'NGC 2778', 
        'NGC 2787', 'NGC 2960', 'NGC 3115', 'NGC 3245', 
        'NGC 3377', 'NGC 3384', 'NGC 3393', 'NGC 3516', 
        'NGC 3585', 'NGC 3607', 'NGC 3608', 'NGC 3783', 
        'NGC 3842', 'NGC 3862', 'NGC 3945', 'NGC 3998', 
        'NGC 4026', 'NGC 4061', 'NGC 4151', 'NGC 4178', 
        'NGC 4253', 'NGC 4261', 'NGC 4335', 'NGC 4342', 
        'NGC 4388', 'NGC 4395', 'NGC 4473', 'NGC 4486b', 
        'NGC 4697', 'NGC 4889', 'NGC 541', 'NGC 5576', 
        'NGC 6240', 'NGC 7052', 'NGC 7457', 'NGC 821', 
         ] #'RX J1242-11', 'SDSS J0927+2943','ULAS J1120-0641'

if not neu3:
    url = "https://blackholes.stardate.org/objects/type-supermassive.html"
    
    response = requests.get(url)
    
    # check if website is avaible
    if response.status_code == 200:
        text = response.text
        print("Erfolgreich abgerufen!")
        # Inhalt der Webseite (HTML) ausgeben
        neu = text[text.index('<table width="100%" cellspacing="0" cellpadding="0">'): text.rindex("</table>")]
        neu2 = neu.split("<strong>")[1:]
        neu3 = [neu2[i][:neu2[i].index("</strong>")] for i in range(len(neu2))]
        print(neu3)
    
    else:
        print(f"Fehler beim Abrufen der Seite: {response.status_code}")
    
blackHoles = neu3  
# get additional data
#result_table = simbad.query_region("m81", radius="0.5d")   


#Sigma from the orignal Paper: https://adsabs.harvard.edu/pdf/1987ApJS...64..581D
#Simbad.query_object("M [1-9]", wildcard=True) 

simbad = Simbad()

#Simbad.list_votable_fields()[["name", "description"]]
simbad.add_votable_fields("pm")
simbad.add_votable_fields("coo_bibcode")
simbad.add_votable_fields("distance")
simbad.add_votable_fields("z_value")
simbad.add_votable_fields("otype")
simbad.add_votable_fields("parallax")
simbad.add_votable_fields("coordinates")

#result_table = simbad.query_region(blackHoles[13])#, radius="2d5m")# criteria="OTYPE!=Galaxy") #radius="0.5d",

for i in blackHoles[57:]:
    try:
        table = Table(simbad.query_region(i))
        for ii in ("MAIN_ID", "COO_BIBCODE", "COO_BIBCODE_2", 
                   "OTYPE", "OTYPE", "PLX_BIBCODE", "COO_BIBCODE_3"
                   ):
            table[ii] = [str(ii) for ii in table[ii]]
        table.write(f"data\Object_{i}.fits", format='fits', overwrite=True)
    except KeyError:
        print(f"KeyError bei {i}")


    