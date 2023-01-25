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
            #Check if bullshit
            is_bs = False
                #Check in title
            if "title" in person:
                if "Ed_Kealty" in person["title"]:
                    is_bs = True
                if "_of_" in person["title"]:
                    is_bs = True
                if "presidential" in person["title"]:
                    is_bs = True
                if "_and_" in person["title"]:
                    is_bs = True
                if "controversy" in person["title"]:
                    is_bs = True
                if "Sunil" in person["title"]:
                    is_bs = True
                if "Santos" in person["title"]:
                    is_bs = True
            if is_president and is_american and not is_coloumbian and not is_bs:
                presidents.append(person)
                print(person["title"])

for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    filter(letter)

with open('presidents.json', 'w', encoding='utf-8') as file:
    json.dump(presidents, file)

with open('presidents.csv', 'w', encoding='utf-8') as file:
   file.write(f'president, education, party_label\n')
   for president in presidents:
       first_university = None
       first_party= None
       if "ontology/almaMater_label" in president:
            if type(president["ontology/almaMater_label"]) is list:
                first_university = president["ontology/almaMater_label"][0]
            else:
                first_university = president["ontology/almaMater_label"]
       if "ontology/party_label" in president:
            if type(president["ontology/party_label"]) is list:
                first_party = president["ontology/party"][0]
            else:
                first_party = president["ontology/party_label"]
       file.write(f'{first_university}, {president["title"]}, {first_party}\n')