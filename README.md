# OverWatch V1

OverWatch is a desktop system-monitoring application built with **Python**, **Tkinter**, **Matplotlib**, and **psutil**. It provides a graphical interface for viewing key hardware and operating-system information, with pie charts for live resource utilisation.

## Features

- **Operating system**
  - OS name, release, version, architecture, and machine type
  - System uptime
- **CPU**
  - Processor name
  - Physical and logical core counts
  - Minimum, maximum, and current frequency
  - Live CPU utilisation chart
- **RAM**
  - Total installed RAM
  - RAM utilisation chart
- **Storage**
  - Total capacity of the `C:\` drive
  - Disk utilisation chart
- **GPU**
  - NVIDIA GPU model
  - Total VRAM
  - VRAM utilisation chart
- Simple Tkinter navigation with separate views for each category

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Tkinter | Desktop GUI |
| psutil | CPU, memory, disk, and uptime information |
| Matplotlib | Resource utilisation pie charts |
| NVIDIA System Management Interface (`nvidia-smi`) | NVIDIA GPU and VRAM information |
| PowerShell / CIM | CPU model detection on Windows |

## Project Structure

```text
OverWatch/
├── main.py          # Tkinter interface and charts
├── system_info.py   # System information and hardware metrics
└── README.md
```

Keep `main.py` and `system_info.py` in the same directory because the GUI imports the `system_info` module.

## Requirements

- Windows
- Python 3.9 or later
- An NVIDIA GPU with working NVIDIA drivers and `nvidia-smi` available for the GPU section
- Python packages:
  - `psutil`
  - `matplotlib`

Tkinter is included with most standard Windows Python installations.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/<your-repository>.git
   ```

2. Move into the project directory:

   ```bash
   cd <your-repository>
   ```

3. (Recommended) Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

4. Install the dependencies:

   ```bash
   pip install psutil matplotlib
   ```

5. Run the application:

   ```bash
   python main.py
   ```

## Usage

Launch `main.py`. Select **OS**, **CPU**, **RAM**, **Memory**, or **GPU** from the main screen to open the corresponding information panel. Use **Go back** to return to the main menu, or **EXIT** to close the application.

## Platform Notes and Limitations

- The current implementation is Windows-oriented: CPU identification uses PowerShell, and GPU information is queried through `nvidia-smi`.
- The storage panel currently monitors the `C:\` drive only.
- The GPU panel requires compatible NVIDIA drivers and an accessible `nvidia-smi` executable. Systems without NVIDIA support may not be able to open that panel.
- Resource charts are refreshed using Tkinter's `after()` scheduling.
- The project currently focuses on monitoring and displaying metrics; it does not modify system settings or control hardware.

## Potential Improvements

- Add support for AMD and Intel GPU monitoring.
- Allow users to select which disk drive to monitor.
- Display additional metrics such as temperatures, network activity, and per-process usage.
- Update existing Matplotlib charts instead of recreating them on every refresh.
- Add error handling for unavailable hardware metrics and missing system utilities.
- Improve layout responsiveness and visual styling.

## Contributing

Contributions, bug reports, and feature suggestions are welcome. For substantial changes, consider opening an issue first to discuss the proposed update.

## License

No license has been specified yet. Add a `LICENSE` file before presenting the project as open source.
