import pandas
import turtle

screen = turtle.Screen()
screen.title("Estados do Brasil")
imagem = "mapa_brasil.gif"
screen.addshape(imagem)
turtle.shape(imagem)

# def get_mouse_click_coord(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coord)
#
# turtle.mainloop()

dado = pandas.read_csv("estados_brasil_coord.csv")
lista_estados = dado.estado.to_list()
estados_acertados = []

while len(estados_acertados) < 27:
    resposta_estado = screen.textinput(title=f"{len(estados_acertados)}/27 Estados Corretos",
                                       prompt="Qual é o nome de outro estado?").title()

    if resposta_estado == "Sair":
        estados_faltando = []
        for estado in lista_estados:
            if estado not in estados_acertados:
                estados_faltando.append(estado)
        novo_dado = pandas.DataFrame(estados_faltando)
        novo_dado.to_csv("estados_faltantes.csv")
        break
    if resposta_estado in lista_estados:
        estados_acertados.append(resposta_estado)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        dado_estado = dado[dado.estado == resposta_estado]
        t.goto(int(dado_estado.x), int(dado_estado.y))
        t.write(resposta_estado)

screen.exitonclick()