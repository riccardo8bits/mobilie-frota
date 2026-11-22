import flet as ft
# Importe as telas quando criarmos elas (por enquanto vamos deixar comentado)
# from views.login_view import tela_login
# from views.home_view import tela_home

def mudar_rota(page: ft.Page):
    rota = page.route
    page.controls.clear() # Limpa a tela atual
    
    if rota == "/" or rota == "/login":
        # Aqui vai entrar a chamada da sua tela de login
        print("Desenhando tela de login")
        # tela_login(page) 
        
    elif rota == "/home":
        # Aqui vai entrar a chamada da tela de viaturas
        print("Desenhando tela home (lista de viaturas)")
        # tela_home(page)
        
    else:
        page.add(ft.Text("Rota não encontrada (Erro 404)"))

    page.update()

def configurar_rotas(page: ft.Page):
    # Diz para o Flet: "toda vez que a rota mudar, chame a função mudar_rota"
    page.on_route_change = mudar_rota
    # Define a rota inicial do app
    page.go("/login") 