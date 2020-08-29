#https://github.com/sudotechcode/create-map-with-flask

from flask import Flask
import folium

app = Flask(__name__)

@app.route("/")

def base():
    map = folium.Map(location = [38.031572, -78.510631])
    
    folium.Marker(
        location = [38.031572, -78.510631],
        popup = "<b>Hacks of Kindness</b>\n Oct 3, 2020 \n ",
        tooltip = "Hacks of Kindness"
    ).add_to(map)

    return map._repr_html_()

if __name__ == "__app__":
    app.run(debug=True)

