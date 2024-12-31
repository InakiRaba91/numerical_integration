from manimlib import *
from typing import Iterable, Sequence, Union


ManimColor = Union[str, Color, None]

class CustomAxes(Axes):
    def get_riemann_trapezoids(
        self,
        graph: ParametricCurve,
        x_range: Sequence[float] = None,
        dx: float | None = None,
        stroke_width: float = 1,
        stroke_color: ManimColor = BLACK,
        fill_opacity: float = 1,
        colors: Iterable[ManimColor] = (BLUE, GREEN),
        negative_color: ManimColor = RED,
        stroke_background: bool = True,
        show_signed_area: bool = True
    ) -> VGroup:
        if x_range is None:
            x_range = self.x_range[:2]
        if dx is None:
            dx = self.x_range[2]
        if len(x_range) < 3:
            x_range = [*x_range, dx]

        traps = []
        x_range[1] = x_range[1] + dx
        xs = np.arange(*x_range)
        for x0, x1 in zip(xs, xs[1:]):
            y0 = self.input_to_graph_point(x0, graph)
            y1 = self.input_to_graph_point(x1, graph)
            trap = Polygon(
                self.c2p(x0, 0),
                self.c2p(x1, 0),
                y1,
                y0,
            )
            traps.append(trap)
        result = VGroup(*traps)
        result.set_submobject_colors_by_gradient(*colors)
        result.set_style(
            stroke_width=stroke_width,
            stroke_color=stroke_color,
            fill_opacity=fill_opacity,
            stroke_behind=stroke_background
        )
        return result
    
    def get_riemann_parabolas(
        self,
        graph: ParametricCurve,
        x_range: Sequence[float] = None,
        dx: float | None = None,
        stroke_width: float = 1,
        stroke_color: ManimColor = BLACK,
        fill_opacity: float = 1,
        colors: Iterable[ManimColor] = (BLUE, GREEN),
        negative_color: ManimColor = RED,
        stroke_background: bool = True,
        show_signed_area: bool = True
    ) -> VGroup:
        if x_range is None:
            x_range = self.x_range[:2]
        if dx is None:
            dx = self.x_range[2]
        if len(x_range) < 3:
            x_range = [*x_range, dx]

        parabolas = []
        x_range[1] = x_range[1] + dx
        delta = 0.1
        xs = np.arange(*x_range)
        for x0, x2 in zip(xs, xs[1:]):
            x1 = (x0 + x2) / 2
            y0 = graph.underlying_function(x0)
            y1 = graph.underlying_function(x1)
            y2 = graph.underlying_function(x2)
            c = self._get_parabola_coeffs((x0, y0), (x1, y1), (x2, y2))
            parab_approx = self.get_graph(
                lambda t: c[0] * t**2 + c[1] * t + c[2],
                x_range=[x0, x2],
                color=GREEN,
                stroke_width=1.5
            )            
            parabola = VMobject()
            n = int((x2 - x0) / delta) + 1
            parab_points = [self.input_to_graph_point(t, parab_approx) for t in np.linspace(x0, x2, n)]
            parabola.set_points_as_corners([self.c2p(x0, 0), *parab_points, self.c2p(x2, 0)])
            parabolas.append(parabola)
        result = VGroup(*parabolas)
        result.set_submobject_colors_by_gradient(*colors)
        result.set_style(
            stroke_width=stroke_width,
            stroke_color=stroke_color,
            fill_opacity=fill_opacity,
            stroke_behind=stroke_background
        )
        return result
    
    def _get_parabola_coeffs(self, pt1, pt2, pt3):
        a = np.array([[pt1[0]**2, pt1[0], 1], [pt2[0]**2, pt2[0], 1], [pt3[0]**2, pt3[0], 1]])
        b = np.array([pt1[1], pt2[1], pt3[1]])
        x = np.linalg.solve(a, b)
        return x