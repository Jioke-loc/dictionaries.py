# create a dic.

bio = {
    "name": "Desmond",
    "age": "29",
    "complextion": "light skinned"
}
print(bio["name"])

# using dic translate numbers to words.
phone = input("type your phone num: ")
digits = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}
output= " "
for ch in phone:
    output += digits.get(ch, "!") + " "
print(output)