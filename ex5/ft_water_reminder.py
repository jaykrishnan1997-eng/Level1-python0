#!/usr/bin/env python3


def ft_water_reminder() -> None:
    days = int(input("Days since last watering: "))
    if (days > 2):
        print("\nWater the plants!\n")
    else:
        print("\nPlants are fine \n")
