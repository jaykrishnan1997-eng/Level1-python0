#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plot_area.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/04 12:08:10 by jkrishna            #+#    #+#            #
#   Updated: 2026/06/09 15:05:12 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_plot_area():
    length = int(input("Enter length: "))
    width = int(input("\nEnter width: "))
    print("\nPlot area: " + str(length * width))
