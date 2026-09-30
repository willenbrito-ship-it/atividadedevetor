produtos = ["Arroz", "Feijão", "Café", "Açúcar"]
 
# Mostrar a lista original
print("Lista original:")
print(produtos)
 
# Alterar o segundo produto
produtos[1] = "Macarrão"
 
# Remover um produto
produtos.remove("Café")
 
# Mostrar a lista final
print("\nLista final:")
print(produtos)
 
# Tentar remover um produto que não existe
produto = "Leite"
 
if produto in produtos:
    produtos.remove(produto)
    print(f"{produto} foi removido.")
else:
    print(f"{produto} não existe na lista.")