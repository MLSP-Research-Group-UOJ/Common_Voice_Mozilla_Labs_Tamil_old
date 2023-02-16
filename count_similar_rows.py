from collections import Counter
import csv

    # (C) 2023 SPDAnuraj All rights reserved.
    # This code is licensed under the MIT License.
    
def count_similar_rows(file_path):
    rows = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            rows.append(tuple(row))
    row_counts = Counter(rows)
    print("Total count of similar rows:", sum(count for count in row_counts.values() if count > 1))


count_similar_rows('concatenated_trainlist_CV_duplicate.tsv')
#print(*counts, sep = '\n')