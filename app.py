import numpy as np
import pickle
from flask import Flask, request, render_template

# Load the saved model
model = pickle.load(open("model.pkl", "rb"))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        input_features = [float(x) for x in request.form.values()]
        final_input = np.array(input_features).reshape(1, -1)
        prediction = model.predict(final_input)

        if prediction[0] == 0:
            result = "The person does NOT have Heart Disease"
        else:
            result = "The person HAS Heart Disease"

        return render_template("index.html", prediction_text=result)

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)