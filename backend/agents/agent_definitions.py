from agents import Agent
from backend.schemas.structured_output import RecruitmentDecision

recruiter_agent = Agent(name="recruiter agent",
                        model="gpt-4o",
                        instructions="Decide whether or not to recruit the candidate for the role",
                        output_type=RecruitmentDecision
                    )