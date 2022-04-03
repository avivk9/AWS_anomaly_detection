from pandas import DataFrame
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


from boto3_instance_utilization import list_time_first5 as list_time
from boto3_instance_utilization import list_utilization as list_util
from boto3_instance_utilization import getUtilizations, getTimes
from utils.functions import stringsToFloats as Stf


def vp_start_gui():
    global root
    root = tk.Tk()
    """ INSERT YOUR WHOLE CODE HERE"""
    data_cpu = {'Time': getTimes(),
                'CPU utilization': getUtilizations()
                }
    df_cpu = DataFrame(data_cpu, columns=['Time', 'CPU utilization'])

    figure_cpu = plt.Figure(figsize=(5, 4), dpi=100)
    ax_cpu = figure_cpu.add_subplot(111)
    line_cpu = FigureCanvasTkAgg(figure_cpu, root)
    line_cpu.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df_cpu = df_cpu[['Time', 'CPU utilization']].groupby('Time').sum()
    df_cpu.plot(kind='line', legend=True, ax=ax_cpu, color='b', marker='o', fontsize=10)
    ax_cpu.set_title('CPU utilization over time')

    btn = tk.Button(root, text='Click me !', bd='5',
                    command=refresh)

    btn.pack(side='top')
    """ CREATE A BUTTON AND ITS command = refresh() which is defined at the bottom"""
    root.mainloop()


if __name__ == '__main__':
    def refresh():
        root.destroy()
        vp_start_gui()
    vp_start_gui()

