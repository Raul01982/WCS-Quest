# Imports
from flask import Flask
from flask_restful import Resource, Api
import pandas as pd
from datetime import date
import datetime 

df_flower = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/flower_color_symbolism.csv')

df_flower['color'] = df_flower['Flower Color '].apply(lambda x : x.split(" ")[0])

# Ici nous créons des instances de l'application et de l'API 
app = Flask(__name__)
api = Api(app)
today = date.today()
today = datetime.datetime.strftime(today, "%d-%m-%Y")
df_flower = df_flower.drop(columns='Flower Color ')

class my_API_class(Resource):
    def get(self, color):
        return {color : df_flower['Meaning'][df_flower['color']==color].values[0], "Date" : today} 
    
api.add_resource(my_API_class, '/<string:color>')

# L'API sera lancée ici dans le script. Pour l'instant, tu peux laisser l'argument debug = True
if __name__ == '__main__':
    app.run(debug=True)





