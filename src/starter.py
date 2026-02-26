import atlasopenmagic as atom
import pandas as pd

def initial_exploration():
    print("Fetching available ATLAS Open Data releases...")
    releases = atom.available_releases()
    print(f"Available releases: {releases}")
    
    # Using the most recent or common release mentioned in search results
    target_release = '2024r-pp'
    if target_release in releases:
        print(f"\nSetting release to {target_release}...")
        atom.set_release(target_release)
        
        # Example dataset ID (usually corresponding to Z->mumu or similar)
        example_sid = '301204'
        print(f"\nRetrieving metadata for Sample ID: {example_sid}")
        try:
            metadata = atom.get_metadata(example_sid)
            print("Metadata retrieved successfully!")
            print(metadata)
            
            print(f"\nRetrieving URLs for Sample ID: {example_sid}")
            urls = atom.get_urls(example_sid)
            print(f"Found {len(urls)} URLs for this sample.")
            if urls:
                print(f"Example URL: {urls[0]}")
        except Exception as e:
            print(f"Error retrieving metadata/URLs: {e}")
            print("Hint: You might need an active internet connection to fetch metadata from CERN.")
    else:
        print(f"Target release {target_release} not found in available releases.")

if __name__ == "__main__":
    initial_exploration()
