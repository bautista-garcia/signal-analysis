import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

class ConvolucionCircular:
    def __init__(self, func1, func2):
        """
        Inicializa el visualizador de convolución circular con dos funciones periódicas.
        
        Args:
            func1 (callable): Primera función periódica en el dominio [-1/2, 1/2].
            func2 (callable): Segunda función periódica en el dominio [-1/2, 1/2].
        """
        self.s = np.linspace(-0.5, 0.5, 500)  # Dominio en el rango [-1/2, 1/2]
        self.func1 = func1
        self.func2 = func2
        self.shift = 0  # Valor inicial de desplazamiento
        self.initialize_plot()

    def initialize_plot(self):
        """Inicializa las gráficas y los widgets interactivos."""
        # Inicializar las funciones y su producto
        self.f1 = self.func1(self.s)
        self.f2 = self.func2(self.s, self.shift)
        self.product_result = self.f1 * self.f2

        # Configuración de la gráfica
        self.fig, self.ax = plt.subplots(3, 1, figsize=(14, 10))
        plt.subplots_adjust(left=0.1, bottom=0.25)

        # Gráfica de las funciones y el producto
        self.l1, = self.ax[0].plot(self.s, self.f1, label='Función 1')
        self.l2, = self.ax[1].plot(self.s, self.f2, label='Función 2 desplazada')
        self.l3, = self.ax[2].plot(self.s, self.product_result, label='Producto de Función 1 y Función 2')

        # Ajustar límites de los ejes y agregar leyendas
        for axis in self.ax:
            axis.set_ylim(-1.5, 1.5)
            axis.legend()

        # Agregar línea punteada inicial para el shift en la gráfica del producto
        self.shift_line = self.ax[2].axvline(0, color='r', linestyle='--', label='Shift actual')

        # Configurar slider para el desplazamiento de la segunda función
        self.ax_shift = plt.axes([0.2, 0.1, 0.65, 0.03])
        self.slider_shift = Slider(self.ax_shift, 'Desplazamiento', -1, 1, valinit=0)
        self.slider_shift.on_changed(self.update_plot)  # Conectar el slider a la actualización

    def update_plot(self, val):
        """Actualiza la gráfica cuando se mueve el slider."""
        self.shift = self.slider_shift.val  # Obtiene el valor actual del desplazamiento del slider
        f2_shifted = self.func2(self.s, self.shift)
        product_result = self.f1 * f2_shifted

        # Actualizar los datos en las gráficas
        self.l2.set_ydata(f2_shifted)
        self.l3.set_ydata(product_result)

        # Actualizar la posición de la línea punteada
        self.shift_line.remove()  # Elimina la línea existente para evitar superposiciones
        self.shift_line = self.ax[2].axvline(self.shift, color='r', linestyle='--', label='Shift actual')

        self.fig.canvas.draw_idle()  # Redibuja la gráfica en tiempo real


    def show(self):
        """Mostrar la gráfica interactiva."""
        plt.show()


