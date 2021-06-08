# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import csv

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_productos"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        with open('vinos.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';', quotechar=';')
            salida = " "
            for row in spamreader:
                salida = salida.join(", ").join(row)
            print("salida: ", salida)
            dispatcher.utter_message(text="Los vinos que manejamos son: " + salida + ". Para mayor informacion visita www.vinos.com/productos")

        return []
