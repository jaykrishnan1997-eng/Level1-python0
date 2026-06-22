#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_seed_inventory.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/09 15:04:21 by jkrishna            #+#    #+#            #
#   Updated: 2026/06/09 15:34:23 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

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
