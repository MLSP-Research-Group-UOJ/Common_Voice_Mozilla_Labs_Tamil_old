# (C) 2023 SPDAnuraj All rights reserved.
# This code is licensed under the MIT License.

def update_tsv(tsv1_file, tsv2_file, tsv1_col=0, tsv2_col=1):
    """
    Update a TSV file by replacing values in one column with values from another TSV file.
    This method used to create a map between CV_corpus speaker id and newly formated speakerid which start from id3#####.
    
    Args:
        tsv1_file (str): Path to the first TSV file to be updated.
        tsv2_file (str): Path to the second TSV file used to update the first file.
        tsv1_col (int): The column number (zero-based) in the first TSV file to use for matching values in the second file. Default is 0.
        tsv2_col (int): The column number (zero-based) in the second TSV file to use for updating values in the first file. Default is 1.
        
    Returns:
        None
        
    Raises:
        IOError: If either file could not be opened or read.
    """
    
    # Create dictionaries for the data in each TSV file, where the keys are the values in the specified column
    tsv1_data = {}
    tsv2_data = {}
    
    # Open both TSV files
    with open(tsv1_file, "r") as tsv1, open(tsv2_file, "r") as tsv2:
        
        # Read all the lines in each file
        tsv1_lines = tsv1.readlines()
        tsv2_lines = tsv2.readlines()
        
        # Store the data from the first TSV file in a dictionary
        for line in tsv1_lines:
            cols = line.strip().split("\t")
            tsv1_data[cols[tsv1_col]] = line
        
        # Store the data from the second TSV file in a dictionary
        for line in tsv2_lines:
            cols = line.strip().split("\t")
            tsv2_data[cols[tsv2_col]] = cols[0]
    
    # Create a new list of lines for the updated TSV file, starting with the header line from the first TSV file
    updated_tsv = [tsv1_lines[0]]
    
    # Update each line in the first TSV file
    for line in tsv1_lines[1:]:
        
        # Split the line into columns
        cols = line.strip().split("\t")
        
        # If the value in the specified column is in the second TSV file, update the line
        if cols[tsv1_col] in tsv2_data:
            updated_line = tsv2_data[cols[tsv1_col]] + "\t".join(cols[1:])
            updated_tsv.append(updated_line)
        
        # If the value is not in the second TSV file, keep the original line
        else:
            updated_tsv.append(line)
    
    # Write the updated TSV file
    with open(tsv1_file, "w") as tsv1:
        tsv1.write("\n".join(updated_tsv))


            
update_tsv('speaker_id_mapping.tsv','modified_test.tsv')