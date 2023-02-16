import os
import shutil
import multiprocessing
from tqdm import tqdm

def copy_wav_file(src_file, src_dir, dst_dir):
    src_path = os.path.join(src_dir, src_file)
    dst_path = os.path.join(dst_dir, src_file)
    shutil.copy(src_path, dst_path)

def copy_wav_files_parallel(src_dir, dst_dir):
    """
    Copies all .wav files from src_dir to dst_dir in parallel.

    Args:
        src_dir (str): Path to the source directory.
        dst_dir (str): Path to the destination directory.

    Returns:
        None
    """
    # (C) 2023 SPDAnuraj All rights reserved.
    # This code is licensed under the MIT License.
    
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    
    # Get a list of all .wav files in the source directory
    wav_files = [f for f in os.listdir(src_dir) if f.endswith('.wav')]
    
    # Create a process pool with the same number of processes as the number of CPU cores
    with multiprocessing.Pool() as pool:
        # Map the copy_wav_file function to the list of .wav files
        # This distributes the work among the processes in the pool
        # pool.starmap(copy_wav_file, [(f, src_dir, dst_dir) for f in wav_files])
        
        results = []
        for f in wav_files:
            result = pool.apply_async(copy_wav_file, args=(f, src_dir, dst_dir))
            results.append(result)
        
        # Wait for all processes to finish
        for result in tqdm(results, desc='Copying files', total=len(wav_files)):
            result.wait()

copy_wav_files_parallel("/mnt/ricproject4/commercial_product/data/cv-corpus/cv-corpus-12.0-2022-12-07/ta/clips/", "/mnt/ricproject4/commercial_product/data/cv-corpus/cv-corpus-12.0-2022-12-07/ta/clipsWav/")
