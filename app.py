from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
books = pd.read_csv('books.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        query = request.form['query'].lower()
        results = books[
            books.apply(
                lambda row: query in row.astype(str).str.lower().to_string(),
                axis=1
            )
        ]
    return render_template('index.html', results=results.to_dict(orient='records'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)
