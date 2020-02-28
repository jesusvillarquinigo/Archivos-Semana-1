aclNum=int(input("¿Cuál es el número ACL IPv4? "))
if aclNum>=1 and aclNum<=99:
    print("Este es un ACL IPv4 estandar")
elif aclNum>=100 and aclNum<=199:
    print("Este es un ACL IPv4 extendido")
else:
    print("Ese no es un ACL IPv4 estandar o extendido")
