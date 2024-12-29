from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_recommend_breeds"

    @staticmethod
    def load_breeds() -> List[Dict]:
        df = pd.read_csv("./db/dog-breeds.csv")

        breeds = []

        for index, row in list(df.iterrows()):
            breeds.append(dict(row))

        return breeds

    @staticmethod
    def load_preferences(tracker) -> Dict:
        adoption_reason = tracker.get_slot("adoption_reason")
        age_preference = tracker.get_slot("age_preference")
        allergies_present = tracker.get_slot("allergies_present")
        time_commitment = tracker.get_slot("time_commitment")
        budget_limit = tracker.get_slot("budget_limit")
        children_at_home = tracker.get_slot("children_at_home")
        home_type = tracker.get_slot("home_type")
        climate_type = tracker.get_slot("climate_type")
        size_preference = tracker.get_slot("size_preference")
        lifestyle = tracker.get_slot("lifestyle")
        temperament_preference = tracker.get_slot("temperament_preference")

        preferences = {
            "adoption_reason": adoption_reason,
            "age_preference": age_preference,
            "allergies_present": allergies_present,
            "time_commitment": time_commitment,
            "budget_limit": budget_limit,
            "children_at_home": children_at_home,
            "home_type": home_type,
            "climate_type": climate_type,
            "size_preference": size_preference,
            "lifestyle": lifestyle,
            "temperament_preference": temperament_preference,
        }

        return preferences

    @staticmethod
    def calculate_scores(dog_breeds, preferences):
        scores = []
        for breed in dog_breeds:
            score = 0

            # Match adoption reason (security preference scores high for confident or independent breeds)
            if preferences['adoption_reason'] == "security" and breed['TEMPERAMENT'] in ["confident",
                                                                                              "independent"]:
                score += 10
            elif preferences['adoption_reason'] == "family" and breed['TEMPERAMENT'] in ["friendly", "adaptable"]:
                score += 10
            elif preferences['adoption_reason'] == "lifestyle" and breed['TEMPERAMENT'] in ["independent",
                                                                                                 "adaptable"]:
                score += 10

            # Match age preference (younger age aligns with active and adaptable temperaments)
            if preferences['age_preference'] == "young" and breed['EXERCISE'] in ["medium", "hard"]:
                score += 10
            elif preferences['age_preference'] == "middle" and breed['EXERCISE'] == "medium":
                score += 10
            elif preferences['age_preference'] == "old" and breed['EXERCISE'] == "easy":
                score += 10

            # Match allergies present (easy grooming favored for mild/severe allergies)
            if preferences['allergies_present'] in ["mild", "severe"] and breed['GROOMING'] == "easy":
                score += 10

            # Match time commitment (easy grooming and exercise align with low commitment)
            if preferences['time_commitment'] == "low" and breed['EXERCISE'] == "easy" and breed[
                'GROOMING'] == "easy":
                score += 10
            elif preferences['time_commitment'] == "moderate" and breed['EXERCISE'] in ["easy", "medium"] and \
                    breed['GROOMING'] in ["easy", "medium"]:
                score += 10
            elif preferences['time_commitment'] == "high" and breed['EXERCISE'] == "hard":
                score += 10

            # Match budget limit (easy feeding aligns with low budget)
            if preferences['budget_limit'] == "low" and breed['FEEDING'] == "easy":
                score += 10
            elif preferences['budget_limit'] == "moderate" and breed['FEEDING'] in ["easy", "medium"]:
                score += 10

            # Match children at home (friendly and adaptable breeds favored for young children)
            if preferences['children_at_home'] == "young" and breed['TEMPERAMENT'] in ["friendly", "adaptable"]:
                score += 10
            elif preferences['children_at_home'] == "grown" and breed['TEMPERAMENT'] in ["confident",
                                                                                              "independent"]:
                score += 10

            # Match home type (large dogs for large houses, small dogs for apartments)
            if preferences['home_type'] == "apartment" and breed['SIZE'] == "small":
                score += 10
            elif preferences['home_type'] == "large_house" and breed['SIZE'] in ["medium", "large"]:
                score += 10

            # Match climate type (specific sizes or temperaments may align with climate)
            if preferences['climate_type'] in ["cold", "dry"] and breed['SIZE'] in ["medium", "large"]:
                score += 10
            elif preferences['climate_type'] in ["hot", "humid"] and breed['GROOMING'] == "easy":
                score += 10
            elif preferences['climate_type'] == "mild":
                score += 10

            # Match size preference
            if preferences['size_preference'] != "any" and breed['SIZE'] == preferences['size_preference']:
                score += 10

            # Match lifestyle (active aligns with hard/medium exercise, relaxed with easy)
            if preferences['lifestyle'] == "active" and breed['EXERCISE'] in ["medium", "hard"]:
                score += 10
            elif preferences['lifestyle'] == "relaxed" and breed['EXERCISE'] == "easy":
                score += 10

            # Match temperament preference
            if preferences['temperament_preference'] != "any" and breed['TEMPERAMENT'] == preferences[
                'temperament_preference']:
                score += 10

            # Append breed and score
            scores.append({"breed": breed['BREED'], "score": score, "description": breed['DESCRIPTION']})

        # Sort breeds by score in descending order
        return sorted(scores, key=lambda x: x['score'], reverse=True)

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Calculate and dispatch recommendations
        dog_breeds = self.load_breeds()
        user_preferences = self.load_preferences(tracker)
        recommendations = self.calculate_scores(dog_breeds, user_preferences)

        rec_breed_0 = recommendations[0]["breed"]
        rec_breed_1 = recommendations[1]["breed"]
        rec_breed_2 = recommendations[2]["breed"]

        message = f"Here are some great matches for you:\n- {rec_breed_0}\n- {rec_breed_1}\n- {rec_breed_2}"
        dispatcher.utter_message(text=message)

        return []
