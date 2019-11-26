a = input()
b = input()
c = input()
d = input()

dd = {
    "A": "MON", "B": "TUE", "C": "WED", "D": "THU", "E": "FRI", "F": "SAT", "G": "SUN"}
hh = {"0": "00", "1": "01", "2": "02", "3": "03", "4": "04", "5": "05", "6": "06", "7": "07", "8": "08", "9": "09",
      "A": "10", "B": "11", "C": "12", "D": "13", "E": "14", "F": "15", "G": "16", "H": "17", "I": "18", "J": "19",
      "K": "20", "L": "21", "M": "22", "N": "23"}

found1 = False
found2 = False
num = min(len(a), len(b))
for i in range(num):
    if found1 is False and a[i].isupper() and a[i] == b[i] and 'A' <= a[i] <= 'G':
        found1 = True
        print(dd.get(a[i]), end=" ")
    elif (a[i].isdigit() or a[i].isupper()) and found1 is True and found2 is False and a[i] == b[i] and (
            'A' <= a[i] <= 'N' or '0' <= a[i] <= '9'):
        found2 = True
        hour = str(a[i])
        print(hh.get(hour), end=":")
        break

found3 = False
num = min(len(c), len(d))
for i in range(num):
    if found3 is False and c[i] == d[i] and c[i].isalpha():
        found3 = True
        if i in range(0, 10):
            print("0" + str(i), end="")
        else:
            print(i, end="")
        break
