import json
# miscellaneous functions to help with 


def read_json_file(file_path):
    # Open the JSON file and load its contents into a Python object
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def write_to_json(data, filename):
    # Writes to a JSON file
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print(f"Data written to {filename}")

def match_job_titles(jobs_results, desired_titles):
    # Normalize desired titles for case-insensitive comparison
    normalized_desired_titles = [title.lower() for title in desired_titles]
    
    matched = []
    unmatched = []
    
    for job in jobs_results:
        # Normalize job title
        job_title = job['title'].lower()
        
        # Check if job title contains any of the desired titles 
        if any(desired_title in job_title for desired_title in normalized_desired_titles):
            matched.append(job['title'])  # Append the job results title
        else:
            unmatched.append(job['title']) 
    print(f"Matched {len(matched)} job titles, Unmatched {len(unmatched)} ")
    return matched,unmatched

