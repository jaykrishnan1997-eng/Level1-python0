#!/usr/bin/env python3


def ft_count_harvest_iterative() -> None:
    i = 1
    num = int(input("Days until harvest: "))
    for i in range(1, (num + 1)):
        print("\nDay " + str(i))
        i += 1
    print("Harvest time!")
