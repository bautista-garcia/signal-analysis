# Importing modules from separate files
from Signal import Signal
from Plot import Plot
from Transform import Transform
import numpy as np
import matplotlib.pyplot as plt


class App:
    def __init__(self):
        self.signal = None
        self.plot = None
        self.transform = None
    
    def run(self):
        """Main entry point for the application."""
        # Valores del dominio temporal
        t_values = np.linspace(-4 * np.pi, 4 * np.pi, 1000)

        # Create a real signal (Example: sine wave)
        self.signal = Signal(t_values, lambda t: np.cos(2 * np.pi * t), complex_signal=True)
        self.plot = Plot(self.signal)
        self.transform = Transform(self.signal)

        # Plot the real signal
        self.plot.plot_complex()
        
        # Plot the Fourier Transform
        self.transform.plot_fourier()



if __name__ == "__main__":
    app = App()
    app.run()
