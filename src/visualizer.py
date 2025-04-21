import pandas as pd
import plotly.express as px

def create_event_timeline(log_df: pd.DataFrame, tactic_column: str = "mapped_tactic"):
    # Convert timestamps
    log_df["ts"] = pd.to_datetime(log_df["ts"], unit="s", errors="coerce")

    # Basic cleaning
    log_df = log_df.dropna(subset=["ts", tactic_column])

    # Use unique ID for each row
    log_df["event"] = log_df["ts"].astype(str) + " - " + log_df[tactic_column]

    fig = px.timeline(
        log_df,
        x_start="ts",
        x_end="ts",
        y="id.orig_h",  # source IP
        color=tactic_column,
        hover_data=["event", "id.resp_h", "method", "host"],
        title="Mapped Zeek Events to MITRE ATT&CK"
    )
    fig.update_yaxes(autorange="reversed")
    fig.update_layout(height=600, margin={"l": 40, "r": 40, "t": 50, "b": 40})
    fig.show()
