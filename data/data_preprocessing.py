import json
import re

# Load the JSON files
with open('data/mutation_labels.json', 'r') as labels_file:
    labels_data = json.load(labels_file)

with open('data/mutation_values.json', 'r') as values_file:
    values_data = json.load(values_file)


pattern = r'p\.([A-Za-z]+)(\d+)([A-Za-z]+)'
def convert_to_values_form(string):
    match = re.match(pattern, string)
    if match:
        amino_acid = match.group(1)
        position = match.group(2)
        substitution = match.group(3)
        return f"{position}-{substitution}"
    else:
        return None

if False:
    values_strs = [values_data[i][''] for i in range(len(values_data))]
    data_incorrectly_labeled = False
    for m in labels_data:
        labels_str = m['Mutation ']
        values_str = convert_to_values_form(labels_str)
        if values_str not in values_strs:
            data_incorrectly_labeled = True
    print("Every label in mutation_labels.json corresponds to a label in mutation_values.json:", not data_incorrectly_labeled)

values_strs = []
# Create a dictionary to store the data matching the labels to the data
matched_data, matched_data_1 = {}, {}
labeled_data, labeled_data_1 = [], []
for m_l in labels_data:
    labels_str = m_l['Mutation ']
    values_str = convert_to_values_form(labels_str)
    values_strs.append(values_str)
    m_v = next((m for m in values_data if m[''] == values_str), None)

    # TODO: is 'p.Ser35Leu' meant to have a manual score of 0?
    if 'Score by rubric (manual)' not in m_l.keys():
        if m_l['Mutation '] == 'p.Ser35Leu':
            m_l['Score by rubric (manual)'] = 0
        else:
            print("ERROR: Not all inputs have a given manual score")

    matched_data[labels_str] = {"Manual Score": m_l['Score by rubric (manual)'], 
                                "hbonds before": m_v['hbonds before'], "hbonds after": m_v['hbonds after'],
                                "contacts before": m_v['contacts before'], "contacts after": m_v['contacts after'],
                                "clashes before": m_v['clashes before'], "clashes after": m_v['clashes after'],
                                "interresidual before": m_v['interresidual before'], "interresidual after": m_v['interresidual after'],
                                "interhelical before": m_v['interhelical before'], "interhelical after": m_v['interhelical after'],
                                "rationalized score": m_v['rationalized score']}
    labeled_data.append(matched_data[labels_str])

    matched_data_1[labels_str] = {"Manual Score": m_l['Score by rubric (manual)'], "delta hbonds": m_v['delta hbonds'],
                                  "delta contacts": m_v['delta contacts'], "delta clashes": m_v['delta clashes'],
                                  "delta interresidual": m_v['delta interresidual'], "delta interhelical": m_v['delta interhelical'],
                                  "rationalized score": m_v['rationalized score']}
    labeled_data_1.append(matched_data_1[labels_str])

# Save the list of dictionaries to a JSON file using json.dump()
with open("data/labeled_data.json", "w") as json_file:
    json.dump(labeled_data, json_file)

with open("data/labeled_data_1.json", "w") as json_file:
    json.dump(labeled_data_1, json_file)

test_data = []
for m_v in values_data:
    if m_v[''] in values_strs:
        continue
    test_data.append({"Mutation": m_v[''], "hbonds before": m_v['hbonds before'], "hbonds after": m_v['hbonds after'],
                      "contacts before": m_v['contacts before'], "contacts after": m_v['contacts after'],
                      "clashes before": m_v['clashes before'], "clashes after": m_v['clashes after'],
                      "interresidual before": m_v['interresidual before'], "interresidual after": m_v['interresidual after'],
                      "interhelical before": m_v['interhelical before'], "interhelical after": m_v['interhelical after'],
                      "rationalized score": m_v['rationalized score']})
    
with open("data/test_data.json", "w") as json_file:
    json.dump(test_data, json_file)