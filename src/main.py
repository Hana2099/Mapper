import sys
import os
from log_parser import load_zeek_log
from log_nlp import describe_http_event
from mitre_mapper import load_mitre_techniques, map_to_technique
from visualizer import create_event_timeline
from utils.validate_log import validate_log

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import pandas as pd

log_df = validate_log_file("data/http.log")

# ✅ Step 1: Load Zeek logs
log = load_zeek_log("data/http.log")

# ✅ Step 2: Load MITRE techniques
techniques = load_mitre_techniques()

# ✅ Step 3: Loop through logs, map to MITRE
mapped_tactics = []
mapped_techniques = []

for _, row in log.iterrows():
    try:
        desc = describe_http_event(row)
        technique, score = map_to_technique(desc, techniques)
        print(f"{desc}\n → {technique['id']} {technique['name']} ({score:.2f})\n")
        mapped_tactics.append(technique['name'])
        mapped_techniques.append(technique['id'])
    except Exception as e:
        print(f"Error processing row: {e}")
        mapped_tactics.append(None)
        mapped_techniques.append(None)

# ✅ Step 4: Add to DataFrame
log["mapped_tactic"] = mapped_tactics
log["mapped_technique"] = mapped_techniques

# ✅ Step 5: Visualize (optional)
create_event_timeline(log)
