import tkinter as tk
from pathlib import Path
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt

class MathPloter(tk.Tk):
    def __init__(self):
        
        # Recursos
        icon = Path(__file__).parent / "calculator.ico"
        
        # Inicialização da instancia de tk.Tk
        super().__init__()
        
        # Configurações da janela
        self.geometry("600x400") # Definindo tamanho da janela
        self.resizable(False, False)
        self.title("MathPloter") # Definindo título da janela
        self.iconbitmap(icon) # Definindo ícone da janela

        # Configuração do Grid Layout
        self.columnconfigure((0,1,2,3), weight=1, uniform=True)
        self.rowconfigure((0,1,2,3), weight=1, uniform=True)
    
    def run(self):
        """
        Método que exibirá o App
        """
        self.widgets()
        self.layout()
        self.mainloop()

    def widgets(self): 
        """
        Método para definição dos Widgets usados na interface
        """

        # --- Título principal da janela ---

        # Frame 
        self.title_frame = ttk.Frame(self, relief="groove", borderwidth=5)

        # Label de Título
        ttk.Label(self.title_frame, text="Visualizador de Lissajous", font=("Cubics",20)).pack(expand=True)

        # --- Título principal da janela ---

        
        # --- Configurações da onda 1 ---

        # Frame
        self.w1_frame = ttk.Frame(self, relief="groove", borderwidth=5) 
        
        # Slider da Amplitude da Onda 1
        self.Ax = tk.DoubleVar(value=0.1)
        self.w1_amp_label = ttk.Label(self.w1_frame, text=f"Amplitude em X: {self.Ax.get()} V")
        self.w1_amplitude = ttk.Scale(
            self.w1_frame, 
            from_=0.1,
            to=10.0,
            variable=self.Ax,
            command=lambda e: self.w1_amp_label.configure(
                text=f"Amplitude em X: {self.Ax.get():.2f} V"
            )
        )
        
        # Slider da Frequência da Onda 1
        self.Fx = tk.IntVar(value=1)
        self.w1_freq_label = ttk.Label(self.w1_frame, text=f"Frequência em X: {self.Fx.get()} Hz")
        self.w1_frequencia = ttk.Scale(
            self.w1_frame, 
            from_=1,
            to=10,
            variable=self.Fx,
            command=lambda e: self.w1_freq_label.configure(
                text=f"Frequência em X: {self.Fx.get()} Hz"
            )
        )
        
        # --- Configurações da onda 1 ---
        
        
        # --- Configurações da onda 2 ---

        # Frame
        self.w2_frame = ttk.Frame(self, relief="groove", borderwidth=5) 
        
        # Slider de Amplitude da Onda 2
        self.Ay = tk.DoubleVar(value=0.1)
        self.w2_amp_label = ttk.Label(self.w2_frame, text=f"Amplitude em Y: {self.Ay.get()} V")
        self.w2_amplitude = ttk.Scale(
            self.w2_frame, 
            from_=0.1,
            to=10.0,
            variable=self.Ay,
            command=lambda e: self.w2_amp_label.configure(
                text=f"Amplitude em Y: {self.Ay.get():.2f} V"
            )
        )

        # Slider de Frequência da Onda 2
        self.Fy = tk.IntVar(value=1)
        self.w2_freq_label = ttk.Label(self.w2_frame, text=f"Frequência em Y: {self.Fy.get()} Hz")
        self.w2_frequencia = ttk.Scale(
            self.w2_frame, 
            from_=1,
            to=10,
            variable=self.Fy,
            command=lambda e: self.w2_freq_label.configure(
                text=f"Frequência em Y: {self.Fy.get()} Hz"
            )
        )

        # --- Configurações da onda 2 ---

        
        # --- Configurações da figura ---

        # Frame
        self.plot_conf = ttk.Frame(self, relief="groove", borderwidth=5)

        # Number Input da Amostragem
        self.amt = tk.IntVar(value=10)
        self.amt_label = ttk.Label(self.plot_conf, text="Taxa de amostragem")
        self.amostragem = ttk.Spinbox(self.plot_conf, textvariable=self.amt, from_=10, to=1000000, increment=10)

        # --- Configurações da figura ---


        # --- Geração do gráfico ---

        # Frame
        self.plot_frame = ttk.Frame(self, relief="groove", borderwidth=5)
        self.plot_button = ttk.Button(self.plot_frame, text="GERAR", command=self.lissajous)

        # --- Geração do gráfico ---
    
    def layout(self):
        self.title_frame.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)
        self.w1_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10)
        self.w2_frame.grid(row=1, column=2, columnspan=2, sticky="nsew", padx=10)
        self.plot_conf.grid(row=2, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)
        self.plot_frame.grid(row=3, column=0, columnspan=4, rowspan=2, sticky="nsew", padx=10, pady=10)

        self.w1_amp_label.pack()
        self.w1_amplitude.pack(fill="x", padx=50)

        self.w1_freq_label.pack()
        self.w1_frequencia.pack(fill="x", padx=50)

        self.w2_amp_label.pack()
        self.w2_amplitude.pack(fill="x", padx=50)

        self.w2_freq_label.pack()
        self.w2_frequencia.pack(fill="x", padx=50)
        
        self.amt_label.pack(expand=True)
        self.amostragem.pack(expand=True)

        self.plot_button.pack(expand=True, ipadx=20, ipady=5)
        
    def lissajous(self):
        t = np.linspace(-2*np.pi, 2*np.pi, self.amt.get())
        defasagem = 1.28
        X = self.Ax.get() * np.sin(
            self.Fx.get() * t + defasagem
        )
        Y = self.Ay.get()  * np.sin(
            self.Fy.get() * t
        )
        
        fig, ax = plt.subplots()
        ax.plot(X,Y)
        ax.set_aspect('equal')
        ax.grid(True)
        fig.show()
        

if __name__ == "__main__":
    app = MathPloter()
    app.run()