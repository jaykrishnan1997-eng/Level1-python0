# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jkrishna <jkrishna@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/04 12:12:24 by jkrishna          #+#    #+#              #
#    Updated: 2026/06/04 15:22:58 by jkrishna         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
    d1 = int(input("Day 1 harvest: "))
    d2 = int(input("\nDay 2 harvest: "))
    d3 = int(input("\nDay 3 harvest: "))
    print("\n Total harvest: " + str(d1 + d2 + d3))