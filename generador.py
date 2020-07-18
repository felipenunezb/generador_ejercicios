import tkinter
from tkinter import *
from tkinter import messagebox
from collections import namedtuple
import random
import operator
from tkinter import filedialog as fd

window = tkinter.Tk()
# to rename the title of the window
window.title("Generador de Ejercicios")
# operations frame
ops_frame = tkinter.Frame(window, height=600, width=800)
ops_frame.pack()
#ranges input
range_1 = StringVar(value='0, 100')
range_2 = StringVar(value='0,100')
range_3 = StringVar()
range_4 = StringVar()
range_5 = StringVar()
#operation checkboxes
suma_in = BooleanVar(value=True)
resta_in = BooleanVar()
mult_in = BooleanVar()
div_in = BooleanVar()

#Textboxes
Label(ops_frame, text="Rango 1:").grid(row=0, sticky=W, padx=5)
Label(ops_frame, text="Rango 2:").grid(row=1, sticky=W, padx=5)
Label(ops_frame, text="Rango 3:").grid(row=2, sticky=W, padx=5)
Label(ops_frame, text="Rango 4:").grid(row=3, sticky=W, padx=5)
Label(ops_frame, text="Rango 5:").grid(row=4, sticky=W, padx=5)
Entry(ops_frame, textvariable = range_1).grid(row=0, column=1, padx=5)
Entry(ops_frame, textvariable = range_2).grid(row=1, column=1, padx=5)
Entry(ops_frame, textvariable = range_3).grid(row=2, column=1, padx=5)
Entry(ops_frame, textvariable = range_4).grid(row=3, column=1, padx=5)
Entry(ops_frame, textvariable = range_5).grid(row=4, column=1, padx=5)

#Checkboxes
Checkbutton(ops_frame, text="Suma", variable=suma_in).grid(row=0, column=2, padx=5, sticky=W)
Checkbutton(ops_frame, text="Resta", variable=resta_in).grid(row=1, column=2, padx=5, sticky=W)
Checkbutton(ops_frame, text="Multiplicacion", variable=mult_in).grid(row=2, column=2, padx=5, sticky=W)
Checkbutton(ops_frame, text="Division", variable=div_in).grid(row=3, column=2, padx=5, sticky=W)

#other
Label(window, text="Numero de Ejercicios:").pack()
nej = Entry(window, textvariable = StringVar())
nej.pack()

#get rangos
def get_rangos(rangos_):
    rangos = []
    rango = namedtuple('rango', ['min', 'max'])
    for rgo in rangos_:
        comma_pos = rgo.find(',')
        try: 
            if int(rgo[comma_pos + 1:]) == 0:
                continue
        except:
            continue
        rangos.append(rango._make((int(rgo[:comma_pos]), int(rgo[comma_pos + 1:]))))
    return rangos

def get_operaciones():
    operaciones_lst = ['+', '-', '*', '/']
    operaciones_in = [suma_in.get(), resta_in.get(), mult_in.get(), div_in.get()]
    operaciones = [op for n, op in enumerate(operaciones_lst) if operaciones_in[n]]
    return operaciones

def get_ejercicio(rangos, operaciones):
    random_nums = []
    random_ops = []
    ex_cont = []
    for r in rangos:
        random_nums.append(random.randint(r.min, r.max))
        random_ops.append(random.choice(operaciones))
    
    for n, num in enumerate(random_nums):
        ex_cont.append(str(num))
        if n + 1 < len(random_nums):
            ex_cont.append(random_ops[n])
        ex_str = ' '.join(ex_cont)
    ex_sol = eval(ex_str)

    return ex_str, ex_sol

#HTML
html_head = '''
<html>
<head>
<title>Hoja de ejercicios</title>
</head><body style="border-top:1px solid #000080; margin:0px;"><h1 style="text-align:center; margin-top:12px; font-size:24px; margin-bottom: 11px; color: #000080; font-family: Verdana">Hoja de ejercicios de matem&aacute;ticas</h1>
<div align=center><center>
<table cellpadding="12" cellspacing="0" width="100%" style="">'''

html_break = '''
</table></center></div><div style="border-top:1px solid #000080; page-break-before:always; margin-top:30px; color:#000080">P&aacute;gina 2</div>
<h1 style="margin-top:0px; font-size:24px; font-family:Verdana; text-align:center; color:#000080;">Clave</h1>
<div align="center"><center>
<table width=100% cellspacing="0px" cellpadding="12px">'''

html_foot = '''
</td></tr>
</table>
</center></div><p style="margin-top:12px; font-size:10px;" align=center><b><i>Autorizaci&oacute;n de copias:</i></b> <i>Se permite toda copia.</i> <br>
<b>Copyright Tumorcito / </b> <a href="https://mundorubik.cl/">Ejercicios de Matematicas Gratis</a>
</body></html>'''

def bloque_ejercicio(ex_str, i):
    html_ej = f'''
    <td style="width:50%; text-align:left; ">
    <table cellspacing="0" cellpadding="0" width="100%" style="font-family: Verdana;"><tr>
    <td valign=top nowrap style="width: 48px; color:maroon; font-size:19px"><b>{i+1}.</b></td>
    <td valign=bottom nowrap style="font-family: Verdana; font-size:19px; text-align:left; width:100%">{ex_str} &nbsp;=&nbsp; _______<br>&nbsp;
    <br>&nbsp;
    </td></tr></table>
    </td>'''
    return html_ej

def bloque_solucion(ex_sol, i):
    html_ej = f'''
    <td style="width:50%; text-align:left; ">
    <table cellspacing="0" cellpadding="0" width="100%" style="font-family: Verdana;"><tr>
    <td valign=top nowrap style="width: 48px; color:maroon; font-size:16px"><b>{i+1}.</b></td>
    <td valign=bottom nowrap style="font-family: Verdana; font-size:19px; text-align:left; width:100%">{ex_sol}<br>&nbsp;
    <br>&nbsp;
    </td></tr></table>
    </td>'''
    return html_ej

def file_save(html_txt):
    f = fd.asksaveasfile(mode='w', defaultextension=".html")
    if not f:
        return
    f.write(html_txt)
    f.close()

#boton prueba
def probando():
    n_ej = int(nej.get())
    rangos_ = [range_1.get(), range_2.get(), range_3.get(), range_4.get(), range_5.get()]
    rangos = get_rangos(rangos_)
    soluciones = []
    final_html = html_head   
    for i in range(n_ej):
        if i % 2 == 0:
            final_html += '\n <tr>'
        ex_str, ex_sol = get_ejercicio(rangos, get_operaciones())
        soluciones.append(ex_sol)
        ex_html = bloque_ejercicio(ex_str, i)
        final_html += f"{ex_html} \n"
        if i % 2 == 1:
            final_html += '\n </tr>'
    final_html += html_break
    for i in range(n_ej):
        if i % 2 == 0:
            final_html += '\n <tr>'
        ex_html = bloque_solucion(soluciones[i], i)
        final_html += f"{ex_html} \n"
        if i % 2 == 1:
            final_html += '\n </tr>'
    final_html += html_foot
    file_save(final_html)

def prueba():
    messagebox.showinfo("Title", nej.get())

#b1 = Button(window, text= 'Generar', command=prueba).pack()
b1 = Button(window, text= 'Generar', command=probando)
b1.pack()

window.mainloop()