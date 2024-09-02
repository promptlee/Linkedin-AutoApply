import requests

def encode_company_name(company_name):
    """
    Encode the company name for use in a URL.
    
    Parameters:
    - company_name: The name of the company to encode.
    
    Returns:
    - The encoded company name.
    """
    company_name = company_name.lower()
    company_name = company_name.strip()

    return company_name.replace(' ', '%20')

def google_search(company_name):
    
    # Google Custom Search API endpoint
    url = 'https://www.glassdoor.com/Search/results.htm?keyword='+encode_company_name(company_name)
    
    # Parameters for the API request
    params = {
        'key': api_key,
        'cx': cx,
        'q': query,
        'num': num_results  # Number of search results to return (1-10)
    }
    
    try:
        # Make the request to the API
        response = requests.get(url, params=params)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse JSON response
            search_results = response.json()
            return search_results.get('items', [])
        else:
            # Print detailed error response for debugging
            error_info = response.json()
            error_message = error_info.get('error', {}).get('message', 'Unknown error')
            print(f"Error: {response.status_code} - {error_message}")
            return []
    
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Replace with your API key and Custom Search Engine ID
    API_KEY = 'AIzaSyDpTXpbgMEXYg9C6PSLevVw6L0McqOFjTg'
    CX = 'c3adba93a665542f4'
    
    query = 'Python programming'
    results = google_search(query, API_KEY, CX)
   

    # Print search results
    for result in results:
        print(result['title'])
        print(result['link'])
        print(result['snippet'])
        print()

