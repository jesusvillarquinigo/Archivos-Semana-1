file=open("devices.txt","a")
while True:
    newItem=input("Ingrese el nombre del dispositivo o ingrese exit para terminar: ")
    if newItem=="exit":
        print("¡Está hecho!")
        break
    file.write(newItem+"\n")
file.close()
    
