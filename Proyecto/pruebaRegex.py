import re 

patron = "^(SDF|SDT|SDR)$"
string = "SdF"


if (re.match(patron, string, re.IGNORECASE)):
    print("Match found!")
else:
    print("No match.")



# string = "   12345"

# if string.strip().isdigit():
#     print("The string represents a digit.")
# else:
#     print("The string does not represent a digit.")