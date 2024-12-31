from numerical_integration.scenes.quadrant_rule import QuadrantRule

class TrapezoidRule(QuadrantRule):
    riemann_func = "get_riemann_trapezoids"
    title_text = "Trapezoid Rule"

# To render the scene, run the following command in your terminal:
# poetry run manimgl trapezoid_rule.py TrapezoidRule -o