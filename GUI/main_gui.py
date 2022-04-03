from pandas import DataFrame
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


from boto3_instance_utilization import list_time_first5 as list_time
from boto3_instance_utilization import list_utilization
from utils.functions import stringsToFloats as Stf

list_utilization = Stf(list_utilization)

data_cpu = {'Time': list_time,
         'CPU utilization': list_utilization
         }
df_cpu = DataFrame(data_cpu, columns=['Time', 'CPU utilization'])

root = tk.Tk()

figure_cpu = plt.Figure(figsize=(5, 4), dpi=100)
ax_cpu = figure_cpu.add_subplot(111)
line_cpu = FigureCanvasTkAgg(figure_cpu, root)
line_cpu.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df_cpu = df_cpu[['Time', 'CPU utilization']].groupby('Time').sum()
df_cpu.plot(kind='line', legend=True, ax=ax_cpu, color='b', marker='o', fontsize=10)
ax_cpu.set_title('CPU utilization over time')

root.mainloop()