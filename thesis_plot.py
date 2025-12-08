import matplotlib as mpl

def set_thesis_style():
    """
    Set global Matplotlib style for Thesis plots.
    """

    mpl.rcParams.update({

        # FONT
        "font.family": "sans-serif",
        "font.sans-serif": ["TeX Gyre Heros", "Helvetica", "Arial"],
        "font.size": 11,

        # AXES & TICKS
        "axes.edgecolor": "black",
        "axes.linewidth": 0.8,
        "axes.labelsize": 11,
        "axes.titlesize": 13,

        "xtick.color": "black",
        "ytick.color": "black",
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,

        # GRID
        "axes.grid": True,
        "grid.color": "0.7",
        "grid.linestyle": "-",
        "grid.linewidth": 0.4,
        "grid.alpha": 0.4,

        # FIGURES
        "figure.dpi": 300,
        "savefig.dpi": 300,
        "figure.autolayout": True,
    })
