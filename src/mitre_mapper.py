from sentence_transformers import SentenceTransformer, util
import json

model = SentenceTransformer("all-mpnet-base-v2")

def load_mitre_techniques(json_path="data/enterprise-attack.json"):
    with open(json_path, "r") as f:
        data = json.load(f)
    techniques = []
    for obj in data["objects"]:
        if obj.get("type") == "attack-pattern":
            techniques.append({
                "id": obj.get("external_references", [{}])[0].get("external_id", ""),
                "name": obj.get("name"),
                "description": obj.get("description")
            })
    return techniques

def map_to_technique(description, technique_list):
    input_embedding = model.encode(description, convert_to_tensor=True)
    candidates = [t["description"] for t in technique_list]
    candidate_embeddings = model.encode(candidates, convert_to_tensor=True)

    scores = util.pytorch_cos_sim(input_embedding, candidate_embeddings)[0]
    top_idx = scores.argmax().item()
    return technique_list[top_idx], scores[top_idx].item()
