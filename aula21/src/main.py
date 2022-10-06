from views.lista_de_tarefas_view import ListatarefasView
from controllers.tarefa_controller import TarefaController

if __name__ == "__main__":
    tarefas_controller = TarefaController()
    tarefas_view = ListatarefasView(tarefas_controller)