import joblib
from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/crop_prediction')
def crop_prediction():
    return render_template('form.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form', methods=["POST"])
def brain():
    nitrogen = float(request.form['Nitrogen'])
    phosphorus = float(request.form['Phosphorus'])
    potassium = float(request.form['Potassium'])
    temperature = float(request.form['Temperature'])
    humidity = float(request.form['Humidity'])
    ph = float(request.form['PH'])
    rainfall = float(request.form['Rainfall'])

    value = [nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]

    if ph>0 and ph<= 14 and temperature < 100 and humidity > 0:
        model = joblib.load('crop_recommend')  # Correct usage of joblib.load
        arr = [value]
        acc = model.predict(arr)
        return render_template('predict.html', prediction=str(acc))
    else:
        return "Sorry... error in entered values, please check the values and fill it again"

if __name__ == "__main__":
    app.run(debug=True)
