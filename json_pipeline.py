import json
#No additional action required; library json comes with Python, and users do not need to install the library themselves

infile = open('eppi_export_12.10.2020.json', 'r', encoding = 'utf-8')
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


#Add http://doi.org/ to DOIs
new_doi_list = []

for record in bibliography:
    if len(record["DOI"]) == 0:
        new_doi_list.append("")
    else:
        new_doi_list.append("http://doi.org/" + record["DOI"])

print("Length of new DOI list:",len(new_doi_list))

for number in range(0,(len(bibliography))):
  bibliography[number]["DOI"] = new_doi_list[number]


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
# attributes_dict = {}
# filters_list = [] # can this be used as an if statement in a loop? e.g., for x in filters_list / if x = artifact
# #
# attributes_dict = codesets[0]["Attributes"]
# attributes_list = attributes_dict["AttributesList"]
# # print(attributes_list)
# print(attributes_list[0]["Attributes"]["AttributesList"]) #List of database source info
# dbsource_dict = {}
#
# for item in attributes_list[0]["Attributes"]["AttributesList"]:
#     item["AttributeName"]
# for item in attributes_list:
#     filters_list.append(item["AttributeName"])


#Google nested dictionaries?
#TRY STARTING FROM THE REFERENCES AND PULL IN ATTRIBUTE NAME AND IDS?

# attribute_id_list = []
# for item in attributes_list:
#     for attribute in item["Attributes"]:
#         if "AttributesList" in attribute:
#             specific_attributes_dict = attribute["AttributesList"]
# print(specific_attributes_dict)

#         attribute_id_list.append(attribute)
# print(attribute_id_list)
# attribute_ids_dict = attributes_dict["AttributesList"]
# for item in attributes_list:
#     if "Attributes" in item:
#         attributeid_dict = item["AttributesList"]
# print(attributeid_dict)



# attributes_dict = (codesets["AttributesList"])
#
#         # if "AttributesList" in item:
#         #     for item in attributes["AttributesList"]:
#         #         print(item)
#
# print(attributes_dict)
#         for thing in item:
#             filters_list.append(item)
# print(filters_list)





#Pull out artifact data extraction codes
# for record in bibliography:
#     if "Codes" in record:
#         for item in record["Codes"]:
#             if item["AttributeId"] == 6209644:
#                 record["Artifact"] = "Altmetrics to Retracted Papers"
#             if item["AttributeId"] == 5655688:
#                 record["Artifact"] = "Citations to Retracted Papers"
#             if item["AttributeId"] == 5655686:
#                 record["Artifact"] = "Instructions to Authors"
#             if item["AttributeId"] == 5655684:
#                 record["Artifact"] = "Retraction Notices"
#             if item["AttributeId"] == 5655685:
#                 record["Artifact"] = "Retracted Papers"
#             if item["AttributeId"] == 5655687:
#                 record["Artifact"] = "Retraction Policies"



#Pull out method data extraction codes
# for record in bibliography:
#     if "Codes" in record:
#         for item in record["Codes"]:
#             if item["AttributeId"] == 5681698:
#                 record["Method"] = "Bibliometrics - Excluding Systematic Reviews"
#             if item["AttributeId"] == 5681700:
#                 record["Method"] = "Citation Content Analysis"
#             if item["AttributeId"] == 5681699:
#                 record["Method"] = "Content/Thematic Analysis"
#             if item["AttributeId"] == 6280798:
#                 record["Method"] = "Econometrics"
#             if item["AttributeId"] == 6306062:
#                 record["Method"] = "Financial Estimation"
#             if item["AttributeId"] == 5717740:
#                 record["Method"] = "Formal, Systematic Review of the Literature"
#             if item["AttributeId"] == 5681702:
#                 record["Method"] = "Handsearching"
#             if item["AttributeId"] == 5681701:
#                 record["Method"] = "Interviews"
#             if item["AttributeId"] == 6145390:
#                 record["Method"] = "Psychology Experiment"
#             if item["AttributeId"] == 5681697:
#                 record["Method"] = "Survey"

#Pull out geographic data extraction codes
# for record in bibliography:
#     if "Codes" in record:
#         for item in record["Codes"]:
#             if item["AttributeId"] == 6266247:
#                 record["Location"] = "Australia"
#             if item["AttributeId"] == 5821359:
#                 record["Location"] = "China"
#             if item["AttributeId"] == 6266248:
#                 record["Location"] = "Germany"
#             if item["AttributeId"] == 6282357:
#                 record["Location"] = "India"
#             if item["AttributeId"] == 6323834:
#                 record["Location"] = "Iran"
#             if item["AttributeId"] == 6282358:
#                 record["Location"] = "Italy"
#             if item["AttributeId"] == 6266249:
#                 record["Location"] = "Japan"
#             if item["AttributeId"] == 5987040:
#                 record["Location"] = "Korea"
#             if item["AttributeId"] == 5822496:
#                 record["Location"] = "Brazil"
#             if item["AttributeId"] == 5822497:
#                 record["Location"] = "Argentina"
#             if item["AttributeId"] == 5822508:
#                 record["Location"] = "Mexico"
#             if item["AttributeId"] == 5751669:
#                 record["Location"] = "Malaysia"
#             if item["AttributeId"] == 6323835:
#                 record["Location"] = "Pakistan"
#             if item["AttributeId"] == 5829141:
#                 record["Location"] = "United States"

