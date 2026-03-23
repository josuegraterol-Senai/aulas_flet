import flet as ft


def main(page: ft.Page):

    def mostrar_mensagem(e):
        page.add(
            ft.Text("Primera sangre!!"),
            ft.Text("Double kill!!"),
            ft.Text("Triple kill!!")
        )

    page.add(
        ft.Text("Cod mobile"),
        ft.Text("El exito no es definitivo  y el fracaso no es fatal"),
        ft.Image(
            src="images/call.webp",
            width=300,
            height=150
        ),
        ft.Button(
            content="Listo para Jugar..?",
            on_click=mostrar_mensagem
        )
    )


ft.run(main)