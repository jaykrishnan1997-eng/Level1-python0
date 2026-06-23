#!/usr/bin/env python3


def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if (unit == "packets"):
        print(seed_type.capitalize() + " seeds: " + str(quantity)
              + " " + unit + " available")
    elif (unit == "grams"):
        print(seed_type.capitalize() + " seeds: " + str(quantity)
              + " " + unit + " total")
    elif (unit == "area"):
        print(seed_type.capitalize() + " seeds: covers" + str(quantity)
              + " " + unit + " square meters")
    else:
        print("Unknown unit type")
