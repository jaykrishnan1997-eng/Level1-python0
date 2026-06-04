# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jkrishna <jkrishna@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/04 12:28:36 by jkrishna          #+#    #+#              #
#    Updated: 2026/06/04 15:25:47 by jkrishna         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
    age = int(input("Enter plant age in days: "))
    if (age > 60):
        print("\nPlant is ready to harvest! \n")
    else:
        print("\nPlant needs more time to grow. \n")
        