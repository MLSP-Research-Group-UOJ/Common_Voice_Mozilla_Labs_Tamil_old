import os
    # (C) 2023 SPDAnuraj All rights reserved.
    # This code is licensed under the MIT License.
    
def count_wav_files(directory):
    count = 0
    for file in os.listdir(directory):
        if file.endswith(".wav"):
            count += 1
    return count

def main():
    directory = "/mnt/ricproject4/commercial_product/data/cv-corpus/cv-corpus-12.0-2022-12-07/ta/clips/"
    count = count_wav_files(directory)
    print(f"Number of .wav files in the directory: {count}")

if __name__ == "__main__":
    main()
