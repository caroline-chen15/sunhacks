#https://github.com/sudotechcode/create-map-with-flask
#https://stackoverflow.com/questions/61928013/adding-a-title-or-text-to-a-folium-map

from flask import Flask, render_template
import folium
import requests
from bs4 import BeautifulSoup
import scraper

app = Flask(__name__)

@app.route("/")

def base():
    
    loc = "2020-2021 Hackathon Map"
    title_html = '''
             <h3 align="center" style="font-size:16px"><b>{}</b></h3>
             '''.format(loc)
    map = folium.Map(location = [38.031572, -78.510631])
    map.get_root().html.add_child(folium.Element(title_html))

    # folium.Marker(
    #     location = [38.031572, -78.510631],
    #     popup = "<b>Hacks of Kindness</b>\n Oct 3, 2020 \n ",
    #     tooltip = "Hacks of Kindness"
    # ).add_to(map)

    names, coords, dates, links = scraper.manip()

    count = 0

    for i in coords:
        #print(i)
        if i[0] != "":
            txt = "<b>"+str(names[count])+"</b>" + "\n" + str(dates[count]) + "\n" + str(links[count])
            folium.Marker(
                location = [i[2], i[1]],
                popup = folium.Popup(txt, max_width='100%'),
                tooltip = names[count],
            ).add_to(map)
        count+=1

    return map._repr_html_()

if __name__ == "__app__":
    app.run(debug=True)