#Pull out database source extraction codes

attributes_dict = codesets[0]["Attributes"]
attributes_list = attributes_dict["AttributesList"]
# print(attributes_list)
# print(attributes_list[0]["Attributes"]["AttributesList"]) #List of database source info

# for item in attributes_list[0]["Attributes"]["AttributesList"]:
#     print(item["AttributeName"])
#     print(item["AttributeId"])

attribute_name_list = []
for number in range(0,len(attributes_list)):
    attribute_name_list.append(attributes_list[number]["AttributeName"])
#
# new_attribute_list = []
# for record in attribute_name_list:
#     if len(record.split(' ')) > 0:
#         attribute_names = []
#         for each_attribute in record.split(' '):  #each_au is individual characters
#             each_attribute = each_attribute.strip()
#             if len(each_attribute) > 0:
#                 attribute_names.append(each_attribute) #au_names is individual authors
#
#         record = ', '.join(each_attribute)
#     new_attribute_list.append(record)
# print(new_attribute_list)
print("GUIDE TO FILTER OPTIONS:")
for name in attribute_name_list:
    print(name, "attribute", attribute_name_list.index(name))
#
#BEST SO FAR; NEED TO REMOVE SPACES FROM ATTRIBUTES IN ATTRIBUTE_NAME_LIST
#OR MAYBE MAKE UP NEW GENERIC NAMES? CAN PRINT OUT INDEX OF ATTRIBUTE_NAME_LIST AS GUIDE?
for record in bibliography:
    if "Codes" in record:
        for item in record["Codes"]:
            for number in range(len(attributes_list)):  #IS THIS LINE THE PROBLEM? FIND ANOTHER WAY?
                if "Attributes" in attributes_list[number]:
                    for attribute in attributes_list[number]["Attributes"]["AttributesList"]:
                        if item["AttributeId"] == attribute["AttributeId"]:
                            # if attribute_name_list[number] in record:
                            #     if not isinstance(record[attribute_name_list[number]], list):
                            #         record[attribute_name_list[number]] = [record[attribute_name_list[number]]]
                            #     record[attribute_name_list[number]].append(attribute["AttributeName"])
                            # else:
                            #     record[attribute_name_list[number]] = attribute["AttributeName"]
                            #
                            # print(attributes_list[number]["AttributeName"])
                            if "attribute"+ str(number) in record:
                                if not isinstance(record["attribute"+ str(number)], list):
                                    record["attribute"+ str(number)] = [record["attribute"+ str(number)]]
                                record["attribute"+ str(number)].append(attribute["AttributeName"])
                            else:
                                record["attribute"+ str(number)] = attribute["AttributeName"]
print(bibliography)

# #12, 10,9,8,4 index positions not working; Problem because of nested data extraction codes?
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
# print(bibliography)

# for record in bibliography:
#     if "Codes" in record:
#         for item in record["Codes"]:
#             for attribute in attributes_list[0]["Attributes"]["AttributesList"]:
#                 if item["AttributeId"] == attribute["AttributeId"]:
#                     if "data_source" in record:
#                         if not isinstance(record["data_source"], list):
#                             record["data_source"] = [record["data_source"]]
#                         record["data_source"].append(attribute["AttributeName"])
#                     else:
#                         record["data_source"] = attribute["AttributeName"]
#             for attribute in attributes_list[1]["Attributes"]["AttributesList"]:
#                 if attribute["AttributeName"] != "Revisit":
#                     if item["AttributeId"] == attribute["AttributeId"]:
#                         if "Artifact" in record:
#                             if not isinstance(record["Artifact"], list):
#                                 record["Artifact"] = [record["Artifact"]]
#                             record["Artifact"].append(attribute["AttributeName"])
#                         else:
#                             record["Artifact"] = attribute["AttributeName"]
#             for attribute in attributes_list[2]["Attributes"]["AttributesList"]:
#                 if attribute["AttributeName"] != "Revisit (What methods does the study use?)":
#                     if item["AttributeId"] == attribute["AttributeId"]:
#                         if "Method" in record:
#                             if not isinstance(record["Method"], list):
#                                 record["Method"] = [record["Method"]]
#                             record["Method"].append(attribute["AttributeName"])
#                         else:
#                             record["Method"] = attribute["AttributeName"]
#
# print(bibliography)
# print(attributes_list)
# print(attributes_list[0]["AttributeName"])
# attribute_name_list = []
# for number in range(0,len(attributes_list)):
#     attribute_name_list.append(attributes_list[number]["AttributeName"])

