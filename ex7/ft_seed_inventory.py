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
    if (seed_type == "tomato"):
        print(seed_type.capitalize() + " seeds: " + str(quantity)
              + " " + unit + " available")
    elif (seed_type == "carrot"):
        print(seed_type.capitalize() + " seeds: " + str(quantity)
              + " " + unit + " total")
    elif (seed_type == "lettuce"):
        print(seed_type.capitalize() + " seeds: " + str(quantity)
              + " " + unit + " meters")
    else:
        print("Unknown unit type")
