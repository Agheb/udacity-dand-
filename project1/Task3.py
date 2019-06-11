"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)

with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


result = []

for row in calls:
    if "(080)" in row[0]:
        if not "140" in row[1][:3]:
            matchAreaCode = re.match(r"\((.*?)\)", row[1])
            if matchAreaCode:
                result.append(matchAreaCode.group(1))
            if row[1][0] in ["7", "8", "9"]:
                result.append(row[1][:4])

# Remove duplicates in list and sort
result_a = sorted(list(dict.fromkeys(result)))

print("The numbers called by people in Bangalore have codes:")
for r in result_a:
    print(r)

count_fixed = 0
count_all = 0
for row in calls:
    if "(080)" in row[0]:
        if "(080)" in row[1]:
            count_fixed += 1

        count_all += 1


result_b = 100 * float(count_fixed) / float(count_all)
print(
    f"""{round(result_b,2)} percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."""
)