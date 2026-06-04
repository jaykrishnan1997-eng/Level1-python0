# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jkrishna <jkrishna@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/04 13:00:23 by jkrishna          #+#    #+#              #
#    Updated: 2026/06/04 15:55:41 by jkrishna         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
    i = 1
    num = int(input("Days until harvest: "))
    for i in range(1, (num + 1)):
        print("\nDay " + str(i))
        i += 1
    print("Harvest time!")
