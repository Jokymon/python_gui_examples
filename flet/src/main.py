import flet as ft


def main(page: ft.Page):
    name_input = ft.TextField(label="Name")
    greeting_output = ft.Text("")

    def create_greeting(event):
        name = name_input.value
        greeting_output.value = f"Hello {name}"
        greeting_output.update()

    layout = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Text("Lass dich begrüssen"), expand=True
                        )
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Text("Wie ist dein Name?"), expand=True
                        ),
                        ft.Container(
                            content=name_input,
                            expand=True,
                        ),
                    ],
                ),
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.FloatingActionButton(
                                "Begrüsse", on_click=create_greeting
                            ),
                            expand=True,
                        )
                    ]
                ),
                ft.Row(controls=[ft.Container(content=greeting_output, expand=True)]),
            ],
            spacing=10,
        ),
        expand=True,
    )

    page.add(layout)
    page.title = "Flet example GUI"
    page.window.width = 390
    page.window.height = 250
    page.update()


ft.app(main)
