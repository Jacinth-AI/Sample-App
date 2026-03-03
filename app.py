"""
Minimal Python UI Demo Application

Demonstrates a visible Tkinter GUI with basic navigation between three screens:
Home, Settings, and Details.

Navigation is implemented by stacking Frame widgets and using tkraise() to bring
the desired frame to the front. All frames are created once at startup and
layered in the same grid cell; switching screens simply raises one frame above
the others — no widgets are destroyed or recreated.
"""

import tkinter as tk
from tkinter import ttk
from typing import Callable, Dict


# ---------------------------------------------------------------------------
# Screen builders
# ---------------------------------------------------------------------------

def build_home(parent: tk.Frame, navigate: Callable[[str], None]) -> None:
    """Populate the Home screen."""
    ttk.Label(parent, text="Home", font=("Helvetica", 24, "bold")).pack(pady=(40, 10))
    ttk.Label(parent, text="Welcome to the Sample App!").pack(pady=(0, 30))

    ttk.Button(parent, text="Go to Settings", command=lambda: navigate("settings")).pack(pady=5)
    ttk.Button(parent, text="Go to Details", command=lambda: navigate("details")).pack(pady=5)


def build_settings(parent: tk.Frame, navigate: Callable[[str], None]) -> None:
    """Populate the Settings screen with a dummy toggle."""
    ttk.Label(parent, text="Settings", font=("Helvetica", 24, "bold")).pack(pady=(40, 10))

    dark_mode = tk.BooleanVar()
    ttk.Checkbutton(parent, text="Enable dark mode (demo only)", variable=dark_mode).pack(pady=10)

    notifications = tk.BooleanVar(value=True)
    ttk.Checkbutton(parent, text="Enable notifications (demo only)", variable=notifications).pack(pady=5)

    ttk.Button(parent, text="Back to Home", command=lambda: navigate("home")).pack(pady=20)


def build_details(parent: tk.Frame, navigate: Callable[[str], None]) -> None:
    """Populate the Details screen with placeholder information."""
    ttk.Label(parent, text="Details", font=("Helvetica", 24, "bold")).pack(pady=(40, 10))

    info = (
        "This is a minimal demo application built with Python and Tkinter.\n\n"
        "It showcases basic multi-screen navigation using frame stacking.\n"
        "No database, authentication, or backend is involved."
    )
    ttk.Label(parent, text=info, wraplength=400, justify="center").pack(pady=(0, 30))

    ttk.Button(parent, text="Back to Home", command=lambda: navigate("home")).pack(pady=5)
    ttk.Button(parent, text="Go to Settings", command=lambda: navigate("settings")).pack(pady=5)


# ---------------------------------------------------------------------------
# Application
# ---------------------------------------------------------------------------

class SampleApp(tk.Tk):
    """Main application window that manages screen navigation."""

    def __init__(self) -> None:
        super().__init__()
        self.title("Sample App")
        self.geometry("500x400")
        self.minsize(400, 350)

        # Container that holds all screens stacked on top of each other.
        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Create one frame per screen and place them in the same grid cell.
        self.frames: Dict[str, ttk.Frame] = {}
        builders = {
            "home": build_home,
            "settings": build_settings,
            "details": build_details,
        }

        for name, builder in builders.items():
            frame = ttk.Frame(container)
            frame.grid(row=0, column=0, sticky="nsew")
            builder(frame, self.navigate)
            self.frames[name] = frame

        # Show the Home screen first.
        self.navigate("home")

    def navigate(self, screen_name: str) -> None:
        """Raise the requested screen to the top of the stacking order."""
        if screen_name not in self.frames:
            print(f"Error: unknown screen '{screen_name}'. "
                  f"Valid screens: {', '.join(self.frames)}")
            return
        frame = self.frames[screen_name]
        frame.tkraise()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
