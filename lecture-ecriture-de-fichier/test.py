fichier = open("file.txt", "rt")

print("contenu du fichier avant ecriture: \"" + fichier.read() + "\"")

fichier.close()

fichier = open("file.txt", "wt")

fichier.write("message")

fichier.close()

fichier = open("file.txt", "rt")

print("contenu du fichier apres ecriture : \"" + fichier.read() + "\"")

fichier.close()
