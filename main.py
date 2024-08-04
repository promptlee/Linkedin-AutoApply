import re
import os
import json
from dotenv import load_dotenv
from linkedin_api import Linkedin



def write_to_json(data, filename):
    # Writes to a JSON file
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print(f"Data written to {filename}")


def match_job_titles(jobs, desired_titles):
    # Normalize desired titles for case-insensitive comparison
    normalized_desired_titles = [title.lower() for title in desired_titles]

    # Regex pattern to identify "sales representative"
    pattern = re.compile(r'sales(?:\s+\w+)*\s+representative', re.IGNORECASE)
    
    matched_jobs = []
    for job in jobs:
        # Normalize job title
        job_title = job['title'].lower()
        if pattern.search(job_title):
            matched_jobs.append(job)
    
    print(f"Matched {len(matched_jobs)} jobs")
    return matched_jobs


# Load environment variables from .env file
load_dotenv()

user_name = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')

api = Linkedin(user_name, password)

# desired_titles = ['AI Engineer','Gen AI Engineer','Conversational AI']
desired_titles = ['sales representative','sales executive','sales manager']

jobs_results = api.search_jobs(
    keywords = 'sales representative',
    job_title = desired_titles,
    # remote = ['2','3'],
    limit=50
)

# with open('jobs.json', 'r') as file:
#    jobs_results = json.load(file)

# Example usage with the existing code
job_title_matches = match_job_titles(jobs_results, desired_titles)

# Optionally, write the matched jobs to a JSON file
write_to_json(job_title_matches, 'matched_jobs.json')

write_to_json(jobs_results, 'jobs.json')

