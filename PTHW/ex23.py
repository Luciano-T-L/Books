# Strings, Bytes and Character Encodings
"""
- How computers store human languages for display and processing
and how Python 3 calls this "strings".
- How encode and decode Pyhon's strings into bytes.
- Handle errors in strings and byte handling
- Read code and ind out what it means even if you have
never seen it before.
"""

# Importing sys
import sys
# Arguments
script, encoding, error = sys.argv

# Creating a fuction
def main(language_file, encoding, errors):
    # Putting the line of the text in a variable
    line = language_file.readline()

# If statement
    if line:
        print_line(line, encoding, errors)
        # Makes the function run until line = False
        return main(language_file, encoding, errors)

# Creating a function
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)

# Things that I never seen before
# .encode() -> Retruns encoded version of a string
# .decode() -> Decodes the string