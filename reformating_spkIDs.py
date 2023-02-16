import csv,os
import sys
import pandas as pd
import shutil
import subprocess
import concurrent.futures
import time
from tqdm import tqdm
from shutil import copyfile
from pydub import AudioSegment

csv.field_size_limit(sys.maxsize)

def remove_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        # remove the first row
        next(reader)
        # create a list of rows
        rows = [row[:2] for row in reader]
    # Open the output file
    with open('modified_' + file_path, 'w') as file:
        # Write the modified data to the output file
        writer = csv.writer(file, delimiter='\t')
        writer.writerows(rows)

def sort_file(file_path):
    # Open the input file
    with open(file_path, 'r') as file:
        # Read the file as a CSV with tab delimiter
        reader = csv.reader(file, delimiter='\t')
        # Extract the first column of each row
        lines = [row[0] for row in reader]
        #print(*lines, sep = '\n')
        print(len(lines), "\n")
        # Sort the first words
        sorted_words = sorted(lines)
        #remove duplicates
        unique_words = list(set(sorted_words))
        print(len(unique_words))
    # Open the output file
    with open('sorted_' + file_path, 'w') as file:
        # Write the unique words to the output file with number starting from 30000
        for i, word in enumerate(unique_words, 30001):
            file.write(str(i) + ' '+ word + '\n')


def assign_values(file_path):
    # Store the unique words and their corresponding values
    words = {}
    # Open the input file
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        rows = [row for row in reader]
    # Assign a unique value to each unique word in the first column
    for i, row in enumerate(rows):
        word = row[0]
        if word not in words:
            words[word] = len(words) + 30001
        rows[i][0] = words[word]
    # Open the output file
    with open(file_path, 'w') as file:
        # Write the modified data to the output file
        writer = csv.writer(file, delimiter='\t')
        writer.writerows(rows)


#def create_directories(file_path):
#    with open(file_path, 'r') as file:
#        reader = csv.reader(file, delimiter='\t')
#        for row in reader:
#            # Create a directory with the word in the first column
#            os.makedirs(row[0], exist_ok=True)
#            # Create a text file with the name in the second column
#            with open(row[0]+"/"+row[1]+".txt", 'w') as f:
#                pass

#Convert the mp3 files to wav files
#def convert_directory(directory_path):
#    for filename in tqdm(os.listdir(directory_path)):
#        if filename.endswith(".mp3"):
#            # Open the mp3 file
#            audio = AudioSegment.from_mp3(directory_path+"/"+filename)
#            # Save the file as wave
#            audio.export(directory_path+"/"+os.path.splitext(filename)[0]+".wav", format="wav")
#            
#            #number_of_files = sum(f.endswith('.wav') for f in os.listdir(directory_path))
#            #print(number_of_files)

#//def convert_directory(directory_path):
#//    files = os.listdir(directory_path)
#//    count = 0
#//    for filename in tqdm(files, desc="Converting files to .wav", total=len(files)):
#//        if filename.endswith(".mp3"):
#//            # Open the mp3 file
#//            audio = AudioSegment.from_mp3(directory_path+"/"+filename)
#//            # Save the file as wave
#//            audio.export(directory_path+"/"+os.path.splitext(filename)[0]+".wav", format="wav")
#//            count += 1
#//    print(f"{count} .wav files were converted")

##Multi Threading code to convert

def convert_file(directory_path, filename):
    if filename.endswith(".mp3"):
        wav_filename = os.path.splitext(filename)[0]+".wav"
        wav_filepath = os.path.join(directory_path, wav_filename)
        if not os.path.exists(wav_filepath):
            # Open the mp3 file
            audio = AudioSegment.from_mp3(os.path.join(directory_path, filename))
            # Save the file as wave
            audio.export(wav_filepath, format="wav")

def convert_directory(directory_path):
    start_time = time.time()
    files = os.listdir(directory_path)
    count = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=24) as executor:
        future_to_file = {executor.submit(convert_file, directory_path, filename): filename for filename in files}
        for future in tqdm(concurrent.futures.as_completed(future_to_file), desc="Converting files to .wav", total=len(files)):
            filename = future_to_file[future]
            if filename.endswith(".mp3"):
                count += 1
    end_time = time.time()
    print(f"{count} .wav files were converted")
    print(f"Time taken: {round((end_time - start_time) / 60, 2)} minutes")


def change_extension(file_path, old_extension, new_extension):
    # read the tsv file
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        rows = [row for row in reader]

    # change the extension of the second column from old_extension to new_extension
    for row in rows:
        row[1] = row[1].replace(old_extension, new_extension)

    # write the changes back to the file
    with open(file_path, 'w') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerows(rows)


'''
This code reads each input file, stores the first and second columns of each row in a list of lists, and then writes the list to the output file.
''' 
####################################################################################
def join_tsv_files(filenames, output_filename):
    rows = []
    for filename in filenames:
        with open(filename, 'r') as tsv_file:
            reader = csv.reader(tsv_file, delimiter='\t')
            for row in reader:
                rows.append([row[0], row[1]])
    with open(output_filename, 'w') as output_file:
        writer = csv.writer(output_file, delimiter='\t')
        writer.writerows(rows)
    
file_list = ['modified_train.tsv', 'modified_validated.tsv', 'modified_dev.tsv','modified_other.tsv']
output_file = 'concatenated_trainlist_CV.tsv'
#join_tsv_files(file_list, output_file)
####################################################################################


#Add 'id' to the speaker identification number
def add_id(file_path):
    # Open the input file
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        rows = [row for row in reader]
    # Add "id" to each row in the first column
    for i, row in enumerate(rows):
        rows[i][0] = "id" + str(row[0])
    # Open the output file
    with open(file_path, 'w') as file:
        # Write the modified data to the output file
        writer = csv.writer(file, delimiter='\t')
        writer.writerows(rows)


