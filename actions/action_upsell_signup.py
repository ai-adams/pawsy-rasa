from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random

upsell_signup_messages = {
    "faq_about_pet_parenting": [
        "Want personalized advice tailored to your pet? Sign up for Pet Portal today and elevate your pet parenting journey!",
        "Ready to take pet parenting to the next level? Sign up for Pet Portal today for personalized guidance and support!",
        "Need help on your pet parenting journey? Sign up for Pet Portal today for expert advice tailored to your pet’s needs!"
    ],
    "faq_about_pet_portal": [
        "Want advice tailored to your pet? Sign up today and experience personalized care with Pet Portal AI!",
        "Ready to see what Pet Portal can do for you? Sign up today for personalized support!",
        "Sign up today and discover how Pet Portal AI can support you on your pet parenting journey!"
    ],
    "faq_behavior_and_diet": [
        "For advice tailored to your pet’s unique needs, sign up for Pet Portal today and take the guesswork out of behavior and diet management!  ",
        "Want personalized tips for your pet? Sign up today and start your journey toward better behavior and diet management!  ",
        "Need guidance tailored to your pet’s needs? Sign up for Pet Portal today and gain personalized insights into their behavior and diet!  "
    ],
    "faq_benefits_of_pet_parenting": [
        "Want to enhance your pet parenting journey? Sign up for Pet Portal today for personalized guidance and support!",
        "Ready to experience the full benefits of pet parenting? Sign up for Pet Portal today and get expert insights tailored to your journey!",
        "Sign up for Pet Portal today to access personalized advice and make the most of your pet parenting experience!"
    ],
    "faq_benefits_of_pet_portal": [
        "Want tailored advice for your furry friend? Sign up for Pet Portal today and experience the difference!",
        "Ready to elevate your pet parenting experience? Sign up for Pet Portal today and get started!",
        "Sign up today and discover the benefits of tailored pet care!"
    ],
    "faq_community_and_feedback": [
        "Want to join the conversation and make an impact? Sign up for Pet Portal today and start connecting with our community!",
        "Ready to engage with fellow pet parents and contribute? Sign up for Pet Portal today and get involved!",
        "Want to be part of the journey? Sign up for Pet Portal today and join our vibrant community!"
    ],
    "faq_expert_support": [
        "Want personalized, expert-backed advice? Sign up for Pet Portal today and take your pet care to the next level!",
        "Ready to access expert-guided insights tailored to your pet? Sign up for Pet Portal today and start your journey with confidence!",
        "Sign up for Pet Portal today and discover expert-backed support tailored to your pet’s needs!"
    ],
    "faq_features_overview": [
        "Want to explore these features for your pet? Sign up today and experience the difference!",
        "Sign up for Pet Portal today and discover how these tools can transform pet care!",
        "Sign up today and see how these features can make pet parenting stress-free and rewarding!"
    ],
    "faq_getting_started_with_pet_portal": [
        "Ready to simplify your pet care routine? Sign up for Pet Portal today and take the first step toward smarter, stress-free pet parenting!",
        "Want to make pet parenting easier and more personalized? Sign up for Pet Portal today and begin your journey with confidence!",
        "Ready to get started? Sign up for Pet Portal today and explore the future of personalized pet care!"
    ],
    "faq_health_guidance": [
        "Want advice customized for your pet’s health? Sign up for Pet Portal today and start your journey to better pet wellbeing!",
        "Sign up for Pet Portal today and discover tailored solutions for your pet’s wellbeing!",
        "Take the guesswork out of pet care—sign up for Pet Portal today and get personalized health advice designed just for your furry companion!"
    ],
    "faq_how_pet_portal_works": [
        "Want to see it in action? Sign up for Pet Portal today and experience smarter, stress-free pet care!",
        "Ready to get started? Sign up for Pet Portal today for a more personalized experience!",
        "Sign up for Pet Portal today and discover how easy pet parenting can be with personalized support!"
    ],
    "faq_pricing_and_plans": [
        "Ready to find the plan that works for you? Sign up for Pet Portal today and start exploring personalized pet care!",
        "With no long-term commitment, you can adjust or cancel anytime. Sign up for Pet Portal today and discover the plan that’s perfect for you!",
        "Sign up today and experience personalized pet care at the level you choose!"
    ],
    "faq_real_stories": [
        "Want to experience similar results? Sign up for Pet Portal today and see the difference personalized pet care can make!",
        "Ready to create your own success story? Sign up for Pet Portal today and discover how it can help you and your pet thrive!",
        "Want to be the next success story? Sign up for Pet Portal today and start your journey to smarter pet care!"
    ],
    "faq_shelters_and_adoptions": [
        "Ready to make a difference? Sign up for Pet Portal today and start your journey with your adopted pet!",
        "Want to join the mission? Sign up for Pet Portal today and make adoption easier and more rewarding!",
        "Sign up for Pet Portal today and make a lasting impact on shelter animals and your adopted pet!"
    ],
    "faq_supported_pets": [
        "Want to see how Pet Portal can help your pet thrive? Sign up today and experience personalized care for your furry friend!",
        "Ready to give your pet the personalized attention they deserve? Sign up for Pet Portal today and start your journey!",
        "Want to unlock personalized insights for your pet today? Sign up for Pet Portal now and see the difference!"
    ],
    "faq_technical_information": [
        "Have technical concerns or questions? Sign up for Pet Portal today and explore a secure, reliable platform tailored to your pet’s needs!",
        "Sign up today and enjoy a secure, tech-friendly way to care for your pet!",
        "Ready to see it in action? Sign up for Pet Portal today and experience a secure, cutting-edge platform built for pet parents!"
    ]
}

class ActionUpsellSignup(Action):

    def name(self) -> Text:
        return "action_upsell_signup"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        prev_intent = tracker.get_intent_of_latest_message()
        upsell_signup = tracker.get_slot("upsell_signup")

        if upsell_signup:
            try:
                upsell_message = random.choice(upsell_signup_messages[prev_intent])
                dispatcher.utter_message(text=upsell_message)

            except KeyError:
                pass

        return []
