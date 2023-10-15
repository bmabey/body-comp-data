
import json
import pandas as pd

def process_json_to_csv(input_json_file, output_csv_file):
    with open(input_json_file) as file:
        data = json.load(file)

    def split_name(name):
        return {
            'metric': name.split('_')[0],
            'sex': name.split('_')[1],
            'percentile': name.split('_')[2]
        }

    all_processed_data = []
    for dataset in data['datasetColl']:
        name_parts = split_name(dataset['name'])
        for row in dataset['data']:
            row['age'] = row['value'][0]
            row[name_parts['metric']] = row['value'][1]
            all_processed_data.append({
                'metric': name_parts['metric'],
                'sex': name_parts['sex'],
                'percentile': name_parts['percentile'],
                'age': row['age'],
                'value': row[name_parts['metric']]
            })

    df = pd.DataFrame(all_processed_data)
    df.to_csv(output_csv_file, index=False)

# Usage example:
process_json_to_csv('wpd.json', 'data.csv')
