import pandas as pd
import folium
from folium.plugins import MarkerCluster
from pathlib import Path
from datetime import datetime
import webbrowser
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# --- Configuration ---
BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "cities.csv"
HTML_MAP_PATH = BASE_DIR / "gps_map.html"
SCREENSHOT_PATH = BASE_DIR / f"gps_map_screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 800

def read_and_parse_csv(csv_path):
    try:
        df = pd.read_csv(csv_path)
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        return pd.DataFrame()

    # Ensure latitude and longitude columns are numeric
    df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
    df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')

    # Filter valid points
    df = df[(df['latitude'].notna()) & (df['longitude'].notna())]
    df = df[(df['latitude'] != 0) & (df['longitude'] != 0)]
    df.drop_duplicates(subset=['latitude', 'longitude'], inplace=True)

    return df

def main():
    print(f"📂 Reading CSV from: {CSV_PATH}")
    df = read_and_parse_csv(CSV_PATH)

    if df.empty:
        print("⚠ No valid GPS data points found.")
        return

    print(f"✅ {len(df)} unique valid points processed.")

    # Build map
    gps_map = folium.Map(zoom_start=5)
    cluster = MarkerCluster().add_to(gps_map)

    for row in df.itertuples():
        folium.Marker(
            location=[row.latitude, row.longitude],
            popup=f"{row.state_name}, {row.country_name}\nLat: {row.latitude}, Lon: {row.longitude}",
            icon=folium.Icon(color='blue')
        ).add_to(cluster)

    gps_map.fit_bounds([
        [df['latitude'].min(), df['longitude'].min()],
        [df['latitude'].max(), df['longitude'].max()]
    ])

    gps_map.save(HTML_MAP_PATH)
    print(f"✅ Map saved to: {HTML_MAP_PATH}")

    # Screenshot
    print("📸 Capturing map screenshot...")
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument(f'--window-size={WINDOW_WIDTH},{WINDOW_HEIGHT}')

    try:
        driver = webdriver.Chrome(options=options)
        driver.get(HTML_MAP_PATH.as_uri())
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "leaflet-pane")))
        driver.save_screenshot(str(SCREENSHOT_PATH))
        print(f"✅ Screenshot saved to: {SCREENSHOT_PATH}")
    except Exception as e:
        print(f"❌ Selenium error: {e}")
    finally:
        driver.quit()
        print("✅ Browser closed.")

    webbrowser.open(HTML_MAP_PATH.as_uri())

if __name__ == "__main__":
    main()
