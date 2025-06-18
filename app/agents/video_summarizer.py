from google.adk.agents import LlmAgent
from ..tools.video_loader import VideoFrameTool
# from ..callbacks import quota_guard  # Comment out temporarily
from ..settings import MODEL_NAME, MAX_TOKENS

SURVEILLANCE_PROMPT = """You are a surveillance detection system. 

When you receive a message with a video path, immediately call the extract_video_frames function using the provided path.

Look for "VIDEO_PATH=" in the message and use that exact path.

After extracting frames, analyze them and provide:

1. A chronological summary of events visible in the video
2. Identify any potential threats to humans, animals, or environment  
3. Analyze each frame for: events, actions, objects, and background

4. Calculate a risk score using the formula: Risk = Hazard × Exposure × Vulnerability

Where:
- Hazard: The potential threat or event that could cause harm (1-10)
- Exposure: The extent to which people/assets are in contact with the hazard (1-10)
- Vulnerability: The susceptibility of exposed people/assets to suffer harm (1-10)

Provide your analysis in this format:
SUMMARY: [chronological description]
THREATS: [identified threats]
HAZARD: [score 1-10]
EXPOSURE: [score 1-10]
VULNERABILITY: [score 1-10]
RISK_SCORE: [Hazard × Exposure × Vulnerability]
"""


video_summarizer = LlmAgent(
    name="VideoSummarizer",
    model=MODEL_NAME,
    instruction=SURVEILLANCE_PROMPT,
    tools=[VideoFrameTool]
    # before_model_callback=quota_guard,  # Comment out temporarily
)
