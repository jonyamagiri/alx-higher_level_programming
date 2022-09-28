## 0x0B. Python - Input/Output

> This repository contains the tasks for `Python - Input/Output` project and a description of what each program or function does:

### Tasks

#### Task: 0-read_file.py
Write a function that reads a text file (`UTF8`) and prints it to stdout:

#### Task:  1-write_file.py
Write a function that writes a string to a text file (`UTF8`) and returns the number of characters written:

#### Task: 2-append_write.py
Write a function that appends a string at the end of a text file (`UTF8`) and returns the number of characters added:

#### Task: 3-to_json_string.py
Write a function that returns the JSON representation of an object (string):

#### Task: 4-from_json_string.py
Write a function that returns an object (Python data structure) represented by a JSON string:

#### Task: 5-save_to_json_file.py
Write a function that writes an Object to a text file, using a JSON representation:

#### Task: 6-load_from_json_file.py
Write a function that creates an Object from a “JSON file”:

#### Task: 7-add_item.py
Write a script that adds all arguments to a Python list, and then save them to a file:

#### Task: 8-class_to_json.py
Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:

#### Task: 9-student.py
Write a class `Student` that defines a student by:

#### Task: 10-student.py
Write a class `Student` that defines a student by: (based on `9-student.py`)

#### Task: 11-student.py
Write a class `Student` that defines a student by: (based on `10-student.py`)

#### Task: 12-pascal_triangle.py
**Technical interview prep:** 
Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of `n`:
* Returns an empty list if `n <= 0`
* You can assume `n` will be always an integer
* You are not allowed to import any module

#### Task: 100-append_after.py
Write a function that inserts a line of text to a file, after each line containing a specific string.

#### Task: 101-stats.py
Write a script that reads `stdin` line by line and computes metrics:
* Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`
* Each 10 lines and after a keyboard interruption (`CTRL + C`), prints those statistics since the beginning:
* * Total file size: `File size: <total size>`
* * where is the sum of all previous (see input format above)
* * Number of lines by status code:
* * * possible status code: `200, 301, 400, 401, 403, 404, 405 and 500`
* * * if a status code doesn’t appear, don’t print anything for this status code
* * * format: `<status code>: <number>`
* * * status codes should be printed in ascending order

___

#### Files:

* [test_files](https://github.com/jonyamagiri/alx-higher_level_programming/tree/master/0x0B-python-input_output/test_files)


