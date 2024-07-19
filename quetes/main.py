# Importe la classe FastAPI depuis le module fastapi
from fastapi import FastAPI
import pandas as pd
# Création d'un dictionnaire qui va être interrogé par une API

df_communes_france = pd.read_csv("C:\Documents\Wild code school\Python\communes_france.csv")

# Crée une instance de l'application FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Bonjour, bien venu dans l'API Communes de Frances"}

@app.get("/nb_communes/region")
def nb_villes_région():
    """
    Retourne le nombre de villes par région.
    """
    return df_communes_france['nom_commune_complet'].groupby(df_communes_france['nom_region']).count().to_dict()


@app.get("/nb_communes/region/{region}")
def nb_villes_région(region):
     """
    Retourne les départements d'une région (nom_region) avec leur nombre de communes.
     """
     liste_region = list(df_communes_france['nom_region'].unique())
     if region in liste_region:
          df_communes_france_x = df_communes_france[df_communes_france['nom_region']== region]
          return(df_communes_france_x['nom_commune_complet'].groupby(df_communes_france_x['nom_departement']).count().to_dict())
     else :
          return("votre reponse n'est pas dans la liste des régions") 
     
@app.get("/departement/{departement}")
def departement_insee(departement):
     """
     Retourne les communes d'un département (nom_departement) avec leur code commune INSEE
     """
     liste_departement = list(df_communes_france['nom_departement'].unique())
     if departement in liste_departement:
          df_communes_france_x = df_communes_france[['nom_commune_complet','code_commune_INSEE']][df_communes_france['nom_departement']== departement]
          return(df_communes_france_x.set_index('nom_commune_complet',drop=True).to_dict())
     else :
          return("votre reponse n'est pas dans la liste des régions") 
     
@app.get("/code_INSEE/{insee}")
def code_insee(insee):
    """
    Retourne les informations d'un code Insee (code_commune_INSEE) 
    (code_commune_INSEE, code_postal, latitude, longitude, nom_commune_complet, nom_département et nom_region )
    """
    liste_code_INSEE = list(df_communes_france['code_commune_INSEE'].unique())
          
    if insee in liste_code_INSEE:
        df_communes_france_x = df_communes_france[df_communes_france['code_commune_INSEE']== insee].drop('Unnamed: 0', axis=1)
        info_dict = {}
        info = df_communes_france_x[df_communes_france_x["code_commune_INSEE"] == insee].to_dict(orient = "records")
        for ele in range(len(info)):
            info_dict[ele] = info[ele]
        return info_dict
    else:    
        return "Ce code n'est pas un code INSEE"
