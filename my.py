
You would include any libraries your project depends on.

### 3. **`app/main.py`**

Here’s a basic Python script to put in `app/main.py`:

```python
import requests

def fetch_website_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Content fetched successfully from {url}")
        print(response.text[:200])  # print first 200 chars of the content
    else:
        print(f"Failed to fetch content. Status code: {response.status_code}")

if __name__ == "__main__":
    url = input("Enter a URL to fetch: ")
    fetch_website_content(url)
