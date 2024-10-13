import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class Plot:
    def __init__(self, signal):
        self.signal = signal
    
    def plot_real(self):
        """Plot real part of the signal."""
        plt.plot(self.signal.t_values, self.signal.signal.real)
        plt.title('Real Signal')
        plt.xlabel('t')
        plt.ylabel('Amplitude')
        plt.show()

    def plot_complex(self):
        """Plot complex signal with Modulo (Magnitude) and Argument (Phase) in one window with two subplots."""
        fig, axs = plt.subplots(2, 1, figsize=(10, 8))  # Create a figure with 2 rows and 1 column of subplots

        # Plot magnitude (Modulo)
        axs[0].plot(self.signal.t_values, np.abs(self.signal.signal))
        axs[0].set_title('Magnitude (Modulo)')
        axs[0].set_xlabel('t')
        axs[0].set_ylabel('Amplitude')

        # Plot phase (Argument)
        axs[1].plot(self.signal.t_values, np.angle(self.signal.signal))
        axs[1].set_title('Phase (Argument)')
        axs[1].set_xlabel('t')
        axs[1].set_ylabel('Phase')

        # Adjust layout for better spacing
        fig.tight_layout()

        # Show the plots
        plt.show()

    def interactive_plot(self):
        """Interactive plot using Plotly."""
        import plotly.graph_objects as go
        
        fig = go.Figure()

        if np.iscomplexobj(self.signal.signal):
            # Modulo (Magnitude)
            fig.add_trace(go.Scatter(x=self.signal.t_values, y=np.abs(self.signal.signal),
                                     mode='lines', name='Magnitude'))
            # Argument (Phase)
            fig.add_trace(go.Scatter(x=self.signal.t_values, y=np.angle(self.signal.signal),
                                     mode='lines', name='Phase'))
        else:
            fig.add_trace(go.Scatter(x=self.signal.t_values, y=self.signal.signal,
                                     mode='lines', name='Real Signal'))

        fig.update_layout(title="Interactive Plot", xaxis_title="t", yaxis_title="Amplitude/Phase")
        fig.show()
