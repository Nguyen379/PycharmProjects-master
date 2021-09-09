class Solution:
    def myAtoi(self, s: str) -> int:
        try:
            output = ""
            sign = []
            s = s.strip()

            if s[0] == "+" or s[0] == "-":
                sign.append(s[0] + "1")
                s = s[1:]

            for n in s:
                if n.isnumeric():
                    output += n
                else:
                    break

            if len(sign) == 1:
                output = int(output) * int(sign[0])
            else:
                output = int(output)

            if output < -2 ** 31:
                return -2 ** 31
            elif output >= 2 ** 31:
                return 2 ** 31 - 1
            else:
                return output
        except:
            return 0
