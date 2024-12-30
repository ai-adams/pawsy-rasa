from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionStateTracker(Action):

    def name(self) -> Text:
        return "action_state_tracker"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        prev_intent = tracker.get_intent_of_latest_message()

        if "faq_" in prev_intent:
            faq_count = tracker.get_slot("faq_count")
            faq_count += 1

            # Toggle upsell_signup every three user messages
            if (faq_count // 2) % 3 == 0:  # Divide by 2 because the function is called twice per user message
                upsell_signup = True
            else:
                upsell_signup = False

            return [SlotSet("faq_count", faq_count), SlotSet("upsell_signup", upsell_signup)]

        else:
            return []
