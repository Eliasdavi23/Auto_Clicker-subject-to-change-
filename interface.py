import customtkinter as ctk
import os
import threading
from main import Auto_Clicker

# JANELA PRINCIPAL
ctk.set_appearance_mode("Dark")  # Ou "Dark" ou "Light"
ctk.set_default_color_theme("blue")

class AutoClickerGUI(ctk.CTk):
    def __init__(self):
        super().__init__()  

        # VARIAVEIS DA JANELA
        self.title("Auto Clicker Genérico")  # TITULO
        self.geometry("600x520")             # TAMANHO (Ajustado levemente para caber tudo folgado)
        self.resizable(False, False)         # BLOQUEAR REDIMENSIONAMENTO

        # CARREGAMENTO SEGURO DE FONTES
        caminho_da_fonte = os.path.join(os.path.dirname(__file__), "fonts", "MinhaFonteCustomizada.ttf")
        
        if os.path.exists(caminho_da_fonte):
            self.fonte_titulo = ("Arial", 12, "bold")
            self.fonte_padrao = ("Arial", 11)
            print("--> Arquivo da fonte encontrado")
        else:
            self.fonte_titulo = ("Arial", 12, "bold")
            self.fonte_padrao = ("Arial", 11)
            print("--> Arquivo de fonte não encontrado. Usando Arial por segurança")

        # ---------------------------------------------------------------------
        # INTERVALO DE CLIQUE
        # ---------------------------------------------------------------------
        self.frame_interval = ctk.CTkFrame(self)
        self.frame_interval.pack(padx=15, pady=10, fill="x")

        # Título da seção adicionado corretamente como Label para não dar erro no Frame
        self.lbl_interval_title = ctk.CTkLabel(self.frame_interval, text="Click interval", font=self.fonte_titulo)
        self.lbl_interval_title.pack(anchor="w", padx=10, pady=5)

        # Sub-frame limpo (sem text ou font) para alinhar horizontalmente os inputs
        self.sub_frame_time = ctk.CTkFrame(self.frame_interval, fg_color="transparent")
        self.sub_frame_time.pack(fill="x", padx=10, pady=5)

        # TIMING (HORA)
        self.entry_hours = ctk.CTkEntry(self.sub_frame_time, width=50)
        self.entry_hours.insert(0, "0")
        self.entry_hours.pack(side="left", padx=2)
        ctk.CTkLabel(self.sub_frame_time, text="hours").pack(side="left", padx=5)

        # TIMING (MINUTOS)
        self.entry_mins = ctk.CTkEntry(self.sub_frame_time, width=50)
        self.entry_mins.insert(0, "0")
        self.entry_mins.pack(side="left", padx=2)
        ctk.CTkLabel(self.sub_frame_time, text="mins").pack(side="left", padx=5)

        # TIMING (SEGUNDOS)
        self.entry_secs = ctk.CTkEntry(self.sub_frame_time, width=50)
        self.entry_secs.insert(0, "0")
        self.entry_secs.pack(side="left", padx=2)
        ctk.CTkLabel(self.sub_frame_time, text="secs").pack(side="left", padx=5)

        # TIMING (MILISEGUNDOS)
        self.entry_ms = ctk.CTkEntry(self.sub_frame_time, width=50)
        self.entry_ms.insert(0, "100")
        self.entry_ms.pack(side="left", padx=2)
        ctk.CTkLabel(self.sub_frame_time, text="milliseconds").pack(side="left", padx=5)

        # ---------------------------------------------------------------------
        # SEÇÃO DO MEIO: OPTIONS E REPEAT (LADO A LADO)
        # ---------------------------------------------------------------------
        self.grid_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.grid_frame.pack(padx=15, pady=5, fill="x")

        # OPÇÕES (Coluna Esquerda)
        # Corrigido de gride_frame para grid_frame
        self.frame_options = ctk.CTkFrame(self.grid_frame)
        self.frame_options.pack(side="left", fill="both", expand=True, padx=(0, 5))

        ctk.CTkLabel(self.frame_options, text="Click options", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=2)

        # Clique Mouse - Corrigido de CTkLavel para CTkLabel
        self.lbl_mouse = ctk.CTkLabel(self.frame_options, text="Mouse button:")
        self.lbl_mouse.pack(anchor="w", padx=10)
        self.menu_mouse = ctk.CTkOptionMenu(self.frame_options, values=["Left", "Right", "Middle"])
        self.menu_mouse.pack(fill="x", padx=10, pady=5)

        # REPETIÇÃO (Coluna Direita)
        self.frame_repeat = ctk.CTkFrame(self.grid_frame)
        self.frame_repeat.pack(side="right", fill="both", expand=True, padx=(5, 0))

        ctk.CTkLabel(self.frame_repeat, text="Click repeat", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=2)

        self.repeat_var = ctk.StringVar(value="infinite")
        
        self.rad_repeat_times = ctk.CTkRadioButton(self.frame_repeat, text="Repeat", variable=self.repeat_var, value="times")
        self.rad_repeat_times.pack(anchor="w", padx=10, pady=5)
        
        self.entry_repeat_times = ctk.CTkEntry(self.frame_repeat, width=60)
        self.entry_repeat_times.insert(0, "1")
        self.entry_repeat_times.pack(anchor="w", padx=30, pady=2)
        
        self.rad_repeat_inf = ctk.CTkRadioButton(self.frame_repeat, text="Repeat until stopped", variable=self.repeat_var, value="infinite")
        self.rad_repeat_inf.pack(anchor="w", padx=10, pady=10)

        # ---------------------------------------------------------------------
        # POSIÇÃO DO CURSOR
        # ---------------------------------------------------------------------
        self.frame_cursor = ctk.CTkFrame(self)
        self.frame_cursor.pack(padx=15, pady=10, fill="x")
        
        ctk.CTkLabel(self.frame_cursor, text="Cursor position", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=2)
        
        self.cursor_var = ctk.StringVar(value="current")
        
        self.rad_curr_loc = ctk.CTkRadioButton(self.frame_cursor, text="Current location", variable=self.cursor_var, value="current")
        self.rad_curr_loc.pack(anchor="w", padx=10, pady=5)
        
        # Sub-frame para simular a seleção de coordenadas fixas
        self.sub_frame_coord = ctk.CTkFrame(self.frame_cursor, fg_color="transparent")
        self.sub_frame_coord.pack(fill="x", padx=10, pady=5)
        
        self.rad_pick_loc = ctk.CTkRadioButton(self.sub_frame_coord, text="Pick location", variable=self.cursor_var, value="pick")
        self.rad_pick_loc.pack(side="left")
        
        ctk.CTkLabel(self.sub_frame_coord, text="X").pack(side="left", padx=(20, 2))
        self.entry_x = ctk.CTkEntry(self.sub_frame_coord, width=50, placeholder_text="0")
        self.entry_x.pack(side="left")
        
        ctk.CTkLabel(self.sub_frame_coord, text="Y").pack(side="left", padx=(10, 2))
        self.entry_y = ctk.CTkEntry(self.sub_frame_coord, width=50, placeholder_text="0")
        self.entry_y.pack(side="left")

        # ---------------------------------------------------------------------
        # BOTÕES DE EXECUÇÃO (START / STOP)
        # ---------------------------------------------------------------------
        self.frame_actions = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_actions.pack(padx=15, pady=15, fill="x")

        self.btn_start = ctk.CTkButton(self.frame_actions, text="Start (F6)", fg_color="green", hover_color="darkgreen", command=self.acao_start)
        self.btn_start.pack(side="left", fill="x", expand=True, padx=(0, 5), ipady=10)

        self.btn_stop = ctk.CTkButton(self.frame_actions, text="Stop (F6)", fg_color="red", hover_color="darkred", command=self.acao_stop, state="disabled")
        self.btn_stop.pack(side="right", fill="x", expand=True, padx=(5, 0), ipady=10)

    # CONTROLE PROVISORIO
    def acao_start(self):
        texto_milissegundos = self.entry_ms.get()
        milissegundos = float(texto_milissegundos)
        segundos = milissegundos / 1000

        self.clicker = Auto_Clicker(segundos)
        print(f"--> Iniciando cliques com intervalo em {segundos}")
        
        self.btn_start.configure(state="disabled")
        self.btn_stop.configure(state="normal")

        threading.Thread(target=self.clicker.start_clicking, daemon=True).start()
        

    def acao_stop(self):
        print("--> Parando cliques...")

        if hasattr(self, 'clicker'):
            self.clicker.stop_clicking()
            
        self.btn_start.configure(state="normal")
        self.btn_stop.configure(state="disabled")

if __name__ == "__main__":
    app = AutoClickerGUI()
    app.mainloop()