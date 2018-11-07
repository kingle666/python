# def aplly_twice(func,arg):
#     return func(func(arg))
# def add_five(x):
#     return x + 5
# print(aplly_twice(add_five,10))
# def test(func,arg):
#     return func(func(arg))
# def mult(x):
#     return x*x
# print(test(mult,2)
# print((lambda x: x*x)(1000))

# def add_five(x):
#     return x + 5
#
# nums = [11, 22, 33, 44, 55]
#
# result = list(map(add_five,nums))
#
# print(result)

# nums = [1, 2, 5, 8, 3, 0, 7]
# res = list(filter(lambda x:x<5,nums))
# print(res)

# def coumus():
#     i=5
#     while i > 0:
#         yield i
#         i -= 1
#
# for i in coumus():
#     print(i)
#
# def numbers(x):
#     for i in range(x):
#         if i % 3 == 0:
#             yield i
#
# print(list(numbers(50)))


# def log(func):
#     def wraper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wraper()

#
# def print_text():
#     print("hello")
#
# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return x * factorial(x-1)
#
# print(factorial(5))
# def fib(x):
#     if x == 0 or x == 1:
#         return 1
#     else:
#         return fib(x-1)+fib(x-2)
# print(fib(4))
# nums = {1, 2, 3, 4, 5}
# word = set(["spam","sggs","sausage"])8
# print(3 in nums)
# print("spam" not in word)

# from itertools import count
# for i in count(3):
#     print(i)
#     if i >=11:
#         break
#
# nums = 5 / 2
# print(nums)

from itertools import accumulate,takewhile,product

# nums = list(accumulate(range(8)))
#
# print(nums)
# print(list(takewhile(lambda x:x<=6,nums)))

# a = {
#     1,
#     2
# }
# print(len(list(product(range(3),a))))

a = (lambda x: x*(x+1))
(6)
print(a)