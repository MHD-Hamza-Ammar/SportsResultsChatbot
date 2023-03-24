from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests
import json
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    messages = [{'bot': 'Hi, how can I help you?'}]
    return render_template('index.html', messages=messages)

@app.route('/parse', methods=['POST'])
def extract():
    data = request.get_json()
    user_message = data['value1']

    # Send message to Rasa
    url = "http://localhost:5005/webhooks/rest/webhook"
    payload = json.dumps({"sender": "user", "message": user_message})
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    response = requests.post(url, data=payload, headers=headers).json()

    # Find the first bot response in the Rasa response
    bot_message = None
    for r in response:
        if 'text' in r:
            bot_message = r['text']
            break

    return jsonify({'bot_message': bot_message})


@app.route('/edit/<int:id>')
def edit(id):
    conn = sqlite3.connect('sports_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sports_data WHERE id=?", (id,))
    sports_data = cursor.fetchone()
    conn.close()

    # Convert the fetched data into a dictionary with column names as keys
    sports_data_dict = {
        "id": sports_data[0],
        "Match": sports_data[1],
        "Score": sports_data[2],
        "Goal_Scorers": sports_data[3],
        "Location": sports_data[4],
        "Date": sports_data[5],
        "Time": sports_data[6],
        "First_Half_Goals": sports_data[7],
        "Second_Half_Goals": sports_data[8],
        "Yellow_Cards": sports_data[9],
        "Red_Cards": sports_data[10],
    }

    return render_template('edit.html', sports_data=sports_data_dict)


@app.route('/update', methods=['POST'])
def update():
    conn = sqlite3.connect('sports_data.db')
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE sports_data SET
        Match=?,
        Score=?,
        Goal_Scorers=?,
        Location=?,
        Date=?,
        Time=?,
        First_Half_Goals=?,
        Second_Half_Goals=?,
        Yellow_Cards=?,
        Red_Cards=?
        WHERE id=?
    """, (
        request.form['match'],
        request.form['score'],
        request.form['goal_scorers'],
        request.form['location'],
        request.form['date'],
        request.form['time'],
        request.form['first_half_goals'],
        request.form['second_half_goals'],
        request.form['yellow_cards'],
        request.form['red_cards'],
        request.form['id']
    ))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
