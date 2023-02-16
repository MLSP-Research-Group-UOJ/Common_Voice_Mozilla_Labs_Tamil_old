    # (C) 2023 SPDAnuraj All rights reserved.
    # This code is licensed under the MIT License.

def convert_tsv_to_txt(tsv_file, txt_file):
    with open(tsv_file, "r") as tsv, open(txt_file, "w") as txt:
        lines = tsv.readlines()
        for line in lines:
            line = line.strip().replace("\t", " ")
            txt.write(line + "\n")
            
convert_tsv_to_txt("concatenated_trainlist_CV.tsv", "train_CV_Tamil.txt")