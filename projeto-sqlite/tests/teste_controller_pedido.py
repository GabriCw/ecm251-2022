from src.controllers.pedido_controller import PedidoController
from src.models.pedido import Pedido

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

print("--------------------------------------")
pedido = Pedido(id="151", id_item="10", id_cliente="ZEZE", data_hora="26/10/2022", numero_pedido="1234", quantidade=2)
controller.inserir_pedido(pedido)
resutado = controller.pegar_pedido(numero_pedido="1234")
for elemento in resutado:
    print(elemento)
print("--------------------------------------")
for elemento in resutado:
    controller.deletar_pedido(elemento.id)
    
resutado = controller.pegar_pedido(numero_pedido="1234")
for elemento in resutado:
    print(elemento)