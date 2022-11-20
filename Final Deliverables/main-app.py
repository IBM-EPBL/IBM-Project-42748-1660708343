from flask import  Flask,render_template,request
import pickle
import numpy as np

app = Flask(__name__)
model=pickle.load(open("resale_value_pickle_file.sav","rb"))
@app.route("/")
def home():
    return render_template("cars-index.html")

@app.route('/submit',methods=["POST","GET"])
def prediction():
    if request.method=="POST":
        yearofRegistration=request.form["yearofRegistration"]
        monthofRegistration=request.form["monthofRegistration"]
        powerPS = request.form["powerPS"]
        kilometer = request.form["kilometer"]
        notRepairedDamage = request.form["notRepairedDamage"]
        if notRepairedDamage == "Yes":
            notRepairedDamage =1
        elif notRepairedDamage == "No":
            notRepairedDamage =0
        elif notRepairedDamage == "not-declared":
            notRepairedDamage =2
        brand = request.form["brand"]
        if brand == "audi":
            brand = 1
        elif brand == "jeep":
            brand = 14
        elif brand == "volkswagen":
            brand = 38
        elif brand == "skoda":
            brand = 31
        elif brand == "bmw":
            brand = 2
        elif brand == "nissan":
            brand = 23
        elif brand == "renault":
            brand = 27
        elif brand == "ford":
            brand = 10
        elif brand == "honda":
            brand = 11
        elif brand == "mercedes_benz":
            brand = 20
        elif brand == "toyota":
            brand = 36
        elif brand == "hyundai":
            brand = 12
        elif brand == "kia":
            brand = 15
        elif brand == "peugeot":
            brand = 25
        elif brand == "mitsubishi":
            brand = 22
        elif brand == "fiat":
            brand = 9
        elif brand == "volvo":
            brand = 39
        elif brand == "suzuki":
            brand = 35
        elif brand == "porsche":
            brand = 26
        elif brand == "dacia":
            brand = 6
        gearbox_feat=request.form["gearbox_feat"]
        if gearbox_feat == "manual":
            gearbox_feat =1
        elif gearbox_feat == "automatic":
            gearbox_feat =0
        fuelType_feat = request.form["fuelType_feat"]
        if fuelType_feat=="petrol":
            fuelType_feat=1
        elif fuelType_feat=="diesel":
            fuelType_feat=3
        elif fuelType_feat=="lpg":
            fuelType_feat=4
        elif fuelType_feat=="hybrid":
            fuelType_feat=6
        elif fuelType_feat=="cng":
            fuelType_feat=7
        vehicleType = request.form["vehicleType"]
        if vehicleType == "coupe":
            vehicleType = 3
        elif vehicleType == "suv":
            vehicleType = 8
        elif vehicleType == "small car":
            vehicleType = 7
        elif vehicleType == "limousine":
            vehicleType = 4
        elif vehicleType == "bus":
            vehicleType = 0
        elif vehicleType == "combination":
            vehicleType = 1
        elif vehicleType == "others":
            vehicleType = 6
        elif vehicleType == "convertible":
            vehicleType = 7


        int_features = [yearofRegistration, powerPS,kilometer,monthofRegistration,notRepairedDamage,brand,gearbox_feat,fuelType_feat,vehicleType]
        features = [np.array(int_features, dtype=int)]
        prediction=model.predict(features)
        return render_template("cars-submit.html",prediction=round(prediction[0],2))

if __name__=="__main__":
    app.run(debug=True)