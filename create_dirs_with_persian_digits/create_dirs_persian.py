from persian import enToPersianNumb
import os
import time

# Record the start time
start_time = time.time()


def create_directory(path):
    start_num = 1
    finish_num = 1000000

    for num in range(start_num, finish_num):
        dirName = enToPersianNumb(pow(num, 2))
        os.makedirs(path + f"{dirName}", exist_ok=True)
        print(f"Directory '{dirName}' created successfully.")


# Example usage:
directory_path = "/tmp/createfolder/"
create_directory(directory_path)

# Record the end time
end_time = time.time()

# Calculate the running time
running_time = end_time - start_time

print("\n\nRunning time:", running_time, "seconds")
