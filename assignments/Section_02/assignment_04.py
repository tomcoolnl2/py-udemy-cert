# Assignment 4:
"""
In the list shown below, replace the letter m with the letter x
and replace the word TV with the word television. Then print my_list.
"""

my_list = [(1, 2), (3, 4), (['c', 'd', 'a', 'm'], [3, 9, 4, 12], 4), 'TV', 42]


# Your Code Below:

char_list = my_list[2][0]
m_pos = char_list.index('m')
char_list[m_pos] = 'x'

tv_pos = my_list.index('TV')
my_list[tv_pos] = 'television'

print(my_list)

































# Solution:
# my_list[2][0][3] = 'x'
# my_list[3] = 'Television'
# print(my_list)