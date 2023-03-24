import sqlite3

def get_sports_data(query_type):
    # Connect to the SQLite database
    conn = sqlite3.connect('sports_data.db')
    cursor = conn.cursor()

    if query_type == 'teams_playing':
        cursor.execute("SELECT Match FROM sports_data LIMIT 1")
        match = cursor.fetchone()[0]
        return f"The teams playing today are: {match}"

    elif query_type == 'current_score':
        cursor.execute("SELECT Score FROM sports_data LIMIT 1")
        score = cursor.fetchone()[0]
        return f"The current score is {score}"

    elif query_type == 'goal_scorers':
        cursor.execute("SELECT Goal_Scorers FROM sports_data LIMIT 1")
        goal_scorers = cursor.fetchone()[0]
        return f"The goal scorers for today's match are: {goal_scorers}"

    elif query_type == 'match_location':
        cursor.execute("SELECT Location FROM sports_data LIMIT 1")
        location = cursor.fetchone()[0]
        return f"The match is being played at {location}"

    elif query_type == 'match_date':
        cursor.execute("SELECT Date FROM sports_data LIMIT 1")
        date = cursor.fetchone()[0]
        return f"The match date is {date}"

    elif query_type == 'match_time':
        cursor.execute("SELECT Time FROM sports_data LIMIT 1")
        time = cursor.fetchone()[0]
        return f"The match time is {time}"

    elif query_type == 'first_half_goals':
        cursor.execute("SELECT First_Half_Goals FROM sports_data LIMIT 1")
        first_half_goals = cursor.fetchone()[0]
        return f"The number of goals scored in the first half is {first_half_goals}"

    elif query_type == 'second_half_goals':
        cursor.execute("SELECT Second_Half_Goals FROM sports_data LIMIT 1")
        second_half_goals = cursor.fetchone()[0]
        return f"The number of goals scored in the second half is {second_half_goals}"

    elif query_type == 'yellow_cards':
        cursor.execute("SELECT Yellow_Cards FROM sports_data LIMIT 1")
        yellow_cards = cursor.fetchone()[0]
        return f"The number of yellow cards in the match is {yellow_cards}"

    elif query_type == 'red_cards':
        cursor.execute("SELECT Red_Cards FROM sports_data LIMIT 1")
        red_cards = cursor.fetchone()[0]
        return f"The number of red cards in the match is {red_cards}"

    else:
        return "Invalid query type. Please enter a valid query."

    # Close the connection to the SQLite database
    conn.close()

print(get_sports_data('teams_playing'))