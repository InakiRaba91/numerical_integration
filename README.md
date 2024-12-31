# Numerical_integration

Educational repo to illustrate the concept of numerical integration for different methods:

Three scenes are included:
- Rectangle rule
- Trapezoidal rule
- Simpson's rule

In order to generate the visualizations, simply install the package and run the following command:

```bash
poetry install
```

Then you can generate the visualizations by running the following command:

```bash
poetry run manimgl numerical_integration/scenes/trapezoid_rule.py TrapezoidRule -o
```

If you just want to generate the final frame, simply run

```bash
poetry run manimgl numerical_integration/scenes/trapezoid_rule.py TrapezoidRule -os
```

