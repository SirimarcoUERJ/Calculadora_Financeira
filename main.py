import tkinter as tk

def get_var():
    var = [inital_value, monthly_value, fees, period, final_value]
    var_get = []

    for i in var:
        var_get.append(i.get())

    index, txt = choice(var_get)

    button["text"] = txt
    text["text"] = Do_var(index, var_get)

def choice(arr):
    var = ['Aporte inicial', 'Aporte mensal', 'Taxa de juros', 'Período investido', 'Total investido', 'Todas os campos foram preenchidos', "Somente um campo pode ficar em branco"]
    _ = 0
    index = 5

    for i,j in enumerate(arr):

        if j == '':
            _ += 1
            index = i
        if _ > 1:
            index = 6

    return index, var[index]   

def Do_var(number, arr):

    resp = ''

    if number == 0:
        pass
    
    elif number == 1:
        valor_inicial = float(arr[0])
        aporte = 0
        juros = float(arr[2])
        tempo = int(arr[3])
        Total = float(arr[4])
        FV = valor_inicial

        while FV < Total:
            aporte += 0.01

            for i in range(int(tempo)):
                FV = aporte + FV*(1 + float(juros)/100)

            if FV < Total:
                FV = valor_inicial
        resp = "R$ " + str(round(aporte,2))
    
    elif number == 2:
        pass
    elif number == 3:
        pass
    elif number == 4:
        pass

    return resp

window = tk.Tk()

# tk.messagebox.showinfo(title="Info", message="Preencha os campos para encontrar o aporte mensal \nnescessario para chegar ao valor desejado!")

window.title("Calculadora Juros Compostos.")

inital_value_text = tk.Label(window, text="Aporte inicial")
inital_value_text.grid(column=0, row=0)
inital_value = tk.Entry(window)
inital_value.grid(column=1, row=0)

monthly_value_text = tk.Label(window, text="Aporte mensal")
monthly_value_text.grid(column=0, row=1)
monthly_value = tk.Entry(window)
monthly_value.grid(column=1, row=1)

fees_text = tk.Label(window, text="Taxa de juros")
fees_text.grid(column=0, row=2)
fees = tk.Entry(window)
fees.grid(column=1, row=2)

period_text = tk.Label(window, text="Período investido")
period_text.grid(column=0, row=3)
period = tk.Entry(window)
period.grid(column=1, row=3)

final_value_text = tk.Label(window, text="Total investido")
final_value_text.grid(column=0, row=4)
final_value = tk.Entry(window)
final_value.grid(column=1, row=4)

button = tk.Button(window, text="Start", command=get_var)
button.grid(column=0, row=5)

text = tk.Label(window, text="aguardando comando...")
text.grid(column=1, row=5)

window.mainloop()