import matplotlib.pyplot as plt
import numpy as np

from IPython.display import HTML
from matplotlib.animation import FuncAnimation
from typing import Callable

plt.style.use("ggplot")


def create_modulation_animation(
            modulation: Callable,
            fc: float,
            num_frames: int,
            plot_duration: float,
            time_step=0.001,
            animation_step=0.01,
            save_path=""
        ):

    total_time = num_frames * animation_step
    t = np.arange(0, total_time*2, time_step)
    signal = np.cos(2 * np.pi * fc * t)

    figure, axis = plt.subplots()
    axis: plt.Axes
    axis.set_xlim(0, plot_duration)
    axis.set_ylim(-2, 2)

    line, = axis.plot([], [], label="Сигнал", color='green')
    axis.legend()

    axis.set_xlabel("Время (с)", fontsize=11, color='black')
    axis.set_ylabel("Амплитуда", fontsize=11, color='black')
    axis.set_title("Анимация модулированного сигнала", fontsize=12)

    axis.set_facecolor('white')
    for spine in axis.spines.values():
        spine.set_color('black')
    axis.tick_params(axis='x', colors='black')
    axis.tick_params(axis='y', colors='black')

    def update(frame):
        current_start_time = frame * animation_step
        current_end_time = current_start_time + plot_duration

        time_interval = (t >= current_start_time) & (t < current_end_time)
        current_t = t[time_interval]
        modulated_signal = modulation(t[time_interval]) * signal[time_interval]

        line.set_data(current_t, modulated_signal)
        axis.set_xlim(current_start_time, current_end_time)
        return line,

    animation = FuncAnimation(
        fig=figure,
        func=update,
        frames=num_frames,
        blit=True,
        interval=animation_step*1000
    )

    if save_path:
        animation.save(save_path, fps=30)

    return animation


def modulation_function(t):
    return np.cos(t * 6)


num_frames = 100
plot_duration = np.pi / 2
time_step = 0.001
animation_step = np.pi / 200
fc = 50
save_path_with_modulation = "modulated_signal.gif"

animation = create_modulation_animation(
    modulation=modulation_function,
    fc=fc,
    num_frames=num_frames,
    plot_duration=plot_duration,
    time_step=time_step,
    animation_step=animation_step,
    save_path=save_path_with_modulation
)
HTML(animation.to_jshtml())
