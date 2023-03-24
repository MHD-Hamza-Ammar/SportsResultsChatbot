import sqlite3

def create_database_and_insert_data():
    # Connect to the SQLite database (if it doesn't exist, it will be created)
    conn = sqlite3.connect('sports_data.db')
    cursor = conn.cursor()

    # Create the sports_data table
    cursor.execute('''CREATE TABLE sports_data (
                        id INTEGER PRIMARY KEY,
                        Match TEXT,
                        Score TEXT,
                        Goal_Scorers TEXT,
                        Location TEXT,
                        Date TEXT,
                        Time TEXT,
                        First_Half_Goals INTEGER,
                        Second_Half_Goals INTEGER,
                        Yellow_Cards INTEGER,
                        Red_Cards INTEGER
                    )''')

    # Insert sample data into the sports_data table
    sample_data = (1, 'Team A vs Team B', '2-1', 'Player 1, Player 2, Player 3', 'Stadium X', '2023-03-21', '19:00', 2, 1, 3, 0)
    cursor.execute("INSERT INTO sports_data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", sample_data)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Call the function to create the database and insert the sample data
create_database_and_insert_data()