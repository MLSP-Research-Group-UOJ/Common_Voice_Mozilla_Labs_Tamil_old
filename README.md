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

    preprocess.py: A script to preprocess the audio files and transcriptions and output them in a format suitable for training a speech recognition model. The script reads the "train.tsv" file and uses the Python librosa library to convert the audio files to Mel-frequency cepstral coefficients (MFCCs). The output of the script is a set of NumPy arrays containing the MFCCs and corresponding transcriptions, which can be used for training a model.
    train.py: A script to train a speech recognition model using the preprocessed data. The script uses the keras library to define and train a deep neural network model. The architecture of the model is defined in the script, and can be easily modified to experiment with different model architectures.
    predict.py: A script to use a trained model to transcribe new speech recordings. The script loads a saved model from disk and uses it to transcribe new audio files. The output of the script is a text file containing the transcriptions of the audio files.

License

The Common Voice dataset is released under the Creative Commons CC0 Public Domain Dedication. This means that the data is freely available for any purpose, and can be used, modified, and distributed without any restrictions. For more information about the CC0 license, please see the LICENSE file in this repository.
