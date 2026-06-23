#!/usr/bin/env python3


def ft_recursive(num) -> None:
    if (num > 1):
        ft_recursive(num - 1)
    print("\nDay " + str(num))


def ft_count_harvest_recursive() -> None:
    num = int(input("Days until harvest: "))
    ft_recursive(num)
    print("\nHarvest time! \n")
