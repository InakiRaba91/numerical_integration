from numerical_integration.scenes.quadrant_rule import QuadrantRule

class SimpsonRule(QuadrantRule):
    riemann_func = "get_riemann_parabolas"
    title_text = "Simpson's Rule"

# To render the scene, run the following command in your terminal:
# poetry run manimgl simpson_rule.py SimpsonRule -o