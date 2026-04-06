import flet as ft


def main(page: ft.Page):
    # Variável com a imagem certa
    imagem_correta = "Cachorro"

    # Texto para feedback
    mensagem = ft.Text(
        "Qual vc acha que pegou a referencia?",
        text_align=ft.TextAlign.CENTER,
        size=20,
        height=50
    )

    # Função Jogar
    def jogar(e):
        imagem_selecionada = e.control.content.value
        if imagem_selecionada == imagem_correta:
            e.control.bgcolor = ft.Colors.GREEN_200
            e.control.image.opacity = 0.3
            e.control.content.value = "🔥"
            e.control.content.size = 40
            mensagem.value = "Parabéns! Você acertou."
        elif imagem_selecionada == "Floppa":
            e.control.bgcolor = ft.Colors.BLUE_200
            e.control.image.opacity = 0.3
            e.control.content.value = "🧼"
            e.control.content.size = 40
            mensagem.value = "Ele e o Floppa, ele só esta tomando banho"
        else:
            e.control.bgcolor = ft.Colors.RED_200
            e.control.image.opacity = 0.3
            e.control.content.value = "💀"
            e.control.content.size = 40
            mensagem.value = "Perdeu mil auras"

        container_gato.on_click = None
        container_cachorro.on_click = None
        container_floppa.on_click = None

        btn_jogar_novamente.visible = True

        page.update()

    # Função Jogar Novamente
    def jogar_novamente(e):
        btn_jogar_novamente.visible = False
        mensagem.value = "Qual vc acha que pegou a referencia?"

        container_gato.image.opacity = 1.0
        container_gato.on_click = jogar
        container_gato.content.size = 0
        container_gato.content.value = "Gato"

        container_cachorro.image.opacity = 1.0
        container_cachorro.on_click = jogar
        container_cachorro.content.size = 0
        container_cachorro.content.value = "Cachorro"

        container_floppa.image.opacity = 1.0
        container_floppa.on_click = jogar
        container_floppa.content.size = 0
        container_floppa.content.value = "Floppa"

        page.update()

    # Container Cachorro
    container_gato = ft.Container(
        content=ft.Text(
            "ave",
            size=0
        ),
        image=ft.DecorationImage(
            src="images/ave.webp",
            fit=ft.BoxFit.COVER
        ),
        width=120,
        height=120,
        margin=10,
        bgcolor=ft.Colors.GREY_200,
        border_radius=10,
        alignment=ft.Alignment(0, 0),
        ink=True,
        on_click=jogar
    )
    # Container aguila
    container_cachorro = ft.Container(
        content=ft.Text(
            "Cachorro",
            size=0
        ),
        image=ft.DecorationImage(
            src="images/aguila.png",
            fit=ft.BoxFit.COVER
        ),
        width=120,
        height=120,
        margin=10,
        bgcolor=ft.Colors.GREY_200,
        border_radius=10,
        alignment=ft.Alignment(0, 0),
        ink=True,
        on_click=jogar
    )
    # Container Floppa
    container_floppa = ft.Container(
        content=ft.Text(
            "Floppa",
            size=0
        ),
        image=ft.DecorationImage(
            src="images/floppa.jpg",
            fit=ft.BoxFit.COVER
        ),
        width=120,
        height=120,
        margin=10,
        bgcolor=ft.Colors.GREY_200,
        border_radius=10,
        alignment=ft.Alignment(0, 0),
        ink=True,
        on_click=jogar
    )
    # Botão "Jogar Novamente"
    btn_jogar_novamente = ft.Button(
        "Jogar Novamente",
        visible=False,
        on_click=jogar_novamente
    )

    page.add(
        ft.Column(
            [
                ft.Text(
                    "Qual pegou a referencia????",
                    size=24,
                    weight="bold"
                ),
                mensagem,
                ft.Row(
                    [
                        container_gato,
                        container_cachorro,
                        container_floppa
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                btn_jogar_novamente
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )


ft.run(main)
