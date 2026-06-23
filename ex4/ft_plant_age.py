#!/usr/bin/env python3


def ft_plant_age() -> None:
    age = int(input("Enter plant age in days: "))
    if (age > 60):
        print("\nPlant is ready to harvest! \n")
    else:
        print("\nPlant needs more time to grow. \n")
