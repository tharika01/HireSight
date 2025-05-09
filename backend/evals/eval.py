import os
import json
import pandas as pd
from backend.app import main
from config.config import setup_logger
from thefuzz import fuzz

logger = setup_logger()

class Eval():
    def __init__(self):
        pass

    def hard_match(self, expected_output, generated_output) -> bool:
        return expected_output == generated_output
    
    def fuzzy_match(self,  expected_output, generated_output, threshold=80) -> bool:
        ratio = fuzz.partial_ratio(expected_output.lower(), generated_output.lower()) 
        logger.info(f"fuzzy ratio {ratio}")
        return ratio > threshold
    
    def match_records(self,  expected_output, generated_output, threshold=90) -> bool:
        if len(expected_output)==0 and len(generated_output)==0:
            return True
        
        if len(expected_output) != len(generated_output):
            return False
        
        expected_output=set(map(str.lower, sorted(expected_output)))
        generated_output=set(map(str.lower, sorted(generated_output)))

        
        logger.info(f"expected output : {expected_output}\ngen o/p: {generated_output}")
        
        for (exp, gen) in zip(expected_output, generated_output):
            score = fuzz.partial_token_set_ratio(exp.lower(), gen.lower())
            logger.info(f"#Comparing: '{exp}' <-> '{gen}' → score: {score}")
            if score < threshold:
                return False
        return True

    def evaluate_response(self, resume_path, ground_truth):
        logger.info(f"Processing resume: {resume_path}")
        generated_response = main(resume_path)

        results = {
            "name": self.hard_match(ground_truth["name"], generated_response["name"]),
            "role": self.fuzzy_match(ground_truth["role"], generated_response["role"], 80),
            "summary_match": self.fuzzy_match(ground_truth["professional_summary"], generated_response["professional_summary"], 90),
            # TODO: If experience gen is 20+ and actual is 28 can i consider this as success ?
            "total_experience": self.fuzzy_match(ground_truth["total_experience"], generated_response["total_work_experience"], 90),
            "courses": self.match_records(ground_truth["courses"], generated_response["courses"], 90),
            "publications": self.match_records(ground_truth["publications"], generated_response["publications"], 90),
            # TODO: Better way to get the accomplishments
            # "accomplishments": self.match_records(ground_truth["accomplishments"], generated_response["accomplishments"], 90),
            # TODO: If 95 % skills matched correctly then success
            "skills": self.match_records(ground_truth["skills"], generated_response["skills"], 90),
            "expected_salary": self.hard_match(ground_truth["expected_salary"], generated_response["expected_salary"])
        }

        results["status"] = "success" if all(results.values()) else "fail"
        results["resume"] = os.path.basename(resume_path)
        return results
    
    
if __name__ == '__main__':
    eval = Eval()
    rows = []

    with open('ground_truth/ground_truth.json', 'r') as ground_truth:
        ground_truth = json.load(ground_truth)

    directory = 'sample_resumes'
    resumes_list = sorted(os.listdir(directory))

    for index, resume in enumerate(resumes_list[:5]):
        result = eval.evaluate_response(os.path.join(directory, resume), ground_truth[index])
        rows.append(result)

    df = pd.DataFrame(rows)
    print(df)
    df.to_csv('results/results2.csv')