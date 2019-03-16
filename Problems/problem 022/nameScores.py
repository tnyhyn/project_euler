import csv

def solve():
    namesList = extract_textFile('p022_names.txt')
    namesList.sort()
    listScore = 0
    for index, name in enumerate(namesList):
        nameScore = 0
        for c in name:
            nameScore += ord(c) - 64
        listScore += nameScore * (index + 1)
    print(listScore)

def extract_textFile(file):
    textList = []
    with open(file) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            textList.append(row)
    textList = textList[0]
    f.close()
    return textList

solve()

# Answer: 871198282