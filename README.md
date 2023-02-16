# Common_Voice_Mozilla_Labs_Tamil
Common Voice Mozilla Labs Tamil

This repository contains a dataset of Tamil speech recordings for use in training and testing speech recognition models. The data was collected as part of the Common Voice project by Mozilla Labs.
Table of Contents

    Dataset Description
    Data Format
    Python Files
    License

Dataset Description

The Common Voice project aims to build a publicly available dataset of speech recordings in multiple languages, which can be used to train speech recognition models. This repository contains the Tamil dataset.

The dataset contains over 5,000 recordings of Tamil speech, with each recording lasting between 2 and 10 seconds. The recordings were made by volunteers, and cover a wide range of ages and accents.
Data Format

The dataset is provided in the following format:

    Audio files in WAV format
    Transcription files in CSV format

The audio files are stored in the "clips" directory, and the corresponding transcriptions are stored in the "train.tsv" file. The "train.tsv" file contains the following columns:

    path: the path to the audio file
    sentence: the transcription of the spoken sentence
    up_votes: the number of upvotes the recording has received
    down_votes: the number of downvotes the recording has received
    age: the age of the speaker (if provided)
    gender: the gender of the speaker (if provided)
    accent: the accent of the speaker (if provided)

Python Files

This repository also contains the following Python files:

    convert_tsv2txt.py: This script converts the transcriptions from the Common Voice Tamil dataset in TSV (tab-separated values) format to plain text files. 
    The script reads the TSV file, extracts the transcription text from each row, and writes it to a separate text file for each audio recording. 
    The text files are saved in a subdirectory called "text". This script is useful for generating the ground truth transcriptions needed for training a speech recognition model, 
    as the text files can be used to compare the transcriptions generated by the model to the actual transcriptions.
    
    
    copy_wav_files_parallel.py: This script is used to copy the audio files from the Common Voice Tamil dataset to a new directory in parallel.
    The script uses the multiprocessing module in Python to copy the files in parallel, which can be faster than copying them sequentially.
    The script takes two arguments: the path to the directory containing the source audio files, and the path to the directory where the files should be copied. 
    This script can be useful for creating a new copy of the dataset for use in training a speech recognition model, or for processing the dataset in a way that 
    requires all of the audio files to be in a single directory.


License

The Common Voice dataset is released under the Creative Commons CC0 Public Domain Dedication. This means that the data is freely available for any purpose, and can be used, modified, and distributed without any restrictions. For more information about the CC0 license, please see the LICENSE file in this repository.
