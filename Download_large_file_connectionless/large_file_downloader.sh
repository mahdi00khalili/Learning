#!/bin/bash




chunk_size=1000000  # Set the chunk size in bytes (e.g., 1 MB)
file_size=$(curl -sI https://csqjxiao.github.io/PersonalPage/csqjxiao_files/OS2015/linux-command-line-and-shell-scripting-bible-by-richard-blum-christine-bresnahan.pdf | grep -i Content-Length | awk '{print $2}' | tr -d '\r')  # Get the size of the file
echo -e "\n total file size is $file_size"
echo -e "............................... \n"
touch temp.mp3

status=true
start=0

# valid download size until now
downloaded_file_size_util_now=0

while $status; do

    end=$((start+chunk_size-1))
    echo "start is $start and end is $end"

    # using a temp.mp3 file to save each chunk for temporary.
    > temp.mp3
    curl -s -r $start-$end --retry 1000 https://csqjxiao.github.io/PersonalPage/csqjxiao_files/OS2015/linux-command-line-and-shell-scripting-bible-by-richard-blum-christine-bresnahan.pdf >> temp.mp3

    # Specify the path to the file
    # Use the stat command to get the temp.mp3 file size
    file_path="temp.mp3"
    temp_file_size=$(stat -c %s "$file_path")

    # how many bytes are less than one chunk at the end off downloading
    remaid_size_of_file=$((file_size % chunk_size))

    # check that the part of this chank that is downloaded is valid or not.
    if [[ "$temp_file_size" == "$chunk_size" ]] || [[ "$temp_file_size" == "$remaid_size_of_file" ]]; then
        
        # adding the temp_file_size to the downloaded_file_size_util_now in every success loop
        downloaded_file_size_util_now=$((downloaded_file_size_util_now + temp_file_size))
        > temp.mp3

        # the size that are downloaded.
        downladed=$downloaded_file_size_util_now
        echo -e "completed : $downladed bytes...\n"

        # remove temporary temp.mp3 file
        rm -rf temp.mp3
    else
        # is not valid 
        
        # repeat this chunks downloading
        start-=$chunk_size
        echo "poor connection. continue ..."
        continue
    fi

    # update the loops variables
    start=$((start + chunk_size))  # Correct the syntax for incrementing start

    # check if all of the contents are downloaded 
    if [[ "$start" -lt "$file_size" ]]; then 
        status=true
    else
        status=false
        
    fi
    
done






