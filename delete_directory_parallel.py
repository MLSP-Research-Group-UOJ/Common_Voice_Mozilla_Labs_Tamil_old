import os
import shutil
import multiprocessing
import sys

def delete_directory_parallel(path):
    """
    Deletes the directory at the given path and all its subdirectories
    in parallel using multiprocessing.

    Args:
        path (str): The path to the directory to be deleted.

    Raises:
        OSError: If the directory could not be deleted.
    """
    
    # (C) 2023 SPDAnuraj All rights reserved.
    # This code is licensed under the MIT License.
    
    # Define the function to delete a directory and all its contents
    def delete_directory(path):
        try:
            shutil.rmtree(path)
        except OSError as e:
            print(f"Error deleting {path}: {e}")

    # Create a multiprocessing Pool with the number of processes equal to the number of CPU cores
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())

    # Use the Pool to apply the delete_directory function to the given path and all its subdirectories in parallel
    for root, dirs, files in os.walk(path, topdown=False):
        for dir in dirs:
            pool.apply_async(delete_directory, args=(os.path.join(root, dir),))
    
    # Close the Pool and wait for all processes to finish
    pool.close()
    pool.join()

    # Delete the original directory
    try:
        shutil.rmtree(path)
    except OSError as e:
        print(f"Error deleting {path}: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python delete_directory_parallel.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    delete_directory_parallel(directory_path)