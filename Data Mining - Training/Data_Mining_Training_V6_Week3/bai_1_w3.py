# Cho một mảng đã sắp xếp của các chuỗi. Mảng đầu vào bao gồm các chuỗi rỗng. Hãy viết một phương thức tìm vị trí
# [“at”, “”, “”, “”, “ball”, “”, “”, “car”, “”, “”, “dad”, “”, “”] -> tìm ball -> vị trí thứ 4
# [“at”, “”, “”, “”, “”, “ball”, “car”, “”, “”, “dad”, “”, “”] -> tìm balldad -> trả về -1
s = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
a = "ball"
s2 = ["at", "", "", "", "", "ball", "car", "", "", "dad", "", ""]
a2 = "balldad"


class Search:
    def __init__(self, lst):
        self.lst = lst

    def search(self, start, end, target):
        if start > end:
            return -1
        position = (start + end) // 2
        if self.lst[position] == target:
            return position
        elif self.lst[position] == "":
            left = self.search(start, position-1, target)
            right = self.search(position + 1, end, target)
            return max(left, right)
        elif self.lst[position] < target:
            return self.search(position + 1, end, target)
        elif self.lst[position] > target:
            return self.search(start, position - 1, target)


search = Search(s2)
print(search.search(0, len(s)-1, a2))
