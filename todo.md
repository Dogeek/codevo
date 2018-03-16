# TO DO :

## UI :

- dégats
- utilisation de la magie (méthode)
- UI messages sur l'écran

## Console:

- interpreter une commande simple (cls pour CLear Screen)
- commande "macro" pour créer un alias vers une liste de commandes
- faire un "output prompt" et un "next prompt" : "<" et "..."

## Entities :

- refactorer, enlever le fichier de config pour les ennemis
- une classe par ennemi qui hérite de la classe Entity
- un seul ennemi apparait même si on en met 2
- il poppent sur la pos du joueur ?
- check l'emplacement des rects des ennemis

## Level :

- tilemap a changer avec des layers :
	- -1 sous le sol
	- 0 sol
	- 1 petit objet
	- 2 gros objet (ennemi volant bloqué)
- spawn d'ennemi a revoir ça n'en fait spawn qu'un
- changement d'écran : le draw est pas instantané, et les collisions sont pas recalculées

## GridEntities :

- pont qui bouge quand on marche dessus (ennemi et joueur)

## Autres :

- Editeur de niveaux
- fonction de debug pour afficher les collisions en jeu (les rects de sprites qui collide)
