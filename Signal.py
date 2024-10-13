import numpy as np

class Signal:
    def __init__(self, t_values, signal_func, complex_signal=False):
        self.t_values = t_values  # Time values
        self.signal_func = signal_func  # Function to generate signal
        self.complex_signal = complex_signal  # Flag for complex signal
        self.signal = self.generate_signal()

    def generate_signal(self):
        """Generate signal values based on the provided function."""
        if self.complex_signal:
            return self.signal_func(self.t_values)  # For complex-valued signal
        else:
            return self.signal_func(self.t_values).real  # For real-valued signal
