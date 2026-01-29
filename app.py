import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

grocery_list = []

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        item = request.form.get("item")
        if item:
            grocery_list.append(item)
            return redirect(url_for("home"))  # <-- IMPORTANT
    
    return render_template("index.html", groceries=grocery_list)

@app.route('/delete', methods=["POST"])
def delete():
    item = request.form.get("item")
    if item and item in grocery_list:
        grocery_list.remove(item)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

