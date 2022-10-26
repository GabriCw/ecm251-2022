from src.controllers.pedido_controller import PedidoController

controller = PedidoController()

#exibe os itens de um pedido
resutado = controller.pegar_pedido("001")
for elemento in resutado:
    print(elemento)

item_pedido = resutado[0]
item_pedido.quantidade = 10
controller.atualizar_pedido(item_pedido)

print("--------------------------------------")
resutado = controller.pegar_pedido("001")
for elemento in resutado:
    print(elemento)