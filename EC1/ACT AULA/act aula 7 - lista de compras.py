persona1 = {"rojo", "azul", "verde", "amarillo", "purpura", "blanco"}
persona2 = {"rojo", "verde", "rosa", "naranja", "blanco", "marron"}

print("Elementos que ambas personas desean comprar:")
common = persona1.intersection(persona2)
for item in common:
    print(f" - {item}")
