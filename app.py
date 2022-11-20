from flask import Flask, render_template, request
import pickle

app = Flask(__name__) # initializing a flask app

model = pickle.load(open('predictionmodel.sav', 'rb'))


@app.route('/',methods=['POST','GET'])  # route to display the home page
def homePage():
    result = ''
    return render_template("index.html",**locals())




@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def predict():
        #  reading the inputs given by the user
        fixed_acidity= float((request.form['fixed_acidity'])) 
        volatile_acidity = float((request.form['volatile_acidity']))
        citric_acid = float((request.form['citric_acid']))
        residual_sugar = float((request.form['residual_sugar']))
        chlorides = float((request.form['chlorides']))
        free_sulfur_dioxide = float((request.form['free_sulfur_dioxide']))
        total_sulfur_dioxide = float((request.form['total_sulfur_dioxide']))
        density = float((request.form['density']))
        pH = float((request.form['pH']))
        sulphates = float((request.form['sulphates']))
        alcohol = float((request.form['alcohol']))
        result = model.predict([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]])
        
        if result :
            wineq= "good"
        else :
            wineq= "bad"
        return render_template("submit.html",**locals())




if __name__ == "__main__":
	app.run(debug=True) # running the app