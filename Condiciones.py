# If - condicionales
calificacion = input("Cual es tu calificación de la AZ-900: ")

#Trasnformar calificacion de "str" a "int"
calificacion = int(calificacion)

if calificacion < 700 : # Si la calificación es menor a 700
    print("No pasaste amigo 😔")
elif calificacion == 700 : # Calificacion es exacto a 700
    print ("Pasaste, pero de panzazo!!👍")
elif calificacion > 1000 : # Calificación es mayor o igual a 1000
    print("Mentiroso, no hay mas allá de 1,000 pts 😠")
elif calificacion > 700 : # Calificación mayor a 700
    print("Felicidades, pasaste el examen!!! 🙌")

# Verificador de mayoria de edad
edad = input("Introduce tu edad: ")
edad = int(edad) # Cambiar str a int

if edad == 22 : # Edad igual a 22
    print("Woow, tienes la misma edad que yo")
elif edad >= 18 and edad <= 100: # Edad mayor o igual a 22 "and" edad menor o igual a 100
    print("Eres una persona legal")
elif edad < 0 : # Edad menor a 0
    print("No existes!!")
elif edad < 18 : # Edad menor a 18
    print("Aun te faltan años")
else : # Edad otro número
    print("Eres un super humano o estas mintiendo")
