import tkinter as tk
from tkinter import messagebox
import socket

class PortManagerApp:
    def __init__(self, master):
        self.master = master
        master.title("Port Manager")

        self.label = tk.Label(master, text="Введите номер порта:")
        self.label.pack()

        self.port_entry = tk.Entry(master)
        self.port_entry.pack()

        self.open_button = tk.Button(master, text="Открыть порт", command=self.open_port)
        self.open_button.pack()

        self.close_button = tk.Button(master, text="Закрыть порт", command=self.close_port)
        self.close_button.pack()

    def open_port(self):
        port = self.get_port()
        if port is not None:
            try:
                server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server_socket.bind(("localhost", port))
                server_socket.listen(1)
                server_socket.accept()
                messagebox.showinfo("Успех", f"Порт {port} успешно открыт!")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось открыть порт: {e}")

    def close_port(self):
        port = self.get_port()
        if port is not None:
            try:
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect(("localhost", port))
                client_socket.close()
                messagebox.showinfo("Успех", f"Порт {port} успешно закрыт!")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось закрыть порт: {e}")

    def get_port(self):
        try:
            port = int(self.port_entry.get())
            if 1 <= port <= 65535:
                return port
            else:
                messagebox.showerror("Ошибка", "Номер порта должен быть от 1 до 65535.")
                return None
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректный номер порта.")
            return None

if __name__ == "__main__":
    root = tk.Tk()
    app = PortManagerApp(root)
    root.mainloop()
