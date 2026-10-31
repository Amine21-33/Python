# Def 1:
"""def cube(R):
    return R ** 3
def vol_sphere(R):
    return (4 / 3) * 3.14 * cube(R)
R = int(input("Entrez le rayon de la sphere: "))
print(f"Le volume de la sphere est: {vol_sphere(R)}")"""

# Def 2:
"""def positif(nbr):
    while nbr < 0:
        nbr = int(input("Entrez un nombre positif: "))
    return nbr
def somme_diviseurs(nbr):
    somme = 0
    for i in range(1, nbr + 1):
        if nbr % i == 0:
            somme += i
    return somme

nbr = int(input("Entrez un nombre: "))
x = positif(nbr)
sx = somme_diviseurs(x)
print(f"La somme des diviseurs de {x} est: {sx}")
nbr = int(input("Entrez un nombre: "))
y = positif(nbr)
sy = somme_diviseurs(y)
print(f"La somme des diviseurs de {y} est: {sy}")

if sx == sy:
    print(f"Les deux nombres {x} et {y} sont amis")"""

# Def 3:

"""def triangle(h):
    j = 1
    for i in range(h, 0, -1):
        print(" " * i, j * "*")
        j += 2"""
       
# Def 4:

"""def rationel(n, d):
    return f"{n}/{d}"
def resultat(op):
    if op == "+":
        r = n1/d1 + n2/d2
        return r
    elif op == "-":
        r = n1/d1 - n2/d2
        return r
    elif op == "/":
        r = (n1/d1) / (n2/d2)
        return r
    elif op == "x":
        r = (n1/d1) * (n2/d2)
        return r
    
    

n1 = int(input("Numérature du 1er nombre: "))
d1 = 0
while d1 == 0 :
    d1 = int(input("Dénominateur du 1er nombre: "))
if d1 != 0:
    print("\n")

n2 = int(input("Numérature du 2e nombre: "))
d2 = 0
while d2 == 0 :
    d2 = int(input("Dénominateur du 2e nombre: "))
if d2 != 0 :
    print("\n")
op = input("Opération: ")
if op == "/" and n2 == 0:
    print("Error")
elif op != "+" and op != "/" and op != "x" and op != "-" :
    print("invalid opération")
else:
    print(rationel(n1, d1), op, rationel(n2, d2), "=", resultat(op))"""

# Def 5 & 6 & 7:
"""def square(n):
    return n ** 2
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    elif c >= a and c >= b:
        return c
    
def calculate_average(grades):
    if len(grades) == 0 :
        return 0
    
    S = 0
    for grade in grades:
        S += grade 

    return S / len(grades)

print(square(4))
print(max_of_three(5, 5, 3))       
print(max_of_three(2, 9, 4))       
print(calculate_average([10, 15, 20]))  
print(calculate_average([]))"""

# Def 8:
"""def calculate_discount(price, percentage):
    if price < 0 or percentage > 100 or percentage < 0: 
        return "Invalid input"
    elif percentage == 0:
        return price
    else :
        return price - price * percentage/100

print(calculate_discount(200, 25))  
print(calculate_discount(200, 0))    
print(calculate_discount(-50, 10))  
print(calculate_discount(200, 120))"""