import socket
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class PortScanner(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=10, spacing=10, **kwargs)

        # Target IP input
        self.add_widget(Label(text="Enter Target IP or Host:", size_hint=(1, 0.1)))
        self.target_input = TextInput(multiline=False)
        self.add_widget(self.target_input)

        # Port range input
        self.add_widget(Label(text="Enter Port Range (e.g. 20-100):", size_hint=(1, 0.1)))
        self.port_range_input = TextInput(multiline=False)
        self.add_widget(self.port_range_input)

        # Scan button
        self.scan_button = Button(text="Scan Ports", size_hint=(1, 0.15))
        self.scan_button.bind(on_press=self.scan_ports)
        self.add_widget(self.scan_button)

        # Result label
        self.result_label = Label(text="", size_hint=(1, 0.6))
        self.add_widget(self.result_label)

    def scan_ports(self, instance):
        target = self.target_input.text.strip()
        port_range = self.port_range_input.text.strip()

        try:
            start_port, end_port = map(int, port_range.split("-"))
        except:
            self.result_label.text = "[ERROR] Invalid port range format."
            return

        open_ports = []
        for port in range(start_port, end_port + 1):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                result = sock.connect_ex((target, port))
                if result == 0:
                    open_ports.append(port)
                sock.close()
            except:
                pass

        if open_ports:
            self.result_label.text = f"Open Ports: {', '.join(map(str, open_ports))}"
        else:
            self.result_label.text = "No open ports found."

class PortScannerApp(App):
    def build(self):
        return PortScanner()

if __name__ == "__main__":
    PortScannerApp().run()
