
<h1 align="center">GPS Map Visualizer</h1>

This project provides a Python script that reads GPS coordinates from a CSV file, plots them on an interactive map, and saves the result as both an interactive HTML file and a static PNG screenshot. It uses pandas for data manipulation, folium for map generation, and selenium for automated screenshot capture.

## Features

- **CSV Data Input**: Reads latitude and longitude data from a cities.csv file.
- **Data Cleaning**: Automatically handles non-numeric values, drops entries with missing coordinates, and removes duplicate points.
- **Interactive Map Generation**: Creates a beautiful, interactive map using Folium with clustered markers for better readability when dealing with many points.
- **Auto-fit Bounds**: The map automatically zooms and centers to fit all plotted data points.
- **Automated Screenshot**: Uses a headless Chrome browser via Selenium to capture a high-resolution screenshot of the map.
- **Dynamic File Naming**: Screenshots are saved with a timestamp to avoid overwriting previous captures.
- **Cross-Platform**: Opens the generated HTML map in your default web browser for immediate viewing.

## Demo / Output

The script generates two primary output files:

- **gps_map.html**: An interactive map. You can zoom, pan, and click on marker clusters to explore the data points.
- **gps_map_screenshot_... .png**: A static image of the map, perfect for embedding in reports, presentations, or sharing.

![alt text](https://github.com/Sharan-Kumar-R/GPS-Map-Visualizer/blob/main/Map_Plotted.png)


## Prerequisites

Before running the script, you need to have Python and the following packages installed.

- **Python 3.6+**
- **pip** (Python package installer)
- **ChromeDriver**: The script uses Selenium to control a Chrome browser. You must download the ChromeDriver that matches your installed Chrome browser version. [Download ChromeDriver Here](https://chromedriver.chromium.org/)

After downloading, ensure `chromedriver.exe` (or `chromedriver` on Linux/macOS) is in your system's PATH.

## Installation

1. **Clone the repository**:
```bash
git clone https://github.com/Sharan-Kumar-R/GPS-Map-Visualizer.git
cd GPS-Map-Visualizer
```

2. **Install the required Python packages**:
```bash
pip install pandas folium selenium
```

## Usage

### Prepare your data:
Ensure you have a CSV file named `cities.csv` in the same directory as the script.
The CSV file must contain at least the following columns: `latitude`, `longitude`, `state_name`, and `country_name`.

**Example cities.csv format**:
```csv
city,state_name,country_name,latitude,longitude
New York,New York,United States,40.7128,-74.0060
Los Angeles,California,United States,34.0522,-118.2437
Paris,Île-de-France,France,48.8566,2.3522
```

### Run the script:
Open your terminal or command prompt, navigate to the project directory, and execute the script.

```bash
python GPS.py
```

### Check the output:
- The script will print its progress to the console.
- Upon completion, you will find `gps_map.html` and `gps_map_screenshot_... .png` in the project directory.
- The interactive map (`gps_map.html`) will automatically open in your default web browser.

## Project Structure

```
.
├── GPS.py                      # The main Python script
├── cities.csv                  # Input data file with GPS coordinates
├── gps_map.html                # Output: Generated interactive map
├── gps_map_screenshot_... .png # Output: Generated map screenshot
└── README.md                   # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

<p align="center">
⭐ <strong>Star this repository if you found it helpful!</strong>
</p>
