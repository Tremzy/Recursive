class Recursive():
    def __init__(self):
        pass
    def sort(self, _list):
        if len(_list) <= 1:
            return _list
        else:
            pivot = _list[0]
            less = [i for i in _list if i < pivot]
            greater = [i for i in _list if i > pivot]
            return self.sort(less) + [pivot] + self.sort(greater)
    def fib(self, limit):
        a, b = 0, 1
        count = 0
        def calcFib(a, b, count):
            a, b = b, a + b
            count += 1
            if count != limit:
                return calcFib(a, b, count)
            else:
                return b
        return calcFib(a, b, count)
    def fact(self, n: int):
        if n == 1:
            return 1
        else:
            return n * self.fact(n-1)
    def sum(self, lst: list):
        if len(lst) == 0:
            return 0
        else:
            return lst[0] + self.sum(lst[1:])
    def reverse(self, s: str):
        if s == "":
            return ""
        else:
            return s[-1] + self.reverse(s[:-1])     
    def listcounter(self, lst: list):
        if len(lst) == 0:
            return 0
        else:
            return 1 + self.listcounter(lst[1:])
    def palindrome(self, s: str):
        if len(s) <= 1:
            return True
        else:
            if s[0].lower() == s[-1].lower():
                return self.palindrome(s[1:-1])
            else:
                return False
    def binarysearch(self, lst: list, target):
        if len(lst) <= 1 and lst[0] != target:
            return -1
        else:
            if lst[len(lst)//2] == target:
                return lst[len(lst)//2]-1
            else:
                if target > lst[len(lst)//2]:
                    return self.binarysearch(lst[len(lst)//2:], target)
                else:
                    return self.binarysearch(lst[:len(lst)//2], target)
            
x = Recursive()
print(x.sort([3, 1, 2, 8, 6, 7, 9, 5]))
print(x.fib(10))
print(x.fact(5))
print(x.sum([1, 2, 3, 4]))
print(x.reverse("hello"))
print(x.listcounter([1, 2, 3]))
print(x.palindrome("civic"))
print(x.binarysearch([1,2,3,4,5], 5))