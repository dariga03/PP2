#Write a Python program that invoke square root function after specific milliseconds.

import time

value = int(input())
m = int(input())

time.sleep(m / 1000)

print(f"Square root of {value} after {m} miliseconds is", pow(value, 0.5))