# print(attribute_name_list)

# for number in range(0,len(bibliography)):
#     bibliography[number]["type"] = ["Publication"]


            # for number in range(1, (len(attributes_list)-1)):
            #     for attribute in attributes_list[number]:
            #         print(attribute)
                    # if item["AttributeId"] == attribute["AttributeId"]:
                    #     record["new_attribute"] = attribute["AttributeName"]

#     print(item["AttributeName"])
#     print(item["AttributeId"])


# for record in bibliography:
#     if "Codes" in record:
#         for item in record["Codes"]:
#             if item["AttributeId"] == 6323832:
#                 record["data_source"] = "AAMC Directory of American Medical Education"
#             if item["AttributeId"] == 6326398:
#                 record["data_source"] = "Azoulay et al. 'Reasons for Retraction'"
#             if item["AttributeId"] == 6323837:
#                 record["data_source"] = "Access World News"
#             if item["AttributeId"] == 6344235:
#                 record["data_source"] = "BioMed Central"
#             if item["AttributeId"] == 5888829:
#                 record["data_source"] = "CINAHL"
#             if item["AttributeId"] == 5822501:
#                 record["data_source"] = "Cochrane Central Register of Controlled"
#             if item["AttributeId"] == 5995689:
#                 record["data_source"] = "Directory of Open Access Journals"
#             if item["AttributeId"] == 5822502:
#                 record["data_source"] = "Embase"
#             if item["AttributeId"] == 6305103:
#                 record["data_source"] = "EurekAlert"
#             if item["AttributeId"] == 6280797:
#                 record["data_source"] = "Faculty Roster of the Association of American Medical"
#             if item["AttributeId"] == 6326399:
#                 record["data_source"] = "Fang et al. 'Misconduct accounts for the majority of retracted scientific publications'"
#             if item["AttributeId"] == 6323838:
#                 record["data_source"] = "The Federal Register"
#             if item["AttributeId"] == 6326400:
#                 record["data_source"] = "Grieneisen and Zhang, 'A comprehensive survey of retracted articles from the scholarly literature'"
#             if item["AttributeId"] == 5888827:
#                 record["data_source"] = "Google Scholar"
#             if item["AttributeId"] == 5971042:
#                 record["data_source"] = "Index Medicus"
#             if item["AttributeId"] == 6313422:
#                 record["data_source"] = "Journal Citation Reports"
#             if item["AttributeId"] == 5987034:
#                 record["data_source"] = "KoreaMed"
#             if item["AttributeId"] == 6305102:
#                 record["data_source"] = "LexisNexis"
#             if item["AttributeId"] == 5822512:
#                 record["data_source"] = "LILACS"
#             if item["AttributeId"] == 5822503:
#                 record["data_source"] = "MEDLINE"
#             if item["AttributeId"] == 6209641:
#                 record["data_source"] = "Mendeley"
#             if item["AttributeId"] == 5995690:
#                 record["data_source"] = "NCBI bibliographic databases"
#             if item["AttributeId"] == 5971032:
#                 record["data_source"] = "NIH Guide for Grants and Contracts"
#             if item["AttributeId"] == 5971034:
#                 record["data_source"] = "ORI Annual Reports"
#             if item["AttributeId"] == 5822504:
#                 record["data_source"] = "PubMed"
#             if item["AttributeId"] == 5822505:
#                 record["data_source"] = "Retraction Watch"
#             if item["AttributeId"] == 5995691:
#                 record["data_source"] = "SCI"
#             if item["AttributeId"] == 5822511:
#                 record["data_source"] = "SciELO"
#             if item["AttributeId"] == 5844708:
#                 record["data_source"] = "ScienceDirect"
#             if item["AttributeId"] == 5925178:
#                 record["data_source"] = "SCImago"
#             if item["AttributeId"] == 5888828:
#                 record["data_source"] = "Scopus"
#             if item["AttributeId"] == 5822506:
#                 record["data_source"] = "Web of Science"

# for record in bibliography:
#     if "Codes" in record:
#         for item in record["Codes"]:
            # for thing in codesets:
            #     for attributes in thing:
            #         if "AttributeId" in attributes:
            #             print(attributes["AttributeId"])
                    # for attributes in thing:
                    #     if attributes["AttributeId"] == item["AttributeId"]:
                    #     # item["AttributeId"] = attributes["AttributeName"]
                    #         record["Location"] = attributes["AttributeName"]

# print(bibliography)

#Guide to help identify what filters are
print("GUIDE TO FILTER OPTIONS:")
for name in attribute_name_list:
    print(name, "attribute", attribute_name_list.index(name))

# Write out to new json file
with open('publications_12.20.2020.json', 'w') as json_file:
  json.dump({"items": bibliography}, json_file)




