#https://github.com/sudotechcode/create-map-with-flask

from flask import Flask
import folium

app = Flask(__name__)

@app.route("/")

def base():
    map = folium.Map(location = [45.52356, -122.6750])
    return map._repr_html_()

if __name__ == "__app__":
    app.run(debug=True)