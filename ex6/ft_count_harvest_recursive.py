#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_count_harvest_recursive.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/04 13:07:47 by jkrishna            #+#    #+#            #
#   Updated: 2026/06/09 15:05:48 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_recursive(num) -> None:
    if (num > 1):
        ft_recursive(num - 1)
    print("\nDay " + str(num))


def ft_count_harvest_recursive() -> None:
    num = int(input("Days until harvest: "))
    ft_recursive(num)
    print("\nHarvest time! \n")
