import json
import httpx

def encode_company_name(company_name: str):
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

def find_company(campany_name: str):
    """find company Glassdoor ID and name by query. e.g. "ebay" will return "eBay" with ID 7853"""
    company_name = encode_company_name(campany_name)
    result = httpx.get('https://www.glassdoor.com/Search/results.htm?keyword='+company_name)
   
   # Specify the file path (adjust as needed)
    file_path = 'glassdoor.html'

    # Write the HTML content to the file
    with open(file_path, 'w') as html_file:
        html_file.write(result.text)

    if result.status_code != 200:
        print(f"Request failed with status code: {result.status_code}")
        return None
    
    try:
        data = json.loads(result.content)
    except json.JSONDecodeError:
        print("Failed to decode JSON. Here's the response:")
        print(result.text)  # Print the raw response text for debugging
        return None
    
    # Assuming the response structure is correct and contains the expected data
    return data[0]["suggestion"], data[0]["employerId"]

find_company("bank of america")  # Example usage