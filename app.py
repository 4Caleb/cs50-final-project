from flask import Flask, render_template, request, jsonify
import util
import numpy as np
import pickle

with open("gbr2_new", "rb") as f:
    model = pickle.load(f)




app = Flask(__name__)



@app.route('/')
def landing():
    return render_template("landing.html")

@app.route('/abuja')
def abuja():
    return render_template("abuja.html")

@app.route("/predict_abuja", methods = ["GET","POST"])
def predict_abuja():
    col_features = ['Serviced', 'Newly Built', 'Furnished', 'Bedrooms', 'Home_DETACHED_DUPLEX', 'Home_DUPLEX', 'Home_FLAT', 'Home_MANSION', 'Home_SEMI_DETACHED_DUPLEX', 'Home_TERRACE_DUPLEX', 'Zones_Abuja_low', 'Zones_Abuja_mid', 'Zones_Lagos_high', 'Zones_Lagos_low', 'Zones_Lagos_mid']
    x = np.zeros(len(col_features))

    x[0] = request.form.get("serviced")
    x[1] = request.form.get("newbuilt")
    x[2] = request.form.get("furnished")
    x[3] = request.form.get("bed")
    
    
    
    
    house = request.form.get("house")
    for i in ['Home_DETACHED_DUPLEX', 'Home_DUPLEX', 'Home_FLAT', 'Home_MANSION', 'Home_SEMI_DETACHED_DUPLEX', 'Home_TERRACE_DUPLEX']:
        if house == i:
            x[col_features.index(house)] = 1

    abuja_low = util.abuja_low
    abuja_mid = util.abuja_mid
    location = request.form.get("location")
    if location in abuja_low:
        x[col_features.index("Zones_Abuja_low")] = 1

    elif location in abuja_mid:
         x[col_features.index("Zones_Abuja_mid")] = 1
         

    response = abs(round(model.predict([x])[0],2))
    print(response)
    return jsonify(response)

@app.route("/lagos")
def lagos():
    return render_template("lagos.html")

@app.route("/predict_lagos", methods = ["GET","POST"])
def predict_lagos():
    col_features = ['Serviced', 'Newly Built', 'Furnished', 'Bedrooms', 'Home_DETACHED_DUPLEX', 'Home_DUPLEX', 'Home_FLAT', 'Home_MANSION', 'Home_SEMI_DETACHED_DUPLEX', 'Home_TERRACE_DUPLEX', 'Zones_Abuja_low', 'Zones_Abuja_mid', 'Zones_Lagos_high', 'Zones_Lagos_low', 'Zones_Lagos_mid']
    x = np.zeros(len(col_features))

    x[0] = request.form.get("serviced")
    x[1] = request.form.get("newbuilt")
    x[2] = request.form.get("furnished")
    x[3] = request.form.get("bed")
    
    
    
    
    house = request.form.get("house")
    for i in ['Home_DETACHED_DUPLEX', 'Home_DUPLEX', 'Home_FLAT', 'Home_MANSION', 'Home_SEMI_DETACHED_DUPLEX', 'Home_TERRACE_DUPLEX']:
        if house == i:
            x[col_features.index(house)] = 1

    lagos_low = util.lagos_low
    lagos_mid = util.lagos_mid
    lagos_high = util.lagos_high
    location = request.form.get("location")
    if location in lagos_low:
        x[col_features.index("Zones_Lagos_low")] = 1

    elif location in lagos_mid:
        x[col_features.index("Zones_Lagos_mid")] = 1

    elif location in lagos_high:
        x[col_features.index("Zones_Lagos_high")] = 1

        

    response = abs(round(model.predict([x])[0],2))
    print(response)
    return jsonify(response)

@app.route('/loc_abuja')
def home():
    response = util.loc_abuja
    return response

@app.route('/loc_lagos')
def home2():
    response = util.loc_lagos
    return response


if __name__ == "__main__":
    app.run(debug=True)