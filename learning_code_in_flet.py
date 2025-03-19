import flet as ft 

def main(page: ft.Page):
    def setup_widgets():
        return {
            "main_container": ft.Container(
                margin=ft.Margin(0, 0, 0, 0),
                padding=ft.Padding(20, 0, 20, 20),
                bgcolor="",
                width=400,
                height=400,
                expand=False,
                border_radius=ft.BorderRadius(10, 10, 10, 10),
            )
        }
    
    widgets = setup_widgets()

    page.add(ft.Row(
        [widgets["main_container"]],
        ft.MainAxisAlignment.CENTER
    ))

    page.update()
    

ft.app(main)