import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''
sentence = 'Start a sentence and then bring it to an end'
pattern = re.compile(r"\d\d\d.\d\d\d.\d\d\d\d")
matches = pattern.finditer(text_to_search)
# literal search
for match in matches:
    print(match)

with open("data.txt", "r") as f:
    contents = f.read()
    pattern = re.compile(r"(Mr|Ms|Mrs)\.?\s[A-Z]\w*")  # anything except inside brackets
    # []: a single character inside bracket
    # [1-5]: any single character from 1 to 5
    # [a-zA-Z]: from a to z, from A to Z
    # cach 1: pattern = re.compile(r"\d\d\d.\d\d\d.\d\d\d\d")
    # cach 2: pattern = re.compile(r"\d{3}.\d{3}.\d{4}
    # {n}: n times, {n,m}: n to m times
    # x*: 0 or more occurrences of x
    # x+: 1 or more occurrences of x
    # x?: 0 or 1 occurrence of x
    # (): multiple patterns

    matches = pattern.finditer(text_to_search)
    for match in matches:
        print(match)

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''
# pattern = re.compile(r"[a-zA-Z0-9_+.-]+@[a-zA-Z0-9_+.-]+\.(com|edu|net)")

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")
matches = pattern.finditer(urls)
# findall: return only group if there are groups or else return fully
for match in matches:
    print(match.group(1))
    # 0 print all, 1 first group () in this case www.

subbed_urls = pattern.sub(r'\2\3', urls)
# substitute matched results in urls with group 2 and 3 of said url.
print(subbed_urls)

pattern = re.compile(r'Start', re.IGNORECASE)
# re.IGNORECASE = ignore upper and lower case

matches = pattern.match(sentence)
# doesn't return an iterable, only 1st match
print(matches)
