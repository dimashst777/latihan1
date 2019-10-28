Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Penggunaan end

print('A', end="")

print('B', end="")

print('C', end="")

print()

print('X')

print('Y')

print('Z')



print("-"*1000)





# Penggunaan separator

w, x, y, z = 10, 15, 20, 25

print(w, x, y, z, sep=',')

print(w, x, y, z, sep='')

print(w, x, y, z, sep=':')

print(w, x, y, z, sep='- - - - -')



print("-"*1000)





# String format

print(0, 10 ** 0)

print(1, 10 ** 1)

print(2, 10 ** 2)

print(3, 10 ** 3)

print(4, 10 ** 4)

print(5, 10 ** 5)

print(6, 10 ** 6)

print(7, 10 ** 7)

print(8, 10 ** 8)

print(9, 10 ** 9)

print(10, 10 ** 10)



print("-"*1000)



# String format

print('{0:>3} {1:>16}'.format(0, 10 ** 0))

print('{0:>3} {1:>16}'.format(1, 10 ** 1))

print('{0:>3} {1:>16}'.format(2, 10 ** 2))

print('{0:>3} {1:>16}'.format(3, 10 ** 3))

print('{0:>3} {1:>16}'.format(4, 10 ** 4))

print('{0:>3} {1:>16}'.format(5, 10 ** 5))

print('{0:>3} {1:>16}'.format(6, 10 ** 6))

print('{0:>3} {1:>16}'.format(7, 10 ** 7))

print('{0:>3} {1:>16}'.format(8, 10 ** 8))

print('{0:>3} {1:>16}'.format(9, 10 ** 9))

print('{0:>3} {1:>16}'.format(10, 10 ** 10))
