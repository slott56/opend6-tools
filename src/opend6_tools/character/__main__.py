"""
The ``__main__`` module is a visible entry-point, creating an app from the ``character`` package.
"""

if __name__ == "__main__":  # pragma: no cover
    from .cli import app

    app()
