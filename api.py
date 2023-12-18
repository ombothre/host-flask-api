from flask import Flask, jsonify, request
import joblib,numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.svm import SVC

app = Flask(__name__)

# Load the trained model

model = joblib.load('models/model.pkl')
le = joblib.load('models/label.pkl')
std = joblib.load('models/std.pkl')

@app.route('/')
def home():
    return "Api on /predict"
    
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)

    input = data['input']
    x = [input['gender'], input['age'], input['salary']]

    #preprocessing on predicting data

    x[0] = le.transform([x[0]])
    x[0] = x[0][0]

    x = np.array(x, dtype = float).reshape(1,-1)

    x = std.transform(x)

    #predicting values

    y = model.predict(x)
    
    return jsonify({'prediction': y.tolist()})
    
if __name__ == '__main__':
    app.run(debug=True)
