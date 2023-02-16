import csv
"""
(c) 2023 SPDAnuraj, Inc. All rights reserved.
This code is licensed under the Apache License, Version 2.0.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
"""

def sort_tsv_file(file_path):

    """
    sort all based on first row values in the given tsv file.

    Args:
    directory (str): The path to .tsv file.
    """
    # Open the input file
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        rows = [row for row in reader]
    # Sort the rows based on the first column
    rows.sort(key=lambda x: x[0])
    # Open the output file
    with open(file_path, 'w') as file:
        # Write the sorted data to the output file
        writer = csv.writer(file, delimiter='\t')
        writer.writerows(rows)

sort_tsv_file('concatenated_trainlist_CV_duplicate.tsv')