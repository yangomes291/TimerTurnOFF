import customtkinter as ctk  # importando a biblioteca
from datetime import datetime, timedelta

app = ctk.CTk()
app.title("TimerTurnOFF")
app.geometry("400x300+390+240")
app.resizable(width=False, height=False)
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"

desligamento = 'shutdown -s -f -t'
cancelar = 'shutdown -a'
horario_atual = datetime.now()


def button_click_event():
    input_dialog = ctk.CTkInputDialog(text="Desligar em quantos minutos: "
                                           "\n(Digite 0 para cancelar um agendamento já definido)", title="Timer",
                                      font=("Rosales", 15))
    input_dialog.geometry("410x200+387+300")
    quantos = (int(input_dialog.get_input()))  # Recebe a entrada e converte para inteiro
    cmd = desligamento + ' ' + str(quantos * 60)  # Multiplica os minutos por 60 para obter segundos

    if quantos > 0:
        desligar(cmd)
        novo_horario_local = datetime.now() + timedelta(minutes=quantos)
        horario_definido(novo_horario_local)
        return quantos, cmd

    elif quantos == 0:
        candesl()


info_box1 = None


def horario_definido(novo_horario):
    global info_box1  # Referência global para a variável
    if info_box1:  # Se já existe, destrói antes de criar o novo
        info_box1.destroy()

    info_box1 = ctk.CTkLabel(app, width=300, height=10, corner_radius=10,
                             text="\nDesligamento agendado para {}".format(novo_horario.strftime("%H:%M")),
                             font=("Rosales", 15))
    info_box1.grid(padx=0, pady=0)
    info_box1.place(x=50, y=220)


def remover_horario():
    global info_box1  # Referência global para a variável
    if info_box1:  # Se já existe, destrói antes de criar o novo
        info_box1.destroy()

    info_box1 = ctk.CTkLabel(app, width=300, height=10, corner_radius=10,
                             text="Desligamento automático removido", text_color="Red", font=("Rosales", 15))
    info_box1.grid(padx=0, pady=0)
    info_box1.place(x=50, y=240)


def desligar(cmd):
    import os
    os.system(cmd)


def candesl():
    import os
    remover_horario()
    os.system(cancelar)


button = ctk.CTkButton(app, width=300, height=50, text="Definir desligamento automático", font=("Rosales", 20),
                       command=button_click_event)
button.grid(padx=0, pady=0)
button.place(x=55, y=60)
button2 = ctk.CTkButton(app, width=180, height=50, text="Remover desligamento automático", font=("Rosales", 20),
                        command=candesl)
button2.grid(padx=0, pady=0)
button2.place(x=50, y=150)

app.mainloop()
