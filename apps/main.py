from scrapper import *
import pandas as pd
from gemini import *
from Driveapi import *
from googlesheets import *
import markdown
from datetime import date


Googlesheetheader = ["ID", "NAME", "COMPANY NAME", "LINK", "RESUMEID", "SCRAPED DATE", "DESCRIPTION"]
Soup = gethtml(url)
job_list = extract_job_details(Soup)

dataframe = pd.DataFrame(job_list)

df = dataframe

for index, row in df.iterrows():
    job_desc = row['description']  # iterate through each description
    companyname = row['company']
    job_title = row["name"]
    job_ID = row["id"]
    apply_link = row["link"]
    today = date.today()
    resume = gemini(job_desc) #pass the description through gemini
    #print(resume)
    html = markdown.markdown(resume)
    resume_id = addtodrive(html, companyname,job_title)
    
    print(job_ID,companyname, job_title, resume_id, apply_link)
    new_row = pd.DataFrame([{
    "ID": f"{job_ID}",
    "NAME": f"{job_title}",
    "COMPANY NAME": f"{companyname}",
    "LINK": f"{apply_link}",
    "RESUME ID": f"{resume_id}",
    "SCRAPED DATE": f"{today}",
    "DESCRIPTION": f"{job_desc}"
        }])
    uploadtoworksheet(new_row)







        




