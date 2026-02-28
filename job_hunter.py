import requests
from bs4 import BeautifulSoup

def find_jobs():
    print("Searching for Python roles...")
    
    # 1. Get the data from the web
    url = "https://realpython.github.io/fake-jobs/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="ResultsContainer")

    # 2. Filter for Python jobs
    job_elements = results.find_all("div", class_="card-content")
    python_jobs = [
        j_elem for j_elem in job_elements
        if "python" in j_elem.find("h2", class_="title").text.lower()
    ]

    print(f"Found {len(python_jobs)} Python-related openings!\n")

    # 3. Loop through and save/print
    for job in python_jobs:
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()
        
        print(f"Role: {title}")
        print(f"Company: {company}")
        print(f"Location: {location}")
        print("-" * 20)
        
        # This saves it to a file on your ThinkPad
        with open("found_jobs.txt", "a") as f:
            f.write(f"Role: {title} | Company: {company} | Location: {location}\n")

if __name__ == "__main__":
    find_jobs()
    with open("found_jobs.txt", "a") as f:
    f.write(f"Role: {title} | Company: {company} | Location: {location}\n")