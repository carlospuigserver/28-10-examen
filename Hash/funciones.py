import hash
import hashlib

def Encript():
    key=("Luke, yo soy tu padre")
    Encriptkey=hashlib.md5(key.encode("ASCII")).hexdigest()
    print("La key encriptada es:  ",Encriptkey[:8])

Encript()

