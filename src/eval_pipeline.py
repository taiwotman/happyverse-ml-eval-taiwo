# ============================
#  src/eval_pipeline.py
#  Author: Taiwo O. Adetiloye
# ============================

import json
from typing import Dict

def evaluate_transcript(transcript: str, job_desc: str, questions: list) -> Dict:
    """
    Stub LLM agent to simulate scoring the transcript.
    """
    plausible_score = 2  # Very low due to made-up tech
    tech_score = 3       # High-sounding but not grounded
    comm_score = 4       # Clear speaking but full of jargon

    return {
        "plausibility": plausible_score,
        "technical_proficiency": tech_score,
        "communication": comm_score,
        "recommendation": "Strong No",
        "strengths": ["Confident tone"],
        "weaknesses": ["Overuse of technical jargon", "Unsupported claims"],
        "red_flags": ["Mentions of IPv7, Layer 8 tunneling, NAT128"]
    }

if __name__ == "__main__":
    transcript = open("assets/sample_transcript.txt").read()
    job_desc = open("assets/job_description.txt").read()
    questions = json.load(open("assets/questions.json"))
    
    result = evaluate_transcript(transcript, job_desc, questions)
    print(json.dumps(result, indent=2))