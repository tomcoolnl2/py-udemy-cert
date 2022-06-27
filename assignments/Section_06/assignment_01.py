# Assignment 1:

import sys
import os
import re

# directory_containing_files = "/Users/imtiazahmad/PycharmProjects/Assignments/Section_06/project_files" #sys.argv[1]
# words_to_aggregate = ["hello", "Peter", "computer"] #sys.argv[2:]
directory_containing_files = sys.argv[1]
words_to_aggregate = sys.argv[2:]

# Expected Output:
# {"there": n, "Michael": n, "running": n}

# Your Code Below:


# I ran this from the root of the project:
# python3 ./assignments/Section_06/assignment_01.py ./assignments/Section_06/project_files hello Peter computer
# python3 ./assignments/Section_06/assignment_01.py ./assignments/Section_06/project_files Michael running there in

print(directory_containing_files)
print(words_to_aggregate)

words_and_counts = {}

for word in words_to_aggregate:
    count = 0
    for path, folder_names, file_names in os.walk(directory_containing_files):
        for file_name in file_names:
            try:
                with open(os.path.join(path, file_name), 'r+') as file:
                    for line in file:
                        if re.search(word, line):
                            word_list = re.findall(word, line)
                            count += len(word_list)
            except FileNotFoundError:
                raise FileNotFoundError('No files found...')
            except TypeError:
                raise TypeError('There was a type error...')
            except:
                print('Something went wrong...')
            finally:
                print('This will always run!')

    words_and_counts[word] = count

print(words_and_counts)







#Solution:
# words_and_counts = {}
#
# for word in words_to_aggregate:
#     count = 0
#     for path, folder_names, file_names in os.walk(directory_containing_files):
#         for file_name in file_names:
#             file = os.path.join(path, file_name)
#             with open(file, "r") as a_file:
#                 for line in a_file:
#                     if re.search(word, line):
#                         word_list = re.findall(word, line)
#                         count += len(word_list)
#
#     words_and_counts[word] = count
#
#
#
# print(words_and_counts)