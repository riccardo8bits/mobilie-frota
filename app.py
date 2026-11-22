import asyncio
import flet as ft
from flet import ThemeMode, Colors, ListView, FontWeight, TextOverflow
from endpoints import buscar_viaturas


def tela_login(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.title = "LOGIN"
    page.theme_mode = ThemeMode.LIGHT
    page.window.width = 400
    page.window.height = 700

    def entrar(e):
        page.controls.clear()
        tela_home(page)
        page.update()

    logo = ft.Image(
        src="/home/ricardo/Documents/mobilie-frota/static/pmsc.jpeg",
        width=120,
        height=120,
        fit=ft.BoxFit.CONTAIN
    )
    
    texto_logo = ft.Text("PMSC", size=18, weight="bold")
    campo_matricula = ft.TextField(label="Matrícula")
    campo_senha = ft.TextField(label="Senha", password=True)
    botao_entrar = ft.Button(content="ENTRAR", on_click=entrar)

    page.add(
        ft.Column([
            logo,
            texto_logo,
            campo_matricula,
            campo_senha,
            botao_entrar
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20)
    )
    page.update()


def tela_home(page: ft.Page):
    page.title = "VIATURAS"
    lista_viaturas = buscar_viaturas()
    controles = []

    # Função para voltar ao login
    def sair(e):
        page.controls.clear()
        tela_login(page)
        page.update()

    for viatura in lista_viaturas:
        prefixo = viatura.prefixo
        modelo = viatura.modelo
        placa = viatura.placa

        card = ft.Container(
            bgcolor="white",
            border=ft.Border.all(1, "#CCCCCC"), 
            border_radius=8,
            padding=15,
            width=350,
            content=ft.Row([
                ft.Column([
                    ft.Text(prefixo, weight="bold", color="#333333", size=16),
                    ft.Text(modelo, color="#666666", size=14),
                    ft.Text(placa, color="#666666", size=12),
                ], spacing=4, expand=True),
                
                ft.Button(
                    content="CHECKLIST",
                    bgcolor="#f85c1b",
                    color="white",
                    on_click=lambda e, v=viatura: tela_checklist(page, v)
                )
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        )
        controles.append(card)

    page.add(
        ft.Column([
            # --- AQUI ESTÁ A MUDANÇA ---
            # Trocamos o Text simples por um Row com o título e o botão de sair
            ft.Row([
                ft.Text("Viaturas", size=20, weight="bold"),
                ft.IconButton(
                    icon=ft.Icons.LOGOUT, 
                    icon_color="red",
                    tooltip="Sair do sistema",
                    on_click=sair
                )
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, width=350),
            # ---------------------------

            ft.ListView(
                controls=controles,
                spacing=10,
                expand=True
            )
        ], expand=True)
    )
    page.update()


def tela_checklist(page: ft.Page, viatura):
    page.controls.clear()
    page.title = f"Checklist - {viatura.prefixo}"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Função do botão voltar
    def voltar(e):
        page.controls.clear()
        tela_home(page)
        page.update()

    # Função para quando clicar em Finalizar
    def finalizar(e):
        # Conta quantos itens foram marcados
        marcados = sum(1 for c in checkboxes if c.value)
        total = len(checkboxes)
        
        # Mostra um aviso na tela (SnackBar)
        page.show_dialog(ft.SnackBar(
            content=ft.Text(f"Checklist da {viatura.prefixo} salvo! ({marcados}/{total} itens OK)"),
            bgcolor="green"
        ))

    # Criando os itens do checklist
    checkboxes = []
    itens_texto = [
        "Documentação (CRLV) em dia",
        "Giroflex e Sirene funcionando",
        "Pneus em boas condições",
        "Luzes (faróis e lanternas) OK",
        "Extintor de incêndio válido",
        "Rádio comunicador funcionando",
        "Lataria e vidros sem avarias"
    ]

    # Montando o visual dos checkboxes num container com borda
    itens_controls = []
    for texto in itens_texto:
        cb = ft.Checkbox(label=texto, value=False)
        checkboxes.append(cb)
        itens_controls.append(cb)

    # Tela em si
    page.add(
        ft.Column([
            # Cabeçalho
            ft.Row([
                ft.IconButton(ft.Icons.ARROW_BACK, on_click=voltar),
                ft.Text(f"CHECKLIST: {viatura.prefixo}", size=18, weight="bold"),
            ], alignment=ft.MainAxisAlignment.START),
            
            ft.Text(f"Modelo: {viatura.modelo} | Placa: {viatura.placa}", color="#666666"),
            ft.Divider(),
            
            # Caixa com os itens
            ft.Container(
                content=ft.Column(itens_controls, spacing=10),
                bgcolor="white",
                border=ft.Border.all(1, "#CCCCCC"),
                border_radius=8,
                padding=15,
                width=350
            ),
            
            ft.Container(height=10),
            
            # Botão Finalizar
            ft.Button(
                content="FINALIZAR CHECKLIST",
                width=350,
                bgcolor="#f85c1b",
                color="white",
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
                on_click=finalizar
            )
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15)
    )
    page.update()


ft.run(tela_login, assets_dir="static")