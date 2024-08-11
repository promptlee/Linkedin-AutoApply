from utils.helpers import read_json_file, match_job_titles, write_to_json


desired_jobs = ['sales representative','sales executive','sales manager','Sales Development Specialist',
    'Arabic Speaking Sales Assosiate',
    'Sales Development Specialist',
    'Sales Development Representative',
    'Sales Specialist',
    'Sales Associate',
    'Sales Assistant'
    ]

test_jobs = read_json_file("jobs.json")

matched_job_titles,unmatched = match_job_titles(test_jobs,desired_jobs)

write_to_json(unmatched, 'unmatched_jobs.json')

print(matched_job_titles)

