import requests
from bs4 import BeautifulSoup

# URL of the Billboard Hot 100 chart
url = 'https://www.billboard.com/charts/hot-100/'

# Make a request to fetch the web page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the chart entries containing titles and artists
    chart_entries = soup.find_all('li', class_='o-chart-results-list__item')
    
    # Filter only the entries that have the necessary title and artist information
    filtered_entries = []
    for entry in chart_entries:
        if entry.find('h3', class_='c-title') and entry.find('span', class_='c-label'):
            filtered_entries.append(entry)

    # Take only the top 10 filtered entries
    filtered_entries = filtered_entries[:10]

    # Check if any valid chart entries are found
    if not filtered_entries:
        print("No valid chart entries found. The structure might have changed.")
    else:
        # Extract and print the top 10 tracks
        for idx, entry in enumerate(filtered_entries, 1):
            title_tag = entry.find('h3', class_='c-title')
            artist_tag = entry.find('span', class_='c-label')
            
            # Check if both title and artist tags are found
            if title_tag and artist_tag:
                title = title_tag.get_text(strip=True)
                artist = artist_tag.get_text(strip=True)
                print(f'{idx}. {title} by {artist}')
            else:
                print(f'{idx}. Information missing')
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
