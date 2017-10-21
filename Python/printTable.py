tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidths = [0] * len(table)
    for i in range(len(table)):
        for j in range(len(table[i])):
            if len(table[i][j]) >= colWidths[i]:
                colWidths[i] = len(table[i][j])
            else:
                colWidths[i] = colWidths[i]

    for m in range(len(table[0])):
        for n in range(len(table)):
            print(table[n][m].rjust(colWidths[n] + 1), end='')
        print()

printTable(tableData)

