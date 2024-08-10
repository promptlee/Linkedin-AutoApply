from utils.helpers import read_json_file, match_job_titles


desired_jobs = [
  "Engineer",
  "Designer",
  "Doctor",
  "Artist",
  "Teacher",
  "Plumber",
  "Lawyer",
  "Nurse",
  "Writer",
  "Analyst",
  "Sales Associate",
  "Project Manager",
  "Software Developer",
  "Product Designer",
  "Marketing Specialist",
  "Customer Support Representative",
  "Financial Analyst",
  "Human Resources Manager",
  "Chief Executive Officer (CEO)",
  "Senior Software Development Engineer",
  "Lead Product Marketing Manager",
  "Business Intelligence Analyst",
  "Environmental Health and Safety Specialist",
  "Director of Human Resources",
  "Senior Vice President of Sales",
  "Executive Director of Corporate Communications",
  "Assistant Vice President of Operations",
  "Head of Global Supply Chain Management",
  "Chief Technology Officer of Innovative Solutions",
  "Vice President of Business Development and Strategic Partnerships"
]

test_jobs = read_json_file("tests/testjobs.json")

matched_job_titles = match_job_titles(test_jobs,desired_jobs)

print(matched_job_titles)

