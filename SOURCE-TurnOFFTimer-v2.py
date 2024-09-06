import customtkinter as ctk
from PIL import Image
from datetime import datetime, timedelta
from subprocess import run

app = ctk.CTk()
app.title("TurnOFFTimer")
app.iconbitmap("/Users/Yan/Desktop/ABC/img-remove.ico")
app.geometry("300x190+450+280")
app.resizable(width=False, height=False)
ctk.set_appearance_mode("System")

imageneutral = ctk.CTkImage(Image.open("/Users/Yan/Desktop/ABC/data/img-defined.png"), size=(60, 60))
imageneutralpos = ctk.CTkLabel(app, image=imageneutral, text="")
imageneutralpos.place(x=232, y=121)
imageneutralpos.lift()
import subprocess

desligamento = 'shutdown -s -f -t'
cancelar = 'shutdown -a'

oinputdonumero = ctk.CTkEntry(app, width=200, height=100, font=("Rosales", 35))
oinputdonumero.insert(0, 0)
oinputdonumero.configure(justify='center')
oinputdonumero.grid(padx=0, pady=0)
oinputdonumero.place(x=25, y=29)

def obter_texto():
    texto = oinputdonumero.get().replace(" ", "")
    return int(texto)

def add_30min():
    texto_atual = obter_texto()
    novo_texto = texto_atual + 30
    oinputdonumero.delete(0, ctk.END)
    oinputdonumero.insert(0, str(novo_texto))

def add_60min():
    texto_atual = obter_texto()
    novo_texto = texto_atual + 60
    oinputdonumero.delete(0, ctk.END)
    oinputdonumero.insert(0, str(novo_texto))

def add_120min():
    texto_atual = obter_texto()
    novo_texto = texto_atual + 120
    oinputdonumero.delete(0, ctk.END)
    oinputdonumero.insert(0, str(novo_texto))

def add_reset():
    oinputdonumero.delete(0, ctk.END)
    oinputdonumero.insert(0, "0")

def button_click_event():
    texto = obter_texto()
    if texto is not None:
        quantos = int(texto)
        cmd = desligamento + ' ' + str(quantos * 60)
        if quantos > 0:
            desligar(cmd)
            novo_horario_local = datetime.now() + timedelta(minutes=quantos)
            horario_definido(novo_horario_local)
        else:
            remover_horario2()

def button_click_event2():
    texto = obter_texto()
    if texto is not None:
        quantos = int(texto)
        if quantos == 0:
            remover_horario2()
        else:
            candesl()
            remover_horario()

info_box1 = None

def horario_definido(novo_horario):
    global info_box1
    if info_box1:
        info_box1.destroy()
    info_box1 = ctk.CTkLabel(app, width=180, height=2, corner_radius=2,
                             text="\nDesligamento agendado para {}".format(novo_horario.strftime("%H:%M")),
                             font=("Rosales", 13))
    info_box1.grid(padx=0, pady=0)
    info_box1.place(x=25, y=154)
    info_box1.lower()

def remover_horario():
    global info_box1
    if info_box1:
        info_box1.destroy()
    info_box1 = ctk.CTkLabel(app, width=180, height=10, corner_radius=0,
                             text="Desligamento cancelado", text_color="Red", font=("Rosales", 13))
    info_box1.grid(padx=0, pady=0)
    info_box1.place(x=28, y=171)
    add_reset()

def remover_horario2():
    global info_box1
    if info_box1:
        info_box1.destroy()
    info_box1 = ctk.CTkLabel(app, width=200, height=3, corner_radius=10,
                             text="Nenhum desligamento definido", text_color="Red", font=("Rosales", 13))
    info_box1.grid(padx=0, pady=0)
    info_box1.place(x=25, y=171)
    candesl()

def desligar(cmd):
    run(cmd, creationflags=subprocess.DETACHED_PROCESS)

def candesl():
    run(cancelar, creationflags=subprocess.DETACHED_PROCESS)

button = ctk.CTkButton(app, width=96, height=30, text="Definir", font=("Rosales", 12, "bold"),
                       command=button_click_event)
button.grid(padx=0, pady=0)
button.place(x=129, y=136)

button2 = ctk.CTkButton(app, width=100, height=30, text="Cancelar", font=("Rosales", 12, "bold"),
                        command=button_click_event2)
button2.grid(padx=0, pady=0)
button2.place(x=26, y=136)

button30min = ctk.CTkButton(app, width=60, height=20, text="+30min", font=("Rosales", 12, "bold"), command=add_30min)
button30min.grid(padx=0, pady=0)
button30min.place(x=231, y=29)

button60min = ctk.CTkButton(app, width=60, height=20, text="+1h", font=("Rosales", 12, "bold"), command=add_60min)
button60min.grid(padx=0, pady=0)
button60min.place(x=231, y=55)

button120min = ctk.CTkButton(app, width=60, height=20, text="+2h", font=("Rosales", 12, "bold"), command=add_120min)
button120min.grid(padx=0, pady=0)
button120min.place(x=231, y=81)

buttonRESETmin = ctk.CTkButton(app, width=60, height=20, text="RESET", font=("Rosales", 11, "bold"), command=add_reset)
buttonRESETmin.grid(padx=0, pady=0)
buttonRESETmin.place(x=231, y=109)

inforboxinforma = ctk.CTkLabel(app, width=300, height=10, corner_radius=10, text="Desligar em quantos minutos: ",
                               font=("Rosales", 15))
inforboxinforma.lift()
inforboxinforma.grid(padx=0, pady=0)
inforboxinforma.place(x=-24, y=5)

app.mainloop()
