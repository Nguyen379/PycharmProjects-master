def check_move(rows, cols, letter_position):
    global output2
    char = board[rows][cols]
    # board 4x4 nen se co 16 char de chay
    if char == word2[letter_position] and output2 != word2:
        # letter_position==0 la chu cai dau tien: board[0][0]=="o"="oath"[0]
        output2 += char
        # output2 la chu tao duoc tu func check_move() nay
        # vi char "o" la chu cai dau oath => them output2 de tim tiep
        if char == word2[letter_position] and output2 == word2:
            result2.append(output2)
            output2 = ""
            return True
            # neu sau khi them chu cai tao thanh tu can tim thi se reset
            # tu tao duoc boi check_move se la "", tu tao duoc thi them vao result2
            # return True vi tim duoc tu roi, huy tat ca nhung tim kiem khac
    else:
        # khong tim duoc tu vi du nhu board[0][1]=="a" khong phai chu cai dau nen se bo luon
        return False
    # khi 1 chu cai la chu cai dau thi no se co 4 cach di chuyen: di len, di xuong, di phai, di trai
    if rows < len(board) - 1:  # dieu kien di xuong duoi la khong nam o dong cuoi
        check_move(rows + 1, cols, letter_position + 1)
    if rows > 0:  # dieu kien di len la khong nam o dong dau
        check_move(rows - 1, cols, letter_position + 1)
    if cols < len(board[0]) - 1:  # dieu kien di sang phai la ko nam o mep phai
        check_move(rows, cols + 1, letter_position + 1)
    if cols > 0:  # dieu kien di sang trai la khong nam o mep trai
        check_move(rows, cols - 1, letter_position + 1)
    # chu cai dau tien tuong thich r thi letter_position + 1 de loc sang chu tiep theo


if __name__ == '__main__':
    board = [["o", "a", "a", "n"],
             ["e", "t", "a", "e"],
             ["i", "h", "k", "r"],
             ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]
    output2 = ""
    result2 = []
    for word2 in words:  # chay tung tu mot trong word
        for row in range(len(board)):  # tung hang trong board
            for col in range(len(board[0])):  # tung cot trong board
                output2 = ""  # tu tao thanh
                check_move(row, col, 0)
    print(result2)
