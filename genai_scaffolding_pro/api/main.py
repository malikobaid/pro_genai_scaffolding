import time
import uuid
from typing import Any, Dict, Optional

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from genai_scaffolding_pro.config import settings
from genai_scaffolding_pro.graph.executor import run_graph


def get_tenant() -> str:
    return "public"


class InvokeRequest(BaseModel):
    input: str = Field(..., description="User message or task")
    params: Optional[Dict[str, Any]] = Field(
        default=None, description="Optional model/config overrides"
    )


class InvokeResponse(BaseModel):
    run_id: str
    agent: str
    output: Dict[str, Any]
    meta: Dict[str, Any]


def create_app() -> FastAPI:
    app = FastAPI(title="GenAI Scaffolding Pro API", version="0.1.0")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/health")
    def health() -> Dict[str, str]:
        return {"status": "ok"}

    @app.post("/v1/agents/{name}/invoke", response_model=InvokeResponse)
    def invoke_agent(
        name: str, req: InvokeRequest, tenant: str = Depends(get_tenant)
    ) -> InvokeResponse:
        if not req.input.strip():
            raise HTTPException(status_code=400, detail="Empty input")
        run_id = f"{int(time.time())}-{uuid.uuid4().hex[:8]}"
        # Merge defaults
        params = {"model": settings.model_default, **(req.params or {})}
        result = run_graph(req.input, params)
        draft = {
            "message": result["message"],
            "echo": req.input,
            "final": result["final"],
            "plan": result["plan"],
            "verified": result["verified"],
            "citations": result["citations"],
        }
        meta = {
            "tenant": tenant,
            "model": params.get("model"),
            "tokens": {"input": len(req.input), "output": 50},
            "env": settings.env,
        }
        return InvokeResponse(run_id=run_id, agent=name, output=draft, meta=meta)

    return app
