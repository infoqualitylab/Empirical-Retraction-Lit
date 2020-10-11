import json

infile = open('eppi_export.json', 'r', encoding = 'utf-8')
bibliography = json.load(infile)
infile.close()

# print(bibliography[0]["Authors"])
print("Length of bibliography: ", len(bibliography))

#Make a list of all the author fields:
author_list = []

for record in range(0,(len(bibliography))):
  if bibliography[record]["Authors"] == "":
    author_list.append("No author listed")
  else:
    author_list.append(bibliography[record]["Authors"])
print(author_list)
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



print(new_author_list)
print("Length of new author list:", len(new_author_list))

#Put the new author list into the author fields in the bibliography:
for number in range(0,(len(bibliography))):
  bibliography[number]["Authors"] = new_author_list[number]


#Add "Publication" as type (needed for exhibit to work)
for number in range(0,len(bibliography)):
    bibliography[number]["type"] = ["Publication"]

#Write out to new json file
with open('json_output_10.11.2020.json', 'w') as json_file:
  json.dump({"items": bibliography}, json_file)




