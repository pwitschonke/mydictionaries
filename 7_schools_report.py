"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons. This
information can be found in the ValueLabels file.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 75%
Display report for all universities that have a total price for in-state students living off campus over $50,000

"""

import json

infile = open("school_data.json", "r")

schools = json.load(infile)
conferenceSchools = [372, 108, 107, 130]

# How many schools are in this file? #
#print(len(schools))


# Display report for all universities that have a graduation rate for Women over 75% #
print("Schools with a graduation rate of 75% or higher for women:")

for i in schools:
    if i["NCAA"]["NAIA conference number football (IC2020)"] in conferenceSchools:
        if i["Graduation rate  women (DRVGR2020)"] > 75:
            print(i["instnm"])

# Display report for all universities that have a total price for in-state students living off campus over $50,000 #
print("\nSchools that have a total price for in-state students living off campus over $50,000:")

for i in schools:
    if i["NCAA"]["NAIA conference number football (IC2020)"] in conferenceSchools:
        temp = i["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"]
        if temp:
            if temp > 50000:
                print(i["instnm"])

