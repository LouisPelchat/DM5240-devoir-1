#coding: utf-8

liste1 = [format(liste1) for liste1 in range(30000, 100000)]

liste2 = ["{:05d}".format(liste2) for liste2 in range(0, 18000)]

print(liste1,liste2)
