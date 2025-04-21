from pydantic import BaseModel, Field
from typing import Optional, List

class WorkDetails(BaseModel):
    company_name: Optional[str] = Field(None, description='Full name of the organization the candidate worked or currently works at (e.g., Google, Amazon). If no name is mentioned set to null.')
    designation: Optional[str] = Field(None, description='The job title or position held by the candidate at the specified company (e.g., Software Engineer, QA Lead).')
    period: str = Field(None, description='The duration of employment at the company, ideally in the format "MM/YYYY to MM/YYYY" or "MM/YYYY or YYYY to Present or Current" if still employed.')

class EducationDetails(BaseModel):
    degree: str = Field(None, description='The academic qualification obtained by the candidate (e.g., Bachelor of Science in Computer Engineering, MBA ... etc).')
    college_name: str = Field(None, description='The full name of the institution or university where the degree was pursued.')
    year_of_completion: int = Field(None, description='The year in which the candidate completed the degree program (e.g., 2020).')

class ResumeChecklist(BaseModel):
    name: str = Field(..., description='Full name of the candidate as mentioned in the resume.')
    role: str = Field(..., description='Job role the candidate is applying for or the most relevant job title based on the resume content.')
    links: Optional[List[str]] = Field(None, description='Links attached in the resume like the link to GitHub / LinkedIn / Portfolio Website / Blogs...')
    professional_summary: str = Field(..., description='A brief summary of the candidate\'s career objectives, key skills, and professional focus.')
    work_experience: Optional[List[WorkDetails]] = Field(None, description='Details of professional work experience of the candidate, including company, designation, and duration.')
    total_work_experience: str = Field(..., description='Total years of professional experience (e.g., "5", "10+" if currently employed). If the candidate\'s last work experience is ongoing (e.g., the word \'current\' is mentioned), append a '+' to indicate it\'s still active. In that case, use the current year (2025) to calculate experience duration. Otherwise, calculate the duration using the end year provided.')
    education: Optional[List[EducationDetails]] = Field(None, description='Highest or most relevant educational qualification with institution and completion year.')
    courses: Optional[List[str]] = Field(None, description='List of non-degree courses or certifications completed by the candidate (e.g., "Data Science Bootcamp", "Certified Scrum Master"). Please note the education details are different from coursework done by the candidate.')
    publications: Optional[List[str]] = Field(None, description='List of academic or professional publications, if any, authored or co-authored by the candidate.')
    projects_count: Optional[int] = Field(None, description="Number of distinct projects mentioned or led in resume")
    accomplishments: Optional[List[str]] = Field(None, description='Professional achievements, awards, recognitions, or notable contributions mentioned in the resume. This can be in an embedded in a paragraph too.')
    skills: Optional[List[str]] = Field(None, description='Explicitly listed technical or soft skills (e.g., Python, Agile, Leadership) extracted from the resume. Note that this can  be listed under skills or skill highlights , if  both exist combine the content from both and only take the unique set of skills.')
    expected_salary: Optional[int] = Field(..., description='The salary the candidate expects to receive, ideally in the local currency and as an annual amount (e.g., 70000 for $70,000/year). If nothing is mentioned simply return 0.')
