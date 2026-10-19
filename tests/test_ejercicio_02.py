from playwright.sync_api import Page, expect


def test_ejercicio_02_verificar_titulo(page: Page):
    page.goto("https://the-internet.herokuapp.com/")

    titulo = page.title()
    print("Título obtenido:", titulo)

    expect(page).to_have_title("The Internet")