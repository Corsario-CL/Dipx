import tkinter as tk
from tkinter import messagebox, filedialog
import scapy.all as scapy
import ipaddress
from prettytable import PrettyTable

class NetworkScannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Escáner de Red Profesional")
        self.root.geometry("800x500")
        self.root.configure(bg="#2c3e50")
        
        # Menú
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        # Menú "Archivo"
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)
        self.file_menu.add_command(label="Guardar Resultados", command=self.save_results)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=root.quit)

        # Menú "Opciones"
        self.options_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Opciones", menu=self.options_menu)
        self.options_menu.add_command(label="Configuración de Escaneo", command=self.scan_options)
        self.options_menu.add_command(label="Guardar Configuración", command=self.save_config)

        # Estilo de los widgets
        label_style = {"bg": "#2c3e50", "fg": "#ecf0f1", "font": ("Arial", 14, "bold")}
        entry_style = {"bg": "#34495e", "fg": "#ecf0f1", "font": ("Arial", 12), "insertbackground": "#ecf0f1"}
        button_style = {"bg": "#e74c3c", "fg": "#ecf0f1", "font": ("Arial", 12, "bold"), "relief": "flat"}

        # Etiqueta de entrada de IP
        self.ip_entry_label = tk.Label(root, text="Ingresa el rango de IP o la IP específica:", **label_style)
        self.ip_entry_label.pack(pady=10)

        # Entrada de IP
        self.ip_entry = tk.Entry(root, width=50, **entry_style)
        self.ip_entry.pack(pady=10)

        # Botón de escaneo
        self.scan_button = tk.Button(root, text="Escanear", command=self.scan_network, **button_style)
        self.scan_button.pack(pady=10)

        # Botón de guardar resultados
        self.save_button = tk.Button(root, text="Guardar Resultados", command=self.save_results, state=tk.DISABLED, **button_style)
        self.save_button.pack(pady=10)

        # Área de texto para mostrar resultados
        self.results_text = tk.Text(root, height=15, width=90, bg="#34495e", fg="#ecf0f1", font=("Arial", 12), relief="flat")
        self.results_text.pack(pady=20)

        # Almacena los resultados del escaneo
        self.scan_results = []

    def validate_ip(self, ip):
        try:
            ipaddress.ip_network(ip, strict=False)
            return True
        except ValueError:
            return False

    def scan_network(self):
        ip = self.ip_entry.get().
        ip = self.ip_entry.get().strip()
        if not self.validate_ip(ip):
            messagebox.showerror("Error", f"'{ip}' no es una IP o rango válido.")
            return

        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, f"Escaneando {ip}...\n\n")

        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        respuestas = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
        
        self.scan_results = []
        tabla = PrettyTable(["IP", "MAC Address"])
        for respuesta in respuestas:
            dispositivo = {"ip": respuesta[1].psrc, "mac": respuesta[1].hwsrc}
            self.scan_results.append(dispositivo)
            tabla.add_row([dispositivo["ip"], dispositivo["mac"]])

        self.results_text.insert(tk.END, tabla)
        self.save_button.config(state=tk.NORMAL)

    def save_results(self):
        if not self.scan_results:
            messagebox.showwarning("Advertencia", "No hay resultados para guardar.")
            return

        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if filename:
            try:
                with open(filename, "w") as file:
                    for dispositivo in self.scan_results:
                        file.write(f"IP: {dispositivo['ip']}, MAC: {dispositivo['mac']}\n")
                messagebox.showinfo("Guardado", f"Resultados guardados en '{filename}'")
            except IOError as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")

    def scan_options(self):
        messagebox.showinfo("Opciones de Escaneo", "Aquí puedes configurar opciones de escaneo adicionales.")

    def save_config(self):
        filename = filedialog.asksaveasfilename(defaultextension=".cfg", filetypes=[("Config files", "*.cfg")])
        if filename:
            try:
                with open(filename, "w") as file:
                    file.write("Configuración de escaneo guardada aquí.")
                messagebox.showinfo("Configuración Guardada", f"Configuración guardada en '{filename}'")
            except IOError as e:
                messagebox.showerror("Error", f"No se pudo guardar la configuración: {e}")

def main():
    root = tk.Tk()
    app = NetworkScannerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
