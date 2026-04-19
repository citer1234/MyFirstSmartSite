from flask import Flask, render_template, request
from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis", model="blanchefort/rubert-base-cased-sentiment")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendation = ""
    user_text = ""

    if request.method == 'POST':
        user_text = request.form['message']

        result = sentiment_analyzer(user_text)[0]
        label = result["label"]

        if label == "positive":
            recommendation = "У тебя хорошее настроение"
        elif label == "negative":
            recommendation = "У тебя настроение не очень("
        else:
            recommendation = "У тебя норм настроение"

    return render_template('index.html', recommendation=recommendation,  # ← исправлено: две 'm'
                           user_text=user_text)

if __name__ == '__main__':
    app.run(debug=True)