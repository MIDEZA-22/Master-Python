import clases

persona = clases.Persona()
persona.setNombre("Mijail Denis")
persona.setApellidos("Zavala Llanco")
persona.setAltura("1.70")
persona.setEdad("27 años")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())
print("-------------------------------------")

informatico = clases.Informatico()
informatico.setNombre("Carlos")
informatico.setApellidos("Martinez")

print(f"El informatico es: {informatico.getNombre()} {informatico.getApellidos()}")
print(informatico.getLenguajes())
print(informatico.caminar())
print(informatico.experiencia)

print("-------------------------------------")

tecnico = clases.TecnicoRedes()
tecnico.setNombre("Pinocho")
print(tecnico.auditarRedes, tecnico.getNombre(), tecnico.getLenguajes())
