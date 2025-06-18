from google.adk.agents import LlmAgent
from ..callbacks import quota_guard
from ..settings import MODEL_NAME

CLASSIFICATION_PROMPT = """You are a threat classification system. Analyze the provided surveillance summary and classify the threat level.

WEAPON DETECTION RULES (CRITICAL):
- If analysis mentions "gun", "firearm", "weapon", "knife", "armed": MINIMUM score 75
- If "pointing gun", "brandishing", "threatening with weapon": MINIMUM score 85
- If risk score > 500: MINIMUM score 70
- If hazard score = 10: MINIMUM score 80

CLASSIFICATION RULES:
- THREAT_SCORE 80-100: Assault (weapons/violence)
- THREAT_SCORE 60-79: Abuse (aggressive behavior)
- THREAT_SCORE 40-59: Arrest (police involvement)
- THREAT_SCORE 20-39: Normal (minor incidents)
- THREAT_SCORE 0-19: Normal (no threat)

SPECIAL OVERRIDES:
- Police outside jail/station = Arrest
- Wheelchair person = +10 to vulnerability
- Multiple weapons = +15 to score

Read the entire analysis carefully. Look for weapon keywords and high risk scores.

Respond ONLY in this exact format:
THREAT_SCORE: [number]
CLASSIFICATION: [Abuse|Assault|Arson|Arrest|Normal]"""



threat_classifier = LlmAgent(
    name="ThreatClassifier", 
    model=MODEL_NAME,
    instruction=CLASSIFICATION_PROMPT,
    before_model_callback=quota_guard
)

