import tkinter as tk
import system_info
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure



class Piechart():
    def __init__(self,parent,title,labels,values):

        self.fig=Figure(figsize=(3,2),dpi=100) #creates figure
        self.area=self.fig.add_subplot(111)  #creates the actual ploting area inside the figure

        self.area.pie(values,labels=labels,autopct="%1.1f%%") #creates the piecart 

        self.area.set_title(title) #sets the tittle for the subplot i.e inside the figure object

        self.canvas=FigureCanvasTkAgg(self.fig,master=parent) #connects the figure object with tkinter frame/window (parent)

        self.canvas.draw()# render the figure onto the tinkter canvas

        self.widgets=self.canvas.get_tk_widget() #retrieves the actual tkinter widgets associated with the canvas and stores it in a instance variable 






root=tk.Tk()
root.geometry("1000x1000")
root.title("OverWatch V1")
root.config(bg="light grey")
tk.Label(root,text="OverWatch",bg="black",fg="white",font=("Orbitron Code", 24),relief=tk.RAISED).pack(padx=10,pady=10)


btn_frame=tk.Frame(root,padx=10,pady=10)
btn_frame.pack(pady=25)
btn_frame.config(bg="lightgrey")

def btn_os_fn():
    os_frame=tk.Frame(root,bg="light grey")
    os_frame.pack(padx=20,pady=10,fill="both",expand=True) 
    btn_frame.pack_forget()
    label_frame=tk.Frame(os_frame,bg="lightgrey")
    label_frame.pack(padx=10,pady=10)
    tk.Label(label_frame,text=system_info.os(),bg="grey",fg="white",font=("Orbitron Code", 20),relief=tk.RAISED).grid(row=0,column=0,padx=10)
    tk.Label(label_frame,text=f"Run time: {system_info.run_time()}",bg="grey",fg="white",font=("Orbitron Code", 20),relief=tk.RAISED).grid(row=0,column=1,padx=10)
    

    def go_back():
        os_frame.pack_forget()
        btn_frame.pack()

    tk.Button(os_frame,text="go back",bg="grey",fg="white",font=("Orbitron Code", 20),command=go_back,relief=tk.RAISED).pack(padx=10,pady=30)





def btn_cpu_fn():
    cpu_frame=tk.Frame(root,bg="light grey")
    cpu_frame.pack(padx=20,pady=10,fill="both",expand=True)  
    btn_frame.pack_forget()
    label_frame=tk.Frame(cpu_frame,bg="lightgrey")
    label_frame.pack(padx=10,pady=10)


    tk.Label(label_frame,text=f"processor: {system_info.processor_name()}",bg="grey",fg="white",font=("Orbitron Code", 20),relief=tk.RAISED).grid(row=0,column=0)
    tk.Label(label_frame,text=f"physical cores: {system_info.cpu_physical_cores()}",bg="grey",fg="white",font=("Orbitron Code", 20),relief=tk.RAISED).grid(row=1,column=0)
    tk.Label(label_frame,text=f"logical cores: {system_info.cpu_logical_cores()}",bg="grey",fg="white",font=("Orbitron Code", 20),relief=tk.RAISED).grid(row=2,column=0)
    tk.Label(label_frame,text=f"max frequency: {system_info.cpu_freq_max()}",bg="grey",fg="white",font=("Orbitron Code", 20),relief=tk.RAISED).grid(row=3,column=0)
    tk.Label(label_frame,text=f"min frequency: {system_info.cpu_freq_min()}",bg="grey",fg="white",font=("Orbitron Code", 20),relief=tk.RAISED).grid(row=4,column=0)
    
    
    
    def curent_frequency():
         tk.Label(label_frame,text=f"curent frequency: {system_info.cpu_freq_current()}",bg="grey",fg="white",font=("Orbitron Code", 20),relief=tk.RAISED).grid(row=5,column=0)
         label_frame.after(500,curent_frequency)
    
    def cpu_use_percent():
        cpu_usage=float(system_info.cpu_usage())
        usage_pie=Piechart(label_frame,"cpu usage",("","usage"),(100-cpu_usage,cpu_usage))
        usage_pie.widgets.grid(row=1,column=1,rowspan=5,padx=20,pady=20)
        label_frame.after(400,cpu_use_percent)
    curent_frequency()
    cpu_use_percent()    



    def go_back():
            cpu_frame.pack_forget()
            btn_frame.pack()
            
    go_back_btn=tk.Button(cpu_frame,text="go back",bg="grey",fg="white",font=("Orbitron Code", 20),command=go_back,relief=tk.RAISED)
    go_back_btn.pack(padx=30,pady=30)


   
    
    ...



