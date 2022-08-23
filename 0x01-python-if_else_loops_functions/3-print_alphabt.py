#!/usr/bin/python3
for alphabt in range(97, 123):
    if alphabt == 101 or alphabt == 113:
        continue
    print("{:c}".format(alphabt), end='')
