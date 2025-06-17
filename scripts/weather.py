import random

def apply_weather_conditions(G):
    weather = random.choice(["clear", "rain", "snow"]) 
    print(f"Weather: {weather.capitalize()}")

    for u, v, data in G.edges(data=True):
        if weather == "rain":
            data['weight'] *= 1.5 
        elif weather == "snow":
            data['weight'] *= 2.0 
        print(f"Updated traffic on road {u}-{v}: New weight = {data['weight']:.2f} (Weather: {weather})")