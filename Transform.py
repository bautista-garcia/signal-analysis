from scipy.fft import fft, fftfreq, fftshift
import numpy as np
import matplotlib.pyplot as plt

class Transform:
    def __init__(self, signal):
        self.signal = signal

    def fourier_transform(self):
        """Apply Fourier Transform and return frequency domain signal with symmetric frequencies."""
        N = len(self.signal.signal)
        T = self.signal.t_values[1] - self.signal.t_values[0]  # Sampling interval
        yf = fft(self.signal.signal)  # Perform Fourier transform
        xf = fftfreq(N, T)  # Compute the corresponding frequencies
        xf = fftshift(xf)   # Shift the zero frequency component to the center
        yf = fftshift(yf)   # Shift the FFT output to match symmetric frequencies
        return xf, yf

    def plot_fourier(self):
        """Plot the Fourier Transform with Magnitude and Phase in one window (symmetric frequency range)."""
        # Get the Fourier transform results with symmetric frequency range
        xf, yf = self.fourier_transform()

        # Create a figure with two subplots (Magnitude and Phase)
        fig, axs = plt.subplots(2, 1, figsize=(10, 8))

        # Plot magnitude (Modulo) in the first subplot
        axs[0].plot(xf, np.abs(yf))
        axs[0].set_title('Fourier Transform - Magnitude (Modulo)')
        axs[0].set_xlabel('Frequency (Hz)')
        axs[0].set_ylabel('Amplitude')

        # Plot phase (Argument) in the second subplot
        axs[1].plot(xf, np.angle(yf))
        axs[1].set_title('Fourier Transform - Phase (Argument)')
        axs[1].set_xlabel('Frequency (Hz)')
        axs[1].set_ylabel('Phase')

        # Adjust layout for better spacing
        fig.tight_layout()

        # Show the plots
        plt.show()
