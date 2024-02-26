def decryptRailFence(cipher, key, repeat):
    result = cipher
    for _ in range(repeat):
        rail = [['\n' for _ in range(len(result))]
                for _ in range(key)]

        dir_down = None
        row, col = 0, 0

        for i in range(len(result)):
            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False

            rail[row][col] = '*'
            col += 1

            if dir_down:
                row += 1
            else:
                row -= 1

        index = 0
        for i in range(key):
            for j in range(len(result)):
                if ((rail[i][j] == '*') and
                        (index < len(result))):
                    rail[i][j] = result[index]
                    index += 1

        result = []
        row, col = 0, 0
        for i in range(len(cipher)):
            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False

            if rail[row][col] != '*':
                result.append(rail[row][col])
                col += 1

            if dir_down:
                row += 1
            else:
                row -= 1
        result = "".join(result)

    return result