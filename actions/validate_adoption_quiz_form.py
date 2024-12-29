from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ValidateAdoptionQuizForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_adoption_quiz_form"

    def validate_start_quiz(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        slot_keys = list(tracker.slots_to_validate().keys())
        if len(slot_keys) > 1:
            return {}

        else:
            slot_key = list(tracker.slots_to_validate().keys())[0]

            if slot_key == "start_quiz" and slot_value in [True, False]:
                return {"start_quiz": slot_value}

            else:
                return {"start_quiz": None}

    def validate_adoption_reason(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        slot_keys = list(tracker.slots_to_validate().keys())
        if len(slot_keys) > 1:
            return {}

        else:
            slot_key = list(tracker.slots_to_validate().keys())[0]

            if slot_key == "adoption_reason" and slot_value in ["family", "lifestyle", "security", "other"]:

                if slot_value == "family":
                    dispatcher.utter_message(response="utter_ack_adoption_reason_family")

                elif slot_value == "lifestyle":
                    dispatcher.utter_message(response="utter_ack_adoption_reason_lifestyle")

                elif slot_value == "security":
                    dispatcher.utter_message(response="utter_ack_adoption_reason_security")

                else:
                    dispatcher.utter_message(response="utter_ack_misc_1")

                return {
                    "adoption_reason": slot_value
                }

            else:
                return {"adoption_reason": None}

    def validate_age_preference(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        slot_keys = list(tracker.slots_to_validate().keys())
        if len(slot_keys) > 1:
            return {}

        else:
            slot_key = list(tracker.slots_to_validate().keys())[0]

            if slot_key == "age_preference" and slot_value in ["young", "middle", "old", "any"]:

                if slot_value == "young":
                    dispatcher.utter_message(response="utter_ack_age_preference_young")

                elif slot_value == "middle":
                    dispatcher.utter_message(response="utter_ack_age_preference_middle")

                elif slot_value == "old":
                    dispatcher.utter_message(response="utter_ack_age_preference_old")

                else:
                    dispatcher.utter_message(response="utter_ack_misc_2")

                return {"age_preference": slot_value}

            else:
                return {"age_preference": None}

    def validate_allergies_present(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        slot_keys = list(tracker.slots_to_validate().keys())
        if len(slot_keys) > 1:
            return {}

        else:
            slot_key = list(tracker.slots_to_validate().keys())[0]

            if slot_key == "allergies_present" and slot_value in ["severe", "mild", "none", "unsure"]:

                if slot_value == "severe":
                    dispatcher.utter_message(response="utter_ack_allergies_present_severe")

                elif slot_value == "mild":
                    dispatcher.utter_message(response="utter_ack_allergies_present_mild")

                elif slot_value == "none":
                    dispatcher.utter_message(response="utter_ack_allergies_present_none")

                else:
                    dispatcher.utter_message(response="utter_ack_misc_3")

                return {"allergies_present": slot_value}

            else:
                return {"allergies_present": None}

    def validate_time_commitment(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        slot_keys = list(tracker.slots_to_validate().keys())
        if len(slot_keys) > 1:
            return {}

        else:
            slot_key = list(tracker.slots_to_validate().keys())[0]

            if slot_key == "time_commitment" and slot_value in ["high", "moderate", "low", "varies"]:

                if slot_value == "high":
                    dispatcher.utter_message(response="utter_ack_time_commitment_high")

                elif slot_value == "moderate":
                    dispatcher.utter_message(response="utter_ack_time_commitment_moderate")

                elif slot_value == "low":
                    dispatcher.utter_message(response="utter_ack_time_commitment_low")

                else:
                    dispatcher.utter_message(response="utter_ack_misc_4")

                return {"time_commitment": slot_value}

            else:
                return {"time_commitment": None}

    def validate_budget_limit(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        slot_keys = list(tracker.slots_to_validate().keys())
        if len(slot_keys) > 1:
            return {}

        else:
            slot_key = list(tracker.slots_to_validate().keys())[0]

            if slot_key == "budget_limit" and slot_value in ["low", "moderate", "high", "unsure"]:

                if slot_value == "low":
                    dispatcher.utter_message(response="utter_ack_budget_limit_low")

                elif slot_value == "moderate":
                    dispatcher.utter_message(response="utter_ack_budget_limit_moderate")

                elif slot_value == "high":
                    dispatcher.utter_message(response="utter_ack_budget_limit_high")

                else:
                    dispatcher.utter_message(response="utter_ack_misc_5")

                return {"budget_limit": slot_value}

            else:
                return {"budget_limit": None}

    def validate_children_at_home(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        slot_keys = list(tracker.slots_to_validate().keys())
        if len(slot_keys) > 1:
            return {}

        else:
            slot_key = list(tracker.slots_to_validate().keys())[0]

            if slot_key == "children_at_home" and slot_value in ["grown", "young", "none", "other"]:

                if slot_value == "grown":

                    dispatcher.utter_message(response="utter_ack_children_at_home_grown")

                elif slot_value == "young":
                    dispatcher.utter_message(response="utter_ack_children_at_home_young")

                elif slot_value == "none":
                    dispatcher.utter_message(response="utter_ack_children_at_home_none")

                else:
                    dispatcher.utter_message(response="utter_ack_misc_6")

                return {"children_at_home": slot_value}

            else:
                return {"children_at_home": None}

    def validate_home_type(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        slot_keys = list(tracker.slots_to_validate().keys())
        if len(slot_keys) > 1:
            return {}

        else:
            slot_key = list(tracker.slots_to_validate().keys())[0]

            if slot_key == "home_type" and slot_value in ["apartment", "small_house", "large_house", "other"]:

                if slot_value == "apartment":
                    dispatcher.utter_message(response="utter_ack_home_type_apartment")

                elif slot_value == "small_house":
                    dispatcher.utter_message(response="utter_ack_home_type_small_house")

                elif slot_value == "large_house":
                    dispatcher.utter_message(response="utter_ack_home_type_large_house")

                else:
                    dispatcher.utter_message(response="utter_ack_misc_7")

                return {"home_type": slot_value}

            else:
                return {"home_type": None}

    def validate_climate_type(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        slot_keys = list(tracker.slots_to_validate().keys())
        if len(slot_keys) > 1:
            return {}

        else:
            slot_key = list(tracker.slots_to_validate().keys())[0]

            if slot_key == "climate_type" and slot_value in ["cold", "dry", "hot", "humid", "mild", "other"]:

                if slot_value == "cold":
                    dispatcher.utter_message(response="utter_ack_climate_type_cold")

                elif slot_value == "dry":
                    dispatcher.utter_message(response="utter_ack_climate_type_dry")

                elif slot_value == "hot":
                    dispatcher.utter_message(response="utter_ack_climate_type_hot")

                elif slot_value == "humid":
                    dispatcher.utter_message(response="utter_ack_climate_type_humid")

                elif slot_value == "mild":
                    dispatcher.utter_message(response="utter_ack_climate_type_mild")

                else:
                    dispatcher.utter_message(response="utter_ack_misc_8")

                return {"climate_type": slot_value}

            else:
                return {"climate_type": None}

    def validate_size_preference(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        slot_keys = list(tracker.slots_to_validate().keys())
        if len(slot_keys) > 1:
            return {}

        else:
            slot_key = list(tracker.slots_to_validate().keys())[0]

            if slot_key == "size_preference" and slot_value in ["small", "medium", "large", "any"]:

                if slot_value == "small":
                    dispatcher.utter_message(response="utter_ack_size_preference_small")

                elif slot_value == "medium":
                    dispatcher.utter_message(response="utter_ack_size_preference_medium")

                elif slot_value == "large":
                    dispatcher.utter_message(response="utter_ack_size_preference_large")

                else:
                    dispatcher.utter_message(response="utter_ack_misc_9")

                return {"size_preference": slot_value}

            else:
                return {"size_preference": None}

    def validate_lifestyle(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        slot_keys = list(tracker.slots_to_validate().keys())
        if len(slot_keys) > 1:
            return {}

        else:
            slot_key = list(tracker.slots_to_validate().keys())[0]

            if slot_key == "lifestyle" and slot_value in ["active", "balanced", "relaxed", "other"]:

                if slot_value == "active":
                    dispatcher.utter_message(response="utter_ack_lifestyle_active")

                elif slot_value == "balanced":
                    dispatcher.utter_message(response="utter_ack_lifestyle_balanced")

                elif slot_value == "relaxed":
                    dispatcher.utter_message(response="utter_ack_lifestyle_relaxed")

                else:
                    dispatcher.utter_message(response="utter_ack_misc_10")

                return {"lifestyle": slot_value}

            else:
                return {"lifestyle": None}

    def validate_temperament_preference(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        slot_keys = list(tracker.slots_to_validate().keys())
        if len(slot_keys) > 1:
            return {}

        else:
            slot_key = list(tracker.slots_to_validate().keys())[0]

            if slot_key == "temperament_preference" and slot_value in ["friendly", "confident", "independent", "adaptable", "any"]:

                if slot_value == "friendly":
                    dispatcher.utter_message(response="utter_ack_temperament_preference_friendly")

                elif slot_value == "confident":
                    dispatcher.utter_message(response="utter_ack_temperament_preference_confident")

                elif slot_value == "independent":
                    dispatcher.utter_message(response="utter_ack_temperament_preference_independent")

                elif slot_value == "adaptable":
                    dispatcher.utter_message(response="utter_ack_temperament_preference_adaptable")

                else:
                    dispatcher.utter_message(response="utter_ack_misc_11")

                return {"temperament_preference": slot_value}

            else:
                return {"temperament_preference": None}