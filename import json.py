#1.1 set up basic filter script by "orderInOffice"
import json

# [0-9]{1,2}[snrt][tdh]President

presidents = []

#1.1 filter for US Presidents

def filter(letter):
    with open(f'People/{letter}_people.json', 'r') as file:
        people = json.load(file)
        for person in people:
            #Check if president
            is_president = False
                #Check in ontology/orderInOffice
            if "ontology/orderInOffice" in person:
                if type(person["ontology/orderInOffice"]) is list:
                    for orderinoffice in person["ontology/orderInOffice"]:
                        if "President of the United States" in orderinoffice and \
                            "Vice President" not in orderinoffice and \
                            "Chief of Staff" not in orderinoffice:
                            is_president = True
                else:
                    if "President of the United States" in person["ontology/orderInOffice"] and \
                        "Vice President" not in person["ontology/orderInOffice"] and \
                        "Chief of Staff" not in person["ontology/orderInOffice"]:
                        is_president = True
                #Check in ontology/office
            if "ontology/office" in person:
                if type(person["ontology/office"]) is list:
                    for office in person["ontology/office"]:
                        if "President of the United States" in office and \
                            "Vice President" not in office:
                            is_president = True
                else:
                    if "President of the United States" in person["ontology/office"] and \
                        "Vice President" not in person["ontology/office"] and \
                        "Chief of Staff" not in person["ontology/office"]:
                        is_president = True
            #Check if american
            is_american = False
                #Check in ontology/birthPlace
            if "ontology/birthPlace" in person:
                if type(person["ontology/birthPlace"]) is list:
                    for birthplace in person["ontology/birthPlace"]:
                        if "http://dbpedia.org/resource/United_States" or "http://dbpedia.org/resource/British_America" in birthplace:
                            is_american = True
                else:
                    if "http://dbpedia.org/resource/United_States" or "http://dbpedia.org/resource/British_America" in person["ontology/birthPlace"]:
                        is_american = True
                #Check in ontology/nationality
            if "ontology/nationality" in person:
                if type(person["ontology/nationality"]) is list:
                    for nationality in person["ontology/nationality"]:
                        if "http://dbpedia.org/resource/United_States" in nationality:
                            is_american = True
                else:
                    if "http://dbpedia.org/resource/United_States" in person["ontology/nationality"]:
                        is_american = True
                #Check in ontology/country_label
            if "ontology/country_label" in person:
                if type(person["ontology/country_label"]) is list:
                    for country_label in person["ontology/country_label"]:
                        if "United States" in country_label:
                            is_american = True
                else:
                    if "United States" in person["ontology/country_label"]:
                        is_american = True
                #Check in ontology/restingPlace
            if "ontology/restingPlace" in person:
                if type(person["ontology/restingPlace"]) is list:
                    for restingPlace in person["ontology/restingPlace"]:
                        if "http://dbpedia.org/resource/Massachusetts" or "http://dbpedia.org/resource/Virginia" or "http://dbpedia.org/resource/New_York" or "http://dbpedia.org/resource/Tennessee" or "http://dbpedia.org/resource/Pennsylvania" or "http://dbpedia.org/resource/New_Hampshire" or "http://dbpedia.org/resource/New_Jersey" "http://dbpedia.org/resource/Ohio" or "http://dbpedia.org/resource/Indiana" or "http://dbpedia.org/resource/California" or "http://dbpedia.org/resource/Georgia" or "http://dbpedia.org/resource/Texas" or "http://dbpedia.org/resource/Missouri" in restingPlace:
                            is_american = True
                else:
                    if "http://dbpedia.org/resource/Massachusetts" in person["ontology/restingPlace"]:
                        is_american = True
            #Check if coloumbian
            is_coloumbian = False
                #Check in ontology/birthPlace
            if "ontology/nationality" in person:
                if type(person["ontology/nationality"]) is list:
                    for nationality in person["ontology/nationality"]:
                        if "http://dbpedia.org/resource/Colombians" in nationality:
                            is_coloumbian = True
                else:
                    if "http://dbpedia.org/resource/Colombians" in person["ontology/nationality"]:
                        is_coloumbian = True
            

            if is_president and is_american and not is_coloumbian:
                presidents.append(person)
                print(person["title"])

    # is_born_after_1855 = False
    # if "ontology/birthYear" in person:
    #     if type(person["ontology/birthYear"]) is list:
    #         year = int(person["ontology/birthYear"][0])
    #     else:
    #         year = int(person["ontology/birthYear"])
    #     if year > 1855:
    #         is_born_after_1855 = True
    

        
# with open("People/B_people.json", 'r') as file:
#     B_people= json.load(file)

# for person in B_people:
#     # Note: orderInOffice may not always be a list
#     if "ontology/orderInOffice" in person:
#         for label in person["ontology/orderInOffice"]:
#             if "President of the United States" in label:
#                 print(person["title"])
#                 presidents.append(person)

for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    filter(letter)

presidentstr = json.dumps(presidents)

with open('presidents.json', 'w', encoding='utf-8') as file:
    file.write(presidentstr)