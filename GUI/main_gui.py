from pandas import DataFrame
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from boto3_instance_utilization import update_time, update_cpu


def vp_start_gui():
    global root
    root = tk.Tk()
    list_time = update_time()
    list_cpu = update_cpu()
    data_cpu = {'Time': list_time,
                'CPU utilization': list_cpu
                }
    df_cpu = DataFrame(data_cpu, columns=['Time', 'CPU utilization'])

    figure_cpu = plt.Figure(figsize=(5, 4), dpi=100)
    ax_cpu = figure_cpu.add_subplot(111)
    line_cpu = FigureCanvasTkAgg(figure_cpu, root)
    line_cpu.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df_cpu = df_cpu[['Time', 'CPU utilization']].groupby('Time').sum()
    df_cpu.plot(kind='line', legend=True, ax=ax_cpu, color='b', marker='o', fontsize=10)
    ax_cpu.set_title('CPU utilization over time')

    status = "Nothing Yet" # get from detect using list_cpu, list_time
    myLabel = tk.Label(root, text=status)

    btn = tk.Button(root, text='REFRESH', bd='2',
                    command=refresh)
    myLabel.pack(side='top')
    btn.pack(side='top')
    """ CREATE A BUTTON AND ITS command = refresh() which is defined at the bottom"""
    root.mainloop()


def refresh():
    root.destroy()
    vp_start_gui()


def main():
    vp_start_gui()


if __name__ == '__main__':
    main()