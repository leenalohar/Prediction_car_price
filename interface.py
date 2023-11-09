from flask import Flask,jsonify
from project_app.utils import CarPrediction
import config

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home API'

@app.route('/predict')
def Predict_car_price():
    year = 2015
    km_driven= 42000
    fuel = 'Petrol'
    seller_type = "Individual"
    transmission = 'Manual'
    owner = 'First Owner'
    car_brand_name = 'Honda'  

    print('km_driven,fuel,seller_type,transmission,owner,car_brand_name >>',km_driven,fuel,seller_type,transmission,owner,car_brand_name)

    car_price =  CarPrediction(year,km_driven,fuel,seller_type,transmission,owner,car_brand_name)
    charges = car_price.get_predict_chagres()
    return jsonify({'Charges':f'The Charges of car is{charges}'})

if __name__ == '__main__':
    app.run(port = config.PORT_NUMBER,debug = True ) # Server Start