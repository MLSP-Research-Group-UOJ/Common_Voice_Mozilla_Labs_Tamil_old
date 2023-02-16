import os
import threading

"""
(c) 2023 SPDAnuraj, Inc. All rights reserved.
This code is licensed under the Apache License, Version 2.0.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
"""
def delete_wav_files(directory):
    """
    Deletes all files with the .wav extension in a given directory.

    Args:
    directory (str): The directory to delete .wav files from.
    """
    deleted = 0
    for file in os.listdir(directory):
        if file.endswith(".wav"):
            os.remove(os.path.join(directory, file))
            deleted += 1
    print(f"Thread finished deleting {deleted} files")

def main():
    """
    Creates multiple threads to delete .wav files from a directory in parallel.
    """
    directory = "/mnt/ricproject4/commercial_product/data/cv-corpus/cv-corpus-12.0-2022-12-07/ta/converted_train_set/"
    threads = []
    for i in range(40):
        t = threading.Thread(target=delete_wav_files, args=(directory,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