def add_paths_list(file_path):
    # Open the input file
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        rows = [row for row in reader]
    # Add the desired text to the second column of each row
    for i, row in enumerate(rows):
        rows[i][1] = row[0] + '/audio/' + row[1]
    # Open the output file
    with open(file_path, 'w') as file:
        # Write the modified data to the output file
        writer = csv.writer(file, delimiter='\t')
        writer.writerows(rows)
        
        
        
def create_dirs(file_path, root_dir):
    # Open the input file
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        rows = [row for row in reader]
    # Create a folder for each unique word in the first column
    words = set([row[0] for row in rows])
    for word in words:
        os.makedirs(os.path.join(root_dir, word), exist_ok=True)
        os.makedirs(os.path.join(root_dir, word, 'audio'), exist_ok=True)


#***********************************************************************************************#

def process_tsv_old(tsv_file, source_dir, dest_dir):
    with open(tsv_file, "r") as f:
        lines = f.readlines()
        headers = lines[0].strip().split("\t")
        for line in tqdm(lines[1:], desc="Processing files"):
            cols = line.strip().split("\t")
            folder_name = cols[0]
            print(folder_name, '\n')
            wav_path = cols[1]
            print(wav_path, '\n')
            wav_name = os.path.basename(wav_path)
            print(wav_name, '\n')
            folder_path = os.path.join(dest_dir, folder_name)
            audio_path = os.path.join(folder_path, "audio")
            clip_path = os.path.join(source_dir, "clips", wav_name)
            
            if not os.path.exists(folder_path):
                os.makedirs(audio_path)            
            else:
                if os.path.exists(clip_path):
                    print(clip_path, '\n')
                    print(audio_path,'\n')
                    audio_path = os.path.join(audio_path, wav_name)
                    print("Line 189")
                    print(audio_path,'\n')
                    shutil.copy2(clip_path, audio_path)
                    #copyfile(clip_path, audio_path)
#                    cmd='cp "%s" "%s"' % (clip_path, audio_path)
#                    subprocess.call(cmd, shell=True)
                    
                else:
                
                    print("Clip path is not exists")
                    print(clip_path)

"""

In this code, we first extract the relevant data from each line of the tsv file and store it in a list called line_data. 
Then, we create a ThreadPoolExecutor with a specified number of workers (4 in this case), and use the submit method to submit tasks to the executor. 
Each task is to call the process_tsv_line function with the relevant data for a single line. 
The as_completed method is used to iterate over the futures as they complete, 
and the tqdm library is used to display a progress bar with the status of the file copying process.

"""
def process_tsv_line(source_dir, dest_dir, folder_name, wav_path):
    wav_name = os.path.basename(wav_path)
    folder_path = os.path.join(dest_dir, folder_name)
    audio_path = os.path.join(folder_path, "audio")
    clip_path = os.path.join(source_dir, "converted_train_set", wav_name)
    
    if not os.path.exists(folder_path):
        os.makedirs(audio_path)            
    else:
        if os.path.exists(clip_path):
            audio_path = os.path.join(audio_path, wav_name)
            shutil.copy2(clip_path, audio_path)
        else:
            print("Clip path does not exist:", clip_path)

def process_tsv(tsv_file, source_dir, dest_dir):
    with open(tsv_file, "r") as f:
        lines = f.readlines()
        headers = lines[0].strip().split("\t")
        line_data = [
            (source_dir, dest_dir, line.strip().split("\t")[0], line.strip().split("\t")[1])
            for line in lines[1:]
        ]
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
            futures = [executor.submit(process_tsv_line, *data) for data in line_data]
            for f in tqdm(concurrent.futures.as_completed(futures), total=len(line_data), desc="Copying files"):
                pass

tsv_file = 'concatenated_trainlist_CV.tsv'
source_dir = "/mnt/ricproject4/commercial_product/data/cv-corpus/cv-corpus-12.0-2022-12-07/ta/"
dest_dir = "/mnt/ricproject4/commercial_product/data/cv-corpus/cv-corpus-12.0-2022-12-07/ta/seperated_converted_train_set_II"
process_tsv(tsv_file, source_dir, dest_dir)

#***********************************************************************************************#
        

#create_dirs(output_file,"/mnt/ricproject4/commercial_product/data/cv-corpus/cv-corpus-12.0-2022-12-07/ta/test/")    
# Test the function with an example file
#remove_data('train.tsv')
#remove_data('validated.tsv')
#remove_data('dev.tsv')
#remove_data('other.tsv')

#creating test list according to our way
#remove_data("test.tsv")
#assign_values("modified_test.tsv")
#change_extension('modified_test.tsv', '.mp3', '.wav')
#add_id('modified_test.tsv')
#add_paths_list('modified_test.tsv')
#process_tsv('modified_test.tsv', source_dir, dest_dir)
#process_tsv_old('modified_test.tsv', source_dir, dest_dir)

#sort_file(output_file)
#remove_data('reported.tsv')
#sort_file('modified_reported.tsv')
#c
#create_directories('modified_train_2.tsv')
#convert_directory("/mnt/ricproject4/commercial_product/data/cv-corpus/cv-corpus-12.0-2022-12-07/ta/clips")
#change_extension(output_file, '.mp3', '.wav')


#test 2023-02-03
#sort_file('modified_dev.tsv')
#assign_values('modified_dev.tsv')
#change_extension('modified_dev.tsv', '.mp3', '.wav')
#add_id('modified_dev.tsv')
#add_paths_list('modified_dev.tsv')
#process_tsv('modified_dev.tsv', source_dir, dest_dir)

#add_id(output_file)
#add_p--ths_list(output_file)