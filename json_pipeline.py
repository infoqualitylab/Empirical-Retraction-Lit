import json

infile = open('eppi_export.json', 'r', encoding = 'utf-8')
bibliography = json.load(infile)
infile.close()

# print(bibliography[0]["Authors"])
print(len(bibliography))

#Make a list of all the author fields:
author_list = []

for record in range(0,(len(bibliography))): #range(0,(len(bibliography)-1?
  if bibliography[record]["Authors"] == "":
    author_list.append("No author listed")
  else:
    author_list.append(bibliography[record]["Authors"])
print(author_list)
print(len(author_list))
#Make a new list of author fields, splitting each field where there are semicolons (turns semicolons into commas):
new_author_list = []

# for number in range(0,(len(author_list)-1)):
#   record_index = number
#

for record in author_list:
    new_author_list.append(record.split(";"))
print(new_author_list)
print(len(new_author_list))

clean_author_list = []

for record in new_author_list:
    if record != ' ':
        clean_author_list.append(record)
print("clean", clean_author_list)
print(len(clean_author_list))

# for record in author_list:
#     new_author_list.append(record.split(";")[0].strip())
# print(new_author_list)
# print(len(new_author_list))

#Put the new author list into the author fields in the bibliography:
# for number in range(0,(len(bibliography))):
#   bibliography[number]["Authors"] = new_author_list[number]


#Add "Publication" as type (needed for exhibit to work)
# for number in range(0,len(bibliography)):
#     bibliography[number]["type"] = ["Publication"]

#Write out to new json file
# with open('json_output_10.8.2020.json', 'w') as json_file:
#   json.dump(bibliography, json_file)






# clean_author_list = []
# clean_record_list = []
#
# for record in new_author_list:
#   for author in record:
#     if author != " ":
#       clean_author_list.append(author)
#       clean_record_list.append(clean_author_list)
#     clean_author_list = []
# #.strip() somewhere?
#
# print(len(clean_author_list))
# print(len(clean_record_list))

# clean_author_list = []
#
# for number in range(0,(len(bibliography))):
#   for record in new_author_list:
#     for author in record:
#       if author != " ":
#         clean_author_list.append(author)
#         bibliography[number]["Authors"] = clean_author_list
#       clean_author_list = []
#
#
# print(bibliography[0]["Authors"])




# def clean_missing(key, r):
#     #pass it a key value that you want to check exists, and a dict it might be in it'll return either that key's value, or 'missing'
#     if key in r:
#         result = r[key]
#     else:
#         result = "missing"
#     return result
#
# gendercount = {}
#
# for record in bibliography:
#     author = clean_missing('Authors', record)
#     if author in gendercount:
#         gendercount[author] += 1
#     else:
#         gendercount[author] = 1
#
# print(gendercount)




