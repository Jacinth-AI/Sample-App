# Sample App — Minimal Python UI Demo

A tiny Tkinter application that demonstrates a visible GUI with basic navigation between three screens: **Home**, **Settings**, and **Details**.

## Requirements

- Python 3.8+ (Tkinter is included in the standard library on most platforms)

> **Linux note:** If Tkinter is not pre-installed, run:
> ```bash
> sudo apt-get install python3-tk   # Debian / Ubuntu
> ```

## How to Run

```bash
python app.py
```

A 500 × 400 window titled **Sample App** will open on the Home screen.

## Screens

| Screen   | Description |
|----------|-------------|
| Home     | Welcome message with buttons to Settings and Details. |
| Settings | Dummy toggle switches (dark mode, notifications). Back button to Home. |
| Details  | Placeholder info about the app. Buttons to Home and Settings. |

## How Navigation Works

All three screens are `ttk.Frame` widgets created once at startup and placed in the **same grid cell** of a container frame. They are stacked on top of each other.

Switching screens calls `frame.tkraise()`, which raises the target frame to the top of the stacking order — making it the visible screen. No widgets are destroyed or recreated, so transitions are instant.

```
container (grid cell 0,0)
├── home_frame      ← tkraise() brings this to front
├── settings_frame
└── details_frame
```

## Project Structure

```
Sample-App/
├── app.py      # Complete application code
└── README.md   # This file
```
