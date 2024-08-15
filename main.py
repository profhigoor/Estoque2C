produto = str(input("Digite o tipo de produto: "))
quantidade = int(input("Digite a quantidade em estoque: "))

if produto == "Smartphone":
    if quantidade < 10:
        print("Reabastecer estoque de smartphones")
    else:
        print("Estoque de smartphones está adequado")

elif produto == "Televisor":
    if quantidade < 5:
        print("Reabastecer estoque de televisores")
    else:
        print("Estoque de televisores está adequado")

elif produto == "Laptop":
    if quantidade < 8:
        print("Reabastecer estoque de laptops")
    else:
        print("Estoque de laptops está adequado")

else:
    if quantidade < 15:
        print("Reabastecer estoque de", produto)
    else:
        print("Estoque de", produto, "está adequado")
