import json
#No additional action required; library json comes with Python, and users do not need to install the library themselves

infile = open('/Users/randiproescholdt/Documents/RA/Sloan/Exhibit/Exhibit - Github Archive v.2.1/eppi_export_386.json', 'r', encoding = 'utf-8')
export = json.load(infile)
infile.close()

bibliography = export["References"]
codesets = export["CodeSets"]

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


#Add http://doi.org/ to DOIs; print out list of those missing DOIs
new_doi_list = []

for record in bibliography:
    if len(record["DOI"]) == 0:
        new_doi_list.append("")
    else:
        new_doi_list.append("http://doi.org/" + record["DOI"])

print("Length of new DOI list:",len(new_doi_list))

for number in range(0,(len(bibliography))):
    if bibliography[number]["DOI"] != "":
        bibliography[number]["DOI"] = new_doi_list[number]
    else:
        print("No DOI:" + bibliography[number]["Authors"][0] + ", " + bibliography[number]["Title"])
        del bibliography[number]["DOI"] #Take out empty DOI field so link to nowhere doesn't appear

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

##DATA EXTRACTION

attributes_dict = codesets[0]["Attributes"]
attributes_list = attributes_dict["AttributesList"]


attribute_name_list = []
for number in range(0,len(attributes_list)):
    attribute_name_list.append(attributes_list[number]["AttributeName"])
# print(attribute_name_list)

new_letter_list = []
new_attribute_name_list = []

for field_name in attribute_name_list:
    for letter in field_name.strip():
        if letter == " ":
            new_letter_list.append("_")
        elif letter == "(":
            # new_letter_list.append("&#40;")
            new_letter_list.append("")
        elif letter == ")":
            # new_letter_list.append("&#41;")
            new_letter_list.append("")
        elif letter == "?":
            # new_letter_list.append("&#63;")
            new_letter_list.append("")
        elif letter == ",":
            new_letter_list.append("")
        else:
            new_letter_list.append(letter)
    new_word = ''.join(new_letter_list)
    new_attribute_name_list.append(new_word)
    new_letter_list = []

print("Available Filters: ", new_attribute_name_list)

#Create new fields for each data extraction code
#Currently, keys are generic (e.g., attribute0, attribute1); spaces in the original names prevent it working
# for record in bibliography:
#     if "Codes" in record:
#         for item in record["Codes"]:
#             for number in range(len(attributes_list)):
#                 if "Attributes" in attributes_list[number]:
#                     for attribute in attributes_list[number]["Attributes"]["AttributesList"]:
#                         if item["AttributeId"] == attribute["AttributeId"]:
#                             if "Revisit" not in attribute["AttributeName"]:  #Get rid of codes meant only for us
#                                 if "attribute"+ str(number) in record:
#                                     if not isinstance(record["attribute"+ str(number)], list):
#                                         record["attribute"+ str(number)] = [record["attribute"+ str(number)]]
#                                     record["attribute"+ str(number)].append(attribute["AttributeName"])
#                                 else:
#                                     record["attribute"+ str(number)] = attribute["AttributeName"]
# print(bibliography)

for record in bibliography:
    if "Codes" in record:
        for item in record["Codes"]:
            for number in range(len(attributes_list)):
                if "Attributes" in attributes_list[number]:
                    for attribute in attributes_list[number]["Attributes"]["AttributesList"]:
                        if item["AttributeId"] == attribute["AttributeId"]:
                            if "Revisit" not in attribute["AttributeName"]:  #Get rid of codes meant only for us
                                 if new_attribute_name_list[number] in record:
                                    if not isinstance(record[new_attribute_name_list[number]], list):
                                        record[new_attribute_name_list[number]] = [record[new_attribute_name_list[number]]]
                                    record[new_attribute_name_list[number]].append(attribute["AttributeName"])
                                 else:
                                    record[new_attribute_name_list[number]] = attribute["AttributeName"]
# print(bibliography)




# Database source 0
# What Type of Artifact is Studied:  (if any)? 1
# What Methods does the Study Use: (Select All That Apply) 2
# Findings Related to the Characteristics of Retracted Papers/Notices: 3
# Several databases/disciplines 4
# Findings Relate To: 5
# Findings Related to Impact of Retraction: 6
# Does the Article Focus on a Particular Role of the Publication Process?  (Select 0, 1 or 2) 7
# In Discussion & Conclusions, What Problems of Retraction are Discussed?  8
# In Discussion & Conclusions, What Reforms are Suggested to Minimize Retractions/Their Impact? 9
# What Open Questions or Future Work are Suggested? 10
# NOTES 11
# citation (first) 12
# STATUS CODES 13
# Valuable data is in varying levels

# Print guide to help identify what filters are
# print("\nGUIDE TO FILTER OPTIONS:")
# for name in attribute_name_list:
#     print(name, "attribute"+str(attribute_name_list.index(name)))

# Write out to new json file
with open('publications.json', 'w') as json_file:
  json.dump({"items": bibliography}, json_file)




