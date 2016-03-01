'''
Created on Jan 28, 2016

@author: Miranda Motsinger

I have tested this code with the given test cases and it passes all of them.
I understand that misrepresenting passing test cases is an academic
integrity violation.

Example Usage

% python mastermind.py garter garden
4:0:2

Description

mastermind.py evaluates the characters of two equal-length strings and determines how
many characters between them:
1. Match and are in the same position (x)
2. Match but are in different positions (y)
3. Don't match at all (z)

The program maintains two dictionaries, each of which mark the number of times some
char c appeared in string_one (first dictionary) and string_two (second dictionary),
excluding any chars which were perfect matches. This allows the program to find
perfect matches, imperfect matches, and no matches in linear time rather than
quadratic time.

It prints its results in the format x:y:z.
'''

import sys
import collections

perfect_match = 0
imperfect_match = 0
no_match = 0

string_one = sys.argv[1]
string_two = sys.argv[2]

# Dictionaries whose keys are the chars in string_one & string_two and whose values
# are the number of times that char appears in that string (minus perfect matches).
char_count_one = collections.defaultdict(int)
char_count_two = collections.defaultdict(int)

# Iterates over both strings' chars. If a perfect match is found, perfect_match is
# incremented; otherwise, the counts for both chars are incremented in the corresponding
# dictionaries.
for i in range(0, len(string_one)):
    if string_one[i] == string_two[i]:
        perfect_match += 1
    else:
        char_count_one[string_one[i]] += 1
        char_count_two[string_two[i]] += 1

# With perfect matches excluded, the number of imperfect matches of each char is how
# many times that char occurred in both strings.
for c in char_count_one:
    imperfect_match += min(char_count_one[c], char_count_two[c])

no_match = len(string_one) - perfect_match - imperfect_match

print(str(perfect_match) + ":" + str(imperfect_match) + ":" + str(no_match))