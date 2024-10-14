import numpy as np
import re
import matplotlib.pyplot as plt
from Signal import Signal
from Plot import Plot
from Transform import Transform


class App:
    def __init__(self):
        self.signal = None
        self.plot = None
        self.transform = None
    
    def run(self):
        """Main entry point for the application."""
        # Define time domain values
        t_values = np.linspace(0.0, 1.0, 500)

        # Get the function from user input
        user_function = input("Enter your signal function (use 't' as the variable): ")

        # Parse the user input to replace common expressions (optional)
        user_function = self.preprocess_input(user_function)

        # Evaluate the function safely using eval()
        signal_function = self.create_signal_function(user_function)

        # Create a signal using the user-defined function
        self.signal = Signal(t_values, signal_function, complex_signal=True)

        # Plot the signal
        self.plot = Plot(self.signal)
        self.plot.plot_complex()

        # Perform Fourier Transform and plot the results
        self.transform = Transform(self.signal)
        self.transform.plot_fourier()

    def preprocess_input(self, user_function):
        """Preprocess the user input to replace regular expressions."""

        # PI Regex
        user_function = re.sub(r'\bpi\b', 'np.pi', user_function)

        # j Regex
        user_function = re.sub(r'\bj\b', '1j', user_function)


        # Sen regex
        user_function = re.sub(r'\bsen\b', 'np.sin', user_function)

        # Cos regex
        user_function = re.sub(r'\bcos\b', 'np.cos', user_function)

        # e regex
        user_function = re.sub(r'\be\^', 'np.exp', user_function)

        # Sinc regex
        user_function = re.sub(r'\bsinc\b', 'np.sinc', user_function)

        # Square root regex
        user_function = re.sub(r'\bsqrt\b', 'np.sqrt', user_function)

        # Logarithm regex
        user_function = re.sub(r'\blog\b', 'np.log', user_function)

        # Power regex
        user_function = re.sub(r'\^', '**', user_function)

        

        # Spaces for multiplication regex - TODO
        # user_function = re.sub(r'(\d|\b\w+\b)\s+(\d|\b\w+\b)', r'\1*\2', user_function)

        return user_function

    def create_signal_function(self, user_function):
        """Create a lambda function from the user input."""
        # Create a safe environment with numpy imported
        safe_env = {
            'np': np,
            't': None  # We will supply 't' when calling the function
        }

        # Create a lambda function that takes 't' as input
        signal_function = eval(f"lambda t: {user_function}", safe_env)
        return signal_function

if __name__ == "__main__":
    app = App()
    app.run()
