#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_water_reminder.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/04 12:36:00 by jkrishna            #+#    #+#            #
#   Updated: 2026/06/09 15:05:05 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_water_reminder() -> None:
    days = int(input("Days since last watering: "))
    if (days > 2):
        print("\nWater the plants!\n")
    else:
        print("\nPlants are fine \n")
