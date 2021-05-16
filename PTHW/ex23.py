# Strings, Bytes and Character Encodings
"""
- How computers store human languages for displau and processing
and how Python 3 calls this "strings".
- How encode and decode Pyhon's strings into bytes.
- Handle errors in strings and byte handling
- Read code and ind out what it means even if you have
never seen it before.
"""
import sys
script, encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding,errors)


def print_line(line, enconding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", encoding="utf-8")


languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)

#Doing a test 2