#1.1 set up basic filter script by "orderInOffice"
import json

presidents = []

#1.1 filter for US Presidents
with open("People/B_people.json", 'r') as file:
    B_people= json.load(file)

for person in B_people:
    # Note: orderInOffice may not always be a list
    if "ontology/orderInOffice" in person:
        for label in person["ontology/orderInOffice"]:
            if "President of the United States" in label:
                print(person)
                presidents.append(person)