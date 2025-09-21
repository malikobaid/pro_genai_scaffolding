from typing import Any, Callable, Dict, List

from .nodes import act_node, plan_node, verify_node

Pipeline = List[Callable[[Dict[str, Any]], Dict[str, Any]]]


def run_graph(input_text: str, params: Dict[str, Any] | None = None) -> Dict[str, Any]:
    state: Dict[str, Any] = {"input": input_text, "params": params or {}}
    pipeline: Pipeline = [plan_node, act_node, verify_node]
    for fn in pipeline:
        state = fn(state)
    return {
        "message": "OK",
        "final": state["final"],
        "plan": state["plan"],
        "verified": state["verified"],
        "citations": [],
    }
