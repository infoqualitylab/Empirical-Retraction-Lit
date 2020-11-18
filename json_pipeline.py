import json
#No additional action required; library json comes with Python, and users do not need to install the library themselves

infile = open('eppi_export_11.17.2020.json', 'r', encoding = 'utf-8')
export = json.load(infile)
infile.close()

bibliography = export["References"]


# print(bibliography[0]["Authors"])
print("Length of bibliography: ", len(bibliography))

#Make a list of all the author fields:
author_list = []

for record in range(0,(len(bibliography))):
  if bibliography[record]["Authors"] == "":
    author_list.append("No author listed")
  else:
    author_list.append(bibliography[record]["Authors"])
# print(author_list)
print("Length of author list: ", len(author_list))


#Make a new list of author fields, splitting each field where there are semicolons (turns semicolons into commas):
new_author_list = []

for record in author_list:
    if len(record.split(';')) > 0:
        au_names = []
        for each_au in record.split(';'):  #each_au is individual characters
            each_au = each_au.strip()
            if len(each_au) > 0:
                au_names.append(each_au) #au_names is individual authors

        # record = ', '.join(each_au)
    new_author_list.append(au_names)

# for ori, modified in zip(author_list, new_author_list):
#     print('{}\n{}\n\n'.format(ori, modified))


# print(new_author_list)
print("Length of new author list:", len(new_author_list))

#Put the new author list into the author fields in the bibliography:
for number in range(0,(len(bibliography))):
  bibliography[number]["Authors"] = new_author_list[number]


#Add "Publication" as type (needed for exhibit to work)
for number in range(0,len(bibliography)):
    bibliography[number]["type"] = ["Publication"]


#Add parentheses around Issue numbers
new_issue_list = []
for record in bibliography:
    if len(record["Issue"]) == 0:
        new_issue_list.append("")
    else:
        new_issue_list.append("(" + record["Issue"]+"),")

# print(new_issue_list)
print("Length of new issue list:",len(new_issue_list))

for number in range(0,(len(bibliography))):
  bibliography[number]["Issue"] = new_issue_list[number]


#Add period after page numbers
new_pages_list = []
for record in bibliography:
    if len(record["Pages"]) == 0:
        new_pages_list.append("")
    else:
        new_pages_list.append(record["Pages"]+".")

# print(new_pages_list)
print("Length of new pages list:",len(new_pages_list))

for number in range(0,(len(bibliography))):
  bibliography[number]["Pages"] = new_pages_list[number]

#Change key names to match index.html
for record in bibliography:
    record["label"] = record["Title"]
    del record["Title"]
    record["author"] = record["Authors"]
    del record["Authors"]
    record["id"] = record["ItemId"]
    del record["ItemId"]
    record["venue"] = record["ParentTitle"]
    del record["ParentTitle"]
    record["pub-type"] = record["TypeName"]
    del record["TypeName"]
    record["year"] = record["Year"]
    del record["Year"]

#Pull out artifact data extraction codes
for record in bibliography:
    if "Codes" in record:
        for item in record["Codes"]:
            if item["AttributeId"] == 6209644:
                record["Artifact"] = "Altmetrics to Retracted Papers"
            if item["AttributeId"] == 5655688:
                record["Artifact"] = "Citations to Retracted Papers"
            if item["AttributeId"] == 5655686:
                record["Artifact"] = "Instructions to Authors"
            if item["AttributeId"] == 5655684:
                record["Artifact"] = "Retraction Notices"
            if item["AttributeId"] == 5655685:
                record["Artifact"] = "Retracted Papers"
            if item["AttributeId"] == 5655687:
                record["Artifact"] = "Retraction Policies"

#Pull out method data extraction codes
for record in bibliography:
    if "Codes" in record:
        for item in record["Codes"]:
            if item["AttributeId"] == 5681698:
                record["Method"] = "Bibliometrics - Excluding Systematic Reviews"
            if item["AttributeId"] == 5681700:
                record["Method"] = "Citation Content Analysis"
            if item["AttributeId"] == 5681699:
                record["Method"] = "Content/Thematic Analysis"
            if item["AttributeId"] == 6280798:
                record["Method"] = "Econometrics"
            if item["AttributeId"] == 6306062:
                record["Method"] = "Financial Estimation"
            if item["AttributeId"] == 5717740:
                record["Method"] = "Formal, Systematic Review of the Literature"
            if item["AttributeId"] == 5681702:
                record["Method"] = "Handsearching"
            if item["AttributeId"] == 5681701:
                record["Method"] = "Interviews"
            if item["AttributeId"] == 6145390:
                record["Method"] = "Psychology Experiment"
            if item["AttributeId"] == 5681697:
                record["Method"] = "Survey"


#Write out to new json file
with open('publications_11.17.2020.json', 'w') as json_file:
  json.dump({"items": bibliography}, json_file)




