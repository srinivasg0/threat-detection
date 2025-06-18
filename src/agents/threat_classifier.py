from google.adk.agents import LlmAgent
from ..callbacks import quota_guard
from ..settings import MODEL_NAME

CLASSIFICATION_PROMPT = """You are a threat classification system. Analyze the provided surveillance summary and classify the threat level.

IMPORTANT: Use the RISK_SCORE from the surveillance summary directly as the THREAT_SCORE. The RISK_SCORE is already in the 0-100 range.

Your job is to:
1. Read the surveillance summary carefully
2. Extract the existing risk scores (HAZARD, EXPOSURE, VULNERABILITY, RISK_SCORE)
3. Use the RISK_SCORE directly as the THREAT_SCORE
4. Provide a threat classification based on the THREAT_SCORE

CLASSIFICATION RULES:
- THREAT_SCORE 80-100: Assault (weapons/violence)
- THREAT_SCORE 60-79: Abuse (aggressive behavior)
- THREAT_SCORE 40-59: Arrest (police involvement)
- THREAT_SCORE 20-39: Normal (minor incidents)
- THREAT_SCORE 0-19: Normal (no threat)

SPECIAL CLASSIFICATIONS:
- Police outside jail/station = Arrest
- Wheelchair person = Consider vulnerability in classification
- Multiple weapons = Assault classification

Respond ONLY in this exact format:
THREAT_SCORE: [use the RISK_SCORE from the surveillance summary]
CLASSIFICATION: [Abuse|Assault|Arson|Arrest|Normal]"""



threat_classifier = LlmAgent(
    name="ThreatClassifier", 
    model=MODEL_NAME,
    instruction=CLASSIFICATION_PROMPT,
    before_model_callback=quota_guard
)

