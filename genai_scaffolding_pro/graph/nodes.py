from typing import Any, Dict


def plan_node(state: Dict[str, Any]) -> Dict[str, Any]:
    state["plan"] = f"Plan for: {state['input']}"
    return state


def act_node(state: Dict[str, Any]) -> Dict[str, Any]:
    state["draft"] = f"Draft answer to: {state['input']}"
    return state


def verify_node(state: Dict[str, Any]) -> Dict[str, Any]:
    state["verified"] = True
    state["final"] = state.get("draft", "")
    return state
