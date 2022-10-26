from src.controllers.pedido_controller import PedidoController

controller = PedidoController()

#exibe os itens de um pedido
resutado = controller.pegar_pedido("001")
for elemento in resutado:
    print(elemento)