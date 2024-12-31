from numerical_integration.scenes.quadrant_rule import QuadrantRule

class RectangleRule(QuadrantRule):
    riemann_func = "get_riemann_rectangles"
    title_text = "Rectangle Rule"

# To render the scene, run the following command in your terminal:
# poetry run manimgl rectangle_rule.py RectangleRule -o