import sqlite3
from typing import Dict, Any, Text, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionTeamsPlaying(Action):
    def name(self) -> Text:
        return "action_teams_playing"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Connect to the SQLite database
        try:
            conn = sqlite3.connect('sports_data.db')
            cursor = conn.cursor()

            # Get the teams playing from the database
            cursor.execute("SELECT Match FROM sports_data LIMIT 1")
            teams_playing = cursor.fetchone()[0]

            # Respond to the user with the teams playing
            dispatcher.utter_message(text=f"The teams playing today are: {teams_playing}")

        except Exception as e:
            print(e)
            dispatcher.utter_message(text="Sorry, something went wrong.")

        finally:
            # Close the connection to the SQLite database
            conn.close()

        return []
    

class ActionCurrentScore(Action):
    def name(self) -> Text:
        return "action_current_score"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Connect to the SQLite database
        try:
            conn = sqlite3.connect('sports_data.db')
            cursor = conn.cursor()

            # Get the current score from the database
            cursor.execute("SELECT Score FROM sports_data LIMIT 1")
            current_score = cursor.fetchone()[0]

            # Respond to the user with the current score
            dispatcher.utter_message(text=f"The current score is {current_score}")

        except Exception as e:
            print(e)
            dispatcher.utter_message(text="Sorry, something went wrong.")

        finally:
            # Close the connection to the SQLite database
            conn.close()

        return []


class ActionGoalScorers(Action):
    def name(self) -> Text:
        return "action_goal_scorers"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Connect to the SQLite database
        try:
            conn = sqlite3.connect('sports_data.db')
            cursor = conn.cursor()

            # Get the goal scorers from the database
            cursor.execute("SELECT Goal_Scorers FROM sports_data LIMIT 1")
            goal_scorers = cursor.fetchone()[0]

            # Respond to the user with the goal scorers
            dispatcher.utter_message(text=f"The goal scorers for today's match are: {goal_scorers}")

        except Exception as e:
            print(e)
            dispatcher.utter_message(text="Sorry, something went wrong.")

        finally:
            # Close the connection to the SQLite database
            conn.close()

        return []

class ActionGetMatchLocation(Action):
    def name(self) -> Text:
        return "action_match_location"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Connect to the SQLite database
        conn = sqlite3.connect('sports_data.db')
        cursor = conn.cursor()

        cursor.execute("SELECT Location FROM sports_data LIMIT 1")
        location = cursor.fetchone()[0]
        dispatcher.utter_message(text=f"The match is being played at {location}")

        # Close the connection to the SQLite database
        conn.close()

        return []

class ActionGetMatchDate(Action):
    def name(self) -> Text:
        return "action_match_date"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Connect to the SQLite database
        conn = sqlite3.connect('sports_data.db')
        cursor = conn.cursor()

        cursor.execute("SELECT Date FROM sports_data LIMIT 1")
        date = cursor.fetchone()[0]
        dispatcher.utter_message(text=f"The match date is {date}")

        # Close the connection to the SQLite database
        conn.close()

        return []
    
class ActionGetMatchTime(Action):
    def name(self) -> Text:
        return "action_match_time"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Connect to the SQLite database
        conn = sqlite3.connect('sports_data.db')
        cursor = conn.cursor()

        # Execute the SQL query
        cursor.execute("SELECT Time FROM sports_data")
        time = cursor.fetchone()[0]

        # Close the connection to the SQLite database
        conn.close()

        dispatcher.utter_message(text=f"The match time is: {time}")

        return []




class ActionFirstHalfGoals(Action):
    def name(self) -> Text:
        return "action_first_half_goals"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conn = sqlite3.connect('sports_data.db')
        cursor = conn.cursor()

        cursor.execute("SELECT First_Half_Goals FROM sports_data LIMIT 1")
        first_half_goals = cursor.fetchone()[0]

        dispatcher.utter_message(text=f"The number of goals scored in the first half is {first_half_goals}")

        conn.close()

        return []

class ActionSecondHalfGoals(Action):
    def name(self) -> Text:
        return "action_second_half_goals"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conn = sqlite3.connect('sports_data.db')
        cursor = conn.cursor()

        cursor.execute("SELECT Second_Half_Goals FROM sports_data LIMIT 1")
        second_half_goals = cursor.fetchone()[0]

        dispatcher.utter_message(text=f"The number of goals scored in the second half is {second_half_goals}")

        conn.close()

        return []

class ActionGetYellowCards(Action):
    def name(self) -> Text:
        return "action_yellow_cards"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Connect to the SQLite database
        conn = sqlite3.connect('sports_data.db')
        cursor = conn.cursor()

        # Execute the SQL query
        cursor.execute("SELECT Yellow_Cards FROM sports_data")
        yellow_cards = cursor.fetchone()[0]

        # Close the connection to the SQLite database
        conn.close()

        dispatcher.utter_message(text=f"The number of yellow cards in the match is: {yellow_cards}")

        return []
class ActionRedCards(Action):
    def name(self) -> Text:
        return "action_red_cards"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conn = sqlite3.connect('sports_data.db')
        cursor = conn.cursor()

        cursor.execute("SELECT Red_Cards FROM sports_data LIMIT 1")
        red_cards = cursor.fetchone()[0]

        dispatcher.utter_message(text=f"The number of red cards in the match is {red_cards}")

        conn.close()

        return []
