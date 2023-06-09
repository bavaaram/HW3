#! /usr/bin/python3

nums = {
        "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8",
        "nine": "9", "ten": "10", "eleven": "11", "twelve": "12",
        "thirteen": "13", "fourteen": "14", "fifteen": "15", "sixteen": "16",
        "seventeen": "17", "eighteen": "18", "nineteen": "19"
}
with open("Zen.txt", "r", encoding="utf-8") as f:
    text = f.read()
text_line, emp = text.split("\n"), []
for line in text_line:
    char = line.split()
    char = list(map(lambda x: nums[x] if x in nums else x, char))
    emp.append(" ".join(char))
TEXT = "\n".join(emp)

with open("NewZen.txt", "w+", encoding="utf-8") as t:
    t.write(TEXT)
