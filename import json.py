#1.1 set up basic filter script by "orderInOffice"
import json

presidents = []

#1.1 filter for US Presidents
with open("People/A_people.json", 'r') as file:
    A_people= json.load(file)

for person in A_people:
    # Note: orderInOffice may not always be a list
    is_us_president = False
    if "ontology/orderInOffice" in person:
        for label in person["ontology/orderInOffice"]:
            if "President of the United States" in label:
                is_us_president = True

    # is_born_after_1855 = False
    # if "ontology/birthYear" in person:
    #     if type(person["ontology/birthYear"]) is list:
    #         year = int(person["ontology/birthYear"][0])
    #     else:
    #         year = int(person["ontology/birthYear"])
    #     if year > 1855:
    #         is_born_after_1855 = True
    
    
    if is_us_president:
        presidents.append(person)
        print(person["title"])
        
# with open("People/B_people.json", 'r') as file:
#     B_people= json.load(file)

# for person in B_people:
#     # Note: orderInOffice may not always be a list
#     if "ontology/orderInOffice" in person:
#         for label in person["ontology/orderInOffice"]:
#             if "President of the United States" in label:
#                 print(person["title"])
#                 presidents.append(person)

