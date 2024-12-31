from abc import ABC, abstractmethod
from manimlib import *

from numerical_integration.utils.axes import CustomAxes
from numerical_integration.utils.functions import transformed_func

class QuadrantRule(Scene, ABC):
    @property
    @abstractmethod
    def riemann_func(self):
        pass

    @property
    def title_text(self):
        pass

    def construct(self):        
        integral_x_range = (-1, 1)            

        # Create axes
        axes = CustomAxes(x_range=(-1.5, 1.5), y_range=(0, 5), axis_config={"color": BLUE}, width=12, height=6)

        # Create the graph of the function
        graph = axes.get_graph(transformed_func, color=ORANGE)

        # add title
        title = Text(self.title_text, font_size=60, color=BLUE).to_edge(0.2*UP)
        self.add(title)

        # Create labels for the axes
        labels = axes.get_axis_labels(x_label_tex="x", y_label_tex="f(x)")
        [label.set_color(ORANGE) for label in labels]

        # Add axes, graph, and labels to the scene
        self.add(axes, graph, labels)

        # Add limits to the integral
        for x in integral_x_range:
            limit = DashedLine(
                start=axes.c2p(x, 0),
                end=axes.c2p(x, transformed_func(x)),
                dash_length=0.1,
                color=RED,
                stroke_width=7,
            )
            self.add(limit)
            # Add labels below the x-axis
            label = Tex(f"x={x}").set_color(RED).scale(0.75).next_to(axes.c2p(x, 0), DOWN)
            self.add(label)

        # Initial dx value
        dx = 2

        # draw area under the curve by riemann subintervals
        for _ in range(2):
            areas_subintervals = getattr(axes, self.riemann_func)(
                graph,
                x_range=integral_x_range,
                dx=dx,
                stroke_width=2,
                stroke_color=GREEN,
                stroke_background=False,
                fill_opacity=0.5,
            )
            self.play(ShowCreation(areas_subintervals))
            self.wait(1)
            self.remove(areas_subintervals)
            dx /= 2  # Decrease dx

        # Show final approximation
        final_areas_subintervals = getattr(axes, self.riemann_func)(
            graph,
            x_range=integral_x_range,
            dx=dx,
            stroke_width=2,
            stroke_color=GREEN,
            stroke_background=False,
            fill_opacity=0.5,
        )
        self.play(ShowCreation(final_areas_subintervals))
        self.wait(1)