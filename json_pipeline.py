import json
#No additional action required; library json comes with Python, and users do not need to install the library themselves

#Input your filepath here:
infile = open('/Users/randiproescholdt/Documents/Sloan - Python/eppi_export_6.18.2021.json', 'r', encoding = 'utf-8')
#If you encounter a unicode error, try the following line instead:
#infile = open(r'/Users/randiproescholdt/Documents/Sloan - Python/eppi_export_6.18.2021.json', 'r', encoding = 'utf-8')

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
    bibliography[number]["type"] = "Publication"


#Add parentheses around Issue numbers
new_issue_list = []
for record in bibliography:
    if len(record["Issue"]) == 0:
        new_issue_list.append("")
        if record['Volume'] != "":
            record['Volume'] = record['Volume'] + "," # Add a comma after the volume number if there is no issue number
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
        bibliography[number]["DOI"] = new_doi_list[number] # This will be for displaying the DOI
        bibliography[number]["Link"] = new_doi_list[number] # This will be for the "Link to article"
    else:
        if bibliography[number]["URL"] != "":
            print("No DOI, but has URL; " + bibliography[number]["Authors"][0] + ", " + bibliography[number]["Title"])
            bibliography[number]["Link"] = bibliography[number]["URL"]
        else:
            print("No DOI, no URL; " + bibliography[number]["Authors"][0] + ", " + bibliography[number]["Title"])
            del bibliography[number]["URL"] # Take out empty URL field so link to nowhere doesn't appear
        del bibliography[number]["DOI"] #Take out empty DOI field

#Change key names to match index.html
for record in bibliography:
    record["label"] = record["Title"]
    del record["Title"]
    record["author"] = record["Authors"]
    del record["Authors"]
    record["id"] = record["ItemId"]
    del record["ItemId"]
    if record["ParentTitle"] != "":     # If no journal is listed, we don't want a journal field; otherwise, an extra comma will show up
        record["venue"] = record["ParentTitle"]
    del record["ParentTitle"]
    record["pub-type"] = record["TypeName"]
    del record["TypeName"]
    record["year"] = record["Year"]
    del record["Year"]

## ACCESSING DATA FROM THE CODE SETS

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


# Write out to new json file
with open('publications.json', 'w') as json_file:
  json.dump({"items": bibliography}, json_file)




