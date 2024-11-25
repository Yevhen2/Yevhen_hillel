"""
Візміть два файли з теки ideas_for_test/work_with_csv.

порівняйте на наявність дублікатів і приберіть їх.

Результат запишіть у файл result_<your_second_name>.csv
"""

import csv

import requests
from io import StringIO


def download_csv(url):
    """Download CSV from URL."""
    response = requests.get(url)
    response.raise_for_status()
    return list(csv.reader(StringIO(response.text)))


"""URL to files on GitHub."""
file1_url = ('https://raw.githubusercontent.com/dntpanix/'
             'automation_qa/main/ideas_for_test/work_with_csv/r-m-c.csv')
file2_url = ('https://raw.githubusercontent.com/dntpanix/automation_qa/'
             'main/ideas_for_test/work_with_csv/rmc.csv')

"""Download."""
file1_data = download_csv(file1_url)
file2_data = download_csv(file2_url)

"""Merge data from two files."""
merged_data = file1_data + file2_data

"""Duplicate removal"""
unique_data = []
seen = set()

for row in merged_data:
    row_tuple = tuple(row)
    if row_tuple not in seen:
        seen.add(row_tuple)
        unique_data.append(row)

"""Write the result in a new file."""
result_file_path = 'result_nakhaba.csv'
with open(result_file_path, mode='w', newline='',
          encoding='utf-8') as result_file:
    writer = csv.writer(result_file)
    writer.writerows(unique_data)

print(f'Результат записано в файл: {result_file_path}')
