from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/<city>')
def show_map(city):
    city_map_files = {
        'mumbai': 'Mumbai_Traffic_Alerts_Map.html',
        'bangalore': 'Bangalore_Traffic_Alerts_Map.html',
        'hyderabad': 'Hyderabad_Traffic_Alerts_Map.html',
        'delhi': 'Delhi_Traffic_Alerts_Map.html',
        'chennai': 'Chennai_Traffic_Alerts_Map.html',
        'kolkata': 'Kolkata_Traffic_Alerts_Map.html',
    }
    map_file = city_map_files.get(city.lower())
    if map_file:
        return render_template(map_file)
    else:
        return "<h1>City map not found</h1>"

if __name__ == '__main__':
    app.run(debug=True)
