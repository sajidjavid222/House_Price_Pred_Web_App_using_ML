
from flask import Flask,render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    room = int(request.form['rooms'])
    distanc = int(request.form['distance'])
    prediction = model.predict([[room, distanc]])
    output = round(prediction[0],2)  #prediction[0] stores the first element of the list returned in prediction eg, 14 incase the list is [14] 
    return render_template('index.html',prediction_text = f"A flat with {room} rooms and located {distanc} KMs away from main city costs Rs {output} Lakhs.")

if __name__ == "__main__":
    app.run()

