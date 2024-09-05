from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load the trained model and vectorizer
try:
    pipeline = joblib.load('phishing_model.pkl')
except Exception as e:
    print(f"Error loading model or vectorizer: {e}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        url = request.form['url']
        # Use the loaded pipeline to make predictions
        prediction = pipeline.predict([url])
        result = 'Phishing' if prediction[0] == 1 else 'Not Phishing'
        return render_template('index.html', prediction_text=f'The URL is: {result}')
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)
