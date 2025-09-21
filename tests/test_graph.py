from genai_scaffolding_pro.graph.executor import run_graph


def test_run_graph_basic() -> None:
    out = run_graph("Find the summary", {"model": "gpt-5-mini"})
    assert out["verified"] is True
    assert "Plan for:" in out["plan"]
    assert out["final"] != ""
