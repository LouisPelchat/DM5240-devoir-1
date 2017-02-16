#coding: utf-8

### Tout d'abord, n'oublie pas d'ajouter «.py» dans le nom de ton script :)

liste1 = [format(liste1) for liste1 in range(30000, 100000)]

liste2 = ["{:05d}".format(liste2) for liste2 in range(0, 18000)]

print(liste1,liste2)

### Deux listes bien formatées s'affichant successivement. C'est bien! :)

### Encore mieux, créer une seule boucle qui nous permettra de traiter chacun des numéros de permis possibles un à la fois, ainsi:

listeComplete = liste1 + liste2

for numeroDePermis in listeComplete:
	print(numeroDePermis)