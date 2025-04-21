from log_parser import load_zeek_log
from log_nlp import describe_http_event
from mitre_mapper import load_mitre_techniques, map_to_technique
from visualizer import create_event_timeline

# Assume you've added "mapped_tactic" and "mapped_technique" to the dataframe
# You can collect them like this:
tactics, techniques = [], []

for _, row in log.iterrows():
    desc = describe_http_event(row)
    technique, score = map_to_technique(desc, techniques)
    tactics.append(technique["name"])  # or extract tactic from MITRE mapping
    techniques.append(technique["id"])

log["mapped_tactic"] = tactics
log["mapped_technique"] = techniques

# Visualize it!
create_event_timeline(log)

log = load_zeek_log("data/http.log")
techniques = load_mitre_techniques()

for _, row in log.iterrows():
    desc = describe_http_event(row)
    technique, score = map_to_technique(desc, techniques)
    print(f"{desc}\n → {technique['id']} {technique['name']} ({score:.2f})\n")