def btn_ram_fn():

    ram_frame=tk.Frame(root,bg="light grey")
    ram_frame.pack(padx=20,pady=10,fill="both",expand=True)  
    btn_frame.pack_forget()
    label_frame=tk.Frame(ram_frame,bg="lightgrey")
    label_frame.pack(padx=10,pady=10)     

    def ram_usage():
         ram_util=float(system_info.ram_usage())
         ram_pie=Piechart(label_frame,"RAM utilisation",("usage",""),(ram_util,100-ram_util))
         ram_pie.widgets.grid(row=0,column=0)
         label_frame.after(500,ram_usage)

    ram_usage() 
    tk.Label(label_frame,text=f"Total Ram : {system_info.total_ram()}",bg="grey",fg="white",font=("Orbitron Code", 20),relief=tk.RAISED).grid(row=1,column=0,padx=20,pady=20)
    
    
    
    def go_back():
                ram_frame.pack_forget()
                btn_frame.pack()
                
    go_back_btn=tk.Button(ram_frame,text="go back",bg="grey",fg="white",font=("Orbitron Code", 20),command=go_back,relief=tk.RAISED)
    go_back_btn.pack(padx=30,pady=30)
    
    ...

def btn_memory_fn():
     
    memory_frame=tk.Frame(root,bg="light grey")
    memory_frame.pack(padx=20,pady=10,fill="both",expand=True)  
    btn_frame.pack_forget()
    label_frame=tk.Frame(memory_frame,bg="lightgrey")
    label_frame.pack(padx=10,pady=10)      



    def disk_util():
         disk_usage=float(system_info.used_disk_percent())
         disk_pie=Piechart(label_frame,"Disk Utilisation",("","usage"),(100-disk_usage,disk_usage))
         disk_pie.widgets.grid(row=0,column=0)     
         label_frame.after(500,disk_util)
    
    disk_util()

    tk.Label(label_frame,text=f"Total Disk Space : {system_info.total_disk()}",bg="grey",fg="white",font=("Orbitron Code", 20),relief=tk.RAISED).grid(row=1,column=0,padx=20,pady=20)
    
    def go_back():
            memory_frame.pack_forget()
            btn_frame.pack()
                
    go_back_btn=tk.Button(memory_frame,text="go back",bg="grey",fg="white",font=("Orbitron Code", 20),command=go_back,relief=tk.RAISED)
    go_back_btn.pack(padx=30,pady=30)
    ...



def btn_gpu_fn():
    gpu_frame=tk.Frame(root,bg="light grey")
    gpu_frame.pack(padx=20,pady=10,fill="both",expand=True)  
    btn_frame.pack_forget()
    label_frame=tk.Frame(gpu_frame,bg="lightgrey")
    label_frame.pack(padx=10,pady=10)     

 

    tk.Label(label_frame,text=f"GPU Commercial Name : {system_info.gpu_model()}",bg="grey",fg="white",font=("Orbitron Code", 20),relief=tk.RAISED).grid(row=0,column=0,padx=20,pady=20)
    
    def vram_util():
         vram_usage=system_info.gpu_vram_usage()
         vram_pie=Piechart(label_frame,"Vram Utilization",("","usage"),(100-vram_usage,vram_usage))
         vram_pie.widgets.grid(row=1,column=0,padx=20,pady=20)    
         label_frame.after(500,vram_util)

    vram_util()

    tk.Label(label_frame,text=f"Total Vram : {system_info.gpu_vram_tot()}",bg="grey",fg="white",font=("Orbitron Code", 20),relief=tk.RAISED).grid(row=2,column=0,padx=20,pady=20)

    def go_back():
            gpu_frame.pack_forget()
            btn_frame.pack()
                
    go_back_btn=tk.Button(gpu_frame,text="go back",bg="grey",fg="white",font=("Orbitron Code", 20),command=go_back,relief=tk.RAISED)
    go_back_btn.pack(padx=30,pady=30)




btn_os=tk.Button(btn_frame,text=" OS ",bg="grey",fg="white",font=("Orbitron Code", 20),command=btn_os_fn,relief=tk.RAISED).grid(row=0,column=0)

btn_cpu=tk.Button(btn_frame,text="CPU",bg="grey",fg="white",font=("Orbitron Code", 20),command=btn_cpu_fn,relief=tk.RAISED).grid(row=1,column=0)


btn_ram=tk.Button(btn_frame,text="RAM",bg="grey",fg="white",font=("Orbitron Code", 20),command=btn_ram_fn,relief=tk.RAISED).grid(row=2,column=0)

btn_memory=tk.Button(btn_frame,text="Memory",bg="grey",fg="white",font=("Orbitron Code", 17),command=btn_memory_fn,relief=tk.RAISED).grid(row=3,column=0)


btn_gpu=tk.Button(btn_frame,text="GPU",bg="grey",fg="white",font=("Orbitron Code", 20),command=btn_gpu_fn,relief=tk.RAISED).grid(row=4,column=0)



btn_exit=tk.Button(root,text="EXIT",bg="grey",fg="white",font=("Orbitron Code", 20),command=root.destroy,relief=tk.RAISED).pack(side="bottom",padx=10,pady=20)











tk.mainloop()

