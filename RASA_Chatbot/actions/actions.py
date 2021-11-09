# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import re
from dateutil.parser import parse
from datetime import datetime, timedelta


#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

def location_confirm(location):
    url = "https://api.rootnet.in/covid19-in/stats/history"
    data = requests.get(url)
    data_json = data.json()['data']
    total_cases = 0
    for i in data_json:
        for detail in i['regional']:
            if re.search(location, detail['loc'], re.IGNORECASE):
                total_cases += detail['totalConfirmed']
    return total_cases


class ActionHelloLoc(Action):

    def name(self) -> Text:
        return "action_city_cases"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # print("tracker slots ", tracker.slots)
        states = [state['value'] for state in tracker.latest_message['entities']]
        # slot_name = tracker.get_slot("city")
        states = list(set(states))
        total_confirmed = 0
        for i in states:
            total_confirmed += location_confirm(i)

        message = "Total confirmed cases for states  " + " , ".join(states) + " altogether is " + str(total_confirmed)
        dispatcher.utter_message(
            text=message)

        return []


class ActionHelloLoc(Action):

    def name(self) -> Text:
        return "action_city_cases_separate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # print("tracker slots ", tracker.slots)
        states = [state['value'] for state in tracker.latest_message['entities']]
        # slot_name = tracker.get_slot("city")
        states = list(set(states))
        message = ""
        for i in states:
            message += "Total Confirmed cases for " + i + " is " + str(location_confirm(i)) + "\n"

        dispatcher.utter_message(
            text=message)

        return []


class ActionDateCases(Action):

    def name(self) -> Text:
        return "action_date_cases"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # print("tracker entity ", tracker.latest_message['entities'])
        tracker_dates = tracker.latest_message['entities']
        dates = []
        for i in tracker_dates:
            if i['extractor'] == "RegexEntityExtractor" and i['entity'] == 'date':
                dates.append(i['value'])

        if len(dates) == 1:
            date1 = dates[0]
            data_dates = to_from_cases(date1)
            message = "Total cases on date " + date1 + " are " + str(data_dates)
        elif len(dates) == 2:
            date1 = dates[0]
            date2 = dates[1]
            data_dates = to_from_cases(date1, date2)
            if data_dates == -1:
                message = "Invalid date format ..try with different one!"
            else:
                message = "Total cases b/w  " + date1 + " and " + date2 + " are " + str(data_dates)
        else:
            message = "Invalid date format ..Please try with different one"
        dispatcher.utter_message(
            text=message)

        return []


def to_from_cases(date1, date2=None):
    #     from_date=datetime.strptime(date1,"%d %b %Y")
    #     to_date=datetime.strptime(date2,"%d %b %Y")
    list_days_bet = []
    if date2 is not None:
        try:
            from_date = parse(date1)
            to_date = parse(date2)
        except:
            return -1
        delta = to_date - from_date  # as timedelta

        for i in range(delta.days + 1):
            day = (from_date + timedelta(days=i)).strftime('%Y-%m-%d')
            list_days_bet.append(day)
        if len(list_days_bet) == 0:
            return -1
    else:
        try:
            from_date = parse(date1)
        except:
            return -1
        list_days_bet = [from_date.strftime('%Y-%m-%d')]
    total_confirmed = 0
    url = "https://api.rootnet.in/covid19-in/stats/history"

    data = requests.get(url)
    data_json = data.json()['data']
    for item in data_json:
        if item['day'] in list_days_bet:
            total_confirmed += item['summary']['confirmedCasesIndian'] + item['summary']['confirmedCasesForeign']
    return total_confirmed

