
<h1 align="center">GPS Map Visualizer</h1>

This project provides a Python script that reads GPS coordinates from a CSV file, plots them on an interactive map, and saves the result as both an interactive HTML file and a static PNG screenshot. It uses pandas for data manipulation, folium for map generation, and selenium for automated screenshot capture.

## Features

- **CSV Data Input**: Reads latitude and longitude data from a CSV file.
- **Data Cleaning**: Automatically handles non-numeric values, drops entries with missing coordinates, and removes duplicate points.
- **Interactive Map Generation**: Creates a beautiful, interactive map using Folium with clustered markers for better readability when dealing with many points.
- **Auto-fit Bounds**: The map automatically zooms and centers to fit all plotted data points.
- **Automated Screenshot**: Uses a headless Chrome browser via Selenium to capture a high-resolution screenshot of the map.

## Demo / Output

The script generates two primary output files:

- **gps_map.html**: An interactive map. You can zoom, pan, and click on marker clusters to explore the data points.
- **gps_map_screenshot_... .png**: A static image of the map, perfect for embedding in reports, presentations, or sharing.

![alt text](https://github.com/Sharan-Kumar-R/GPS-Map-Visualizer/blob/main/Map_Plotted.png)

## Prerequisites

Before running the script, you need to have Python and the following packages installed.

- **Python 3.6+**
- **pip** (Python package installer)
- **ChromeDriver**: The script uses Selenium to control a Chrome browser. You must download the [ChromeDriver](https://chromedriver.chromium.org/) that matches your installed Chrome browser version. 

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

**Dataset Source**: This project works great with the [Geolocation Dataset from Kaggle](https://www.kaggle.com/datasets/liewyousheng/geolocation?resource=download) which contains comprehensive GPS coordinates for cities worldwide.

**Example cities.csv format**:
```csv
id,name,state_id,state_code,state_name,country_id,country_code,country_name,latitude,longitude,wikiDataId
52,Ashkasham,3901,BDS,Badakhshan,1,AF,Afghanistan,36.68333000,71.53333000,Q4805192
68,Fayzabad,3901,BDS,Badakhshan,1,AF,Afghanistan,37.11660000,70.58002000,Q156558
78,Jurm,3901,BDS,Badakhshan,1,AF,Afghanistan,36.86477000,70.83421000,Q10308323
84,Khandud,3901,BDS,Badakhshan,1,AF,Afghanistan,36.95127000,72.31800000,Q3290334
```

### Run the script:
Open your terminal or command prompt, navigate to the project directory, and execute the script.

```bash
python GPS.py
```

### Console Output Example
When you run the script, you'll see output similar to this:

```
📂 Reading CSV from: C:\Users\shana\OneDrive\Desktop\GitHub\cities.csv
✅ 147209 unique valid points processed.
✅ Map saved to: C:\Users\shana\OneDrive\Desktop\GitHub\gps_map.html
📸 Capturing map screenshot...

DevTools listening on ws://127.0.0.1:58090/devtools/browser/1bf5a2e-80c8-4329-a3ed-0f1ee550916a
✅ Screenshot saved to: C:\Users\shana\OneDrive\Desktop\GitHub\gps_map_screenshot_20250616_210420.png
✅ Browser closed.
```

### Check the output:
- The script will print its progress to the console.
- Upon completion, you will find `gps_map.html` and `gps_map_screenshot_... .png` in the project directory.
- The interactive map (`gps_map.html`) will automatically open in your default web browser.

## Project Structure

```
gps-map-visualizer/
├── GPS.py                      # The main Python script
├── cities.csv                  # Input data file with GPS coordinates
├── gps_map.html                # Output: Generated interactive map
├── gps_map_screenshot_... .png # Output: Generated map screenshot
└── README.md                   # This file
```
## Configuration

You can easily modify the script's behavior by changing the configuration variables at the top of the `GPS.py` file.

```python
# --- Configuration ---
BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "cities.csv"
HTML_MAP_PATH = BASE_DIR / "gps_map.html"
SCREENSHOT_PATH = BASE_DIR / f"gps_map_screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 800
```

- CSV_PATH: Path to your input data file.
- HTML_MAP_PATh: Path where the HTML map will be saved.
- WINDOW_WIDTH / WINDOW_HEIGHT: Dimensions of the screenshot image in pixels.

## Troubleshooting

### Common Issues

**ChromeDriver not found**
```
selenium.common.exceptions.WebDriverException: 'chromedriver' executable needs to be in PATH
```
**Solution**: Download ChromeDriver and add to your system PATH or place in project directory.

**CSV reading errors**
```
❌ Error reading CSV: [Errno 2] No such file or directory: 'cities.csv'
```
**Solution**: Ensure `cities.csv` exists in the project directory with proper formatting.

**No valid GPS data**
```
⚠ No valid GPS data points found.
```
**Solution**: Check your CSV format and ensure coordinates are valid numbers (latitude: -90 to 90, longitude: -180 to 180).

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

In case of any Queries kindly leave a text or put mail given in my profile.

<p align="center">
⭐ <strong>Star this repository if you found it helpful!</strong>
</p>
