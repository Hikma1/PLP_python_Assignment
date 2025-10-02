# Ubuntu-Inspired Image Fetcher 🌍
# "I am because we are"

import os
import requests
from urllib.parse import urlparse
from pathlib import Path


def fetch_image(url):
    # Create folder if it doesn’t exist
    folder = Path("Fetched_Images")
    folder.mkdir(parents=True, exist_ok=True)

    try:
        # Request image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises HTTPError for bad responses

        # Extract filename from URL or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path) or "downloaded_image.jpg"

        # Ensure unique filename if file already exists
        filepath = folder / filename
        counter = 1
        while filepath.exists():
            filepath = folder / f"{filepath.stem}_{counter}{filepath.suffix}"
            counter += 1

        # Save image in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✅ Success! Image saved as: {filepath}")

    except requests.exceptions.MissingSchema:
        print("❌ Error: Invalid URL format. Please include http:// or https://")
    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"❌ Network error: {req_err}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    print("Ubuntu-Inspired Image Fetcher 🌍")
    print("The Wisdom of Ubuntu: 'I am because we are'\n")
    url = input("Enter an image URL to fetch: ").strip()
    fetch_image(url)
