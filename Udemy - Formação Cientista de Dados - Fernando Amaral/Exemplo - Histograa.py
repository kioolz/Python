# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 21:24:54 2019

@author: Caio
"""


num_friends= [100,49, 41, 40, 25]


friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]
plt.bar(xs,ys)
plt.axis([0,101, 0, 25])
plt.title("Histograma da Contagem de Amigos")

plt.xlabel("# de amigos")
plt.ylabel("# de pessoas")
plt.show()