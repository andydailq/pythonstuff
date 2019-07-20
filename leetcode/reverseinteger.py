class Solution:
    def reverse(self, x):
        string = str(x)
        if x > 0:
            reverse = int(string[::-1])
            if reverse <= (2 ** 31) - 1:
                return reverse
            elif reverse > (2 ** 31) - 1:
                return 0
        elif x < 0:
            lists = []
            new_str = ''
            reverse = string[::-1]
            for i in range(len(reverse)):
                lists.append(reverse[i])
            for j in range(len(reverse) - 1):
                new_str += lists[j]
            negative = lists.pop()
            new = int(negative + new_str)
            if new >= -(2 ** 31):
                return new
            elif new < -(2 ** 31):
                return 0
        elif x == 0:
            return 0