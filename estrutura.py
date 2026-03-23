import flet as ft
#IMPORTA A BIBLIOTECA FLET E CRIA UM APELIDO(ALIAS)

def main(page: ft.Page):
    page.title = "Meu primeiro App Flet" #Define o titulo da janela
    page.bgcolor = "red"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.add(
        ft.Text("Bem-vindo ao meu app"),
        ft.Text("Aqui voce pode criar o que quiser!!")
    )

ft.run(main)