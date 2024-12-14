
from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load knowledge base data
with open("data/knowledge.json", "r") as f:
    knowledge_data = json.load(f)

@app.route("/")
def index():
    return render_template("index.html", data=knowledge_data)

@app.route("/category/<name>")
def category(name):
    category_items = knowledge_data.get(name, [])
    return render_template("category.html", name=name, items=category_items)

@app.route("/visualize")
def visualize():
    chart_path = "static/images/regression_chart.html"
    return render_template("visualization.html", chart_path=chart_path)

if __name__ == "__main__":
    app.run(debug=True)
