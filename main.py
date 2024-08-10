import re
import os
import json
from dotenv import load_dotenv
from linkedin_api import Linkedin
from utils.helpers import read_json_file, match_job_titles, write_to_json


# Load environment variables from .env file
load_dotenv()

user_name = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')

api = Linkedin(user_name, password)

# desired_titles = ['AI Engineer','Gen AI Engineer','Conversational AI']
desired_titles = ['sales representative','sales executive','sales manager'"Sales Development Specialist",
    "Arabic Speaking Sales Assosiate",
    "Sales Development Specialist",
    "Sales Development Representative",
    "Sales Associate"]

jobs_results = api.search_jobs(
    ###### find out what combination of keywords and jobtitle gets most results 
    keywords = 'sales representative',
    job_title = desired_titles,
    # remote = ['2','3'],
    limit=50
)

# with open('jobs.json', 'r') as file:
#    jobs_results = json.load(file)

# Example usage with the existing code
job_title_matches, unmatched = match_job_titles(jobs_results, desired_titles)

# Optionally, write the matched jobs to a JSON file
write_to_json(job_title_matches, 'matched_jobs.json')

write_to_json(unmatched, 'unmatched_jobs.json')

write_to_json(jobs_results, 'jobs.json')

