class Solution:
    def convert(self, s: str, numRows):
        dict = {}
        range_up = True
        index = [0, 0]
        while True:
            try:
                if index[0] not in dict:
                    dict[index[0]] = s[index[1]]
                else:
                    dict[index[0]] += s[index[1]]
                if index[0] == 0:
                    range_up = True
                elif index[0] == numRows - 1:
                    range_up = False
                if range_up:
                    index[0] += 1
                elif not range_up:
                    index[0] -= 1
                index[1] += 1
            except:
                break
        output = ""
        for n in dict:
            output += dict[n]
        return output


print(Solution().convert("PAYPALISHIRING", 3))
