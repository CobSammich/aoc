#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <number> <programming_file_type>"
    exit 1
fi

# Extract the arguments
number="$1"
file_type="$2"

# Check if the number is a valid integer
if ! [[ "$number" =~ ^[0-9]+$ ]]; then
    echo "Error: The first argument must be a valid number."
    exit 1
fi

declare -A programming_names_dict
programming_names_dict["c"]="./templates/c.c"
programming_names_dict["cpp"]="./templates/cpp.cpp"
programming_names_dict["python"]="./templates/python.py"
programming_names_dict["rust"]="./templates/rust.rs"

if ! [[ -v programming_names_dict["$file_type"] ]]; then
  echo "$file_type Not Supported"
  exit 1
fi

# Create a directory called day?? with zero-padded integer from the first argument
directory_name="day$(printf "%02d" "$number")"

# Create the directory
mkdir "$directory_name"
mkdir "$directory_name/data"
cp ${programming_names_dict["$file_type"]} $directory_name

#echo "Directory '$directory_name' created for programming file type '$file_type'."
