import time
import uuid
from typing import Any, Dict, Optional

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


# ---- Dependencies ----
def get_tenant() -> str:
    """Stub for tenant resolution. Extend later with real auth/tenancy."""
    return "public"


# ---- Models ----
class InvokeRequest(BaseModel):
    input: str = Field(..., description="User message or task")
    params: Optional[Dict[str, Any]] = Field(
        default=None, description="Optional overrides for model/config"
    )


class InvokeResponse(BaseModel):
    run_id: str
    agent: str
    output: Dict[str, Any]
    meta: Dict[str, Any]


# ---- App Factory ----
def create_app() -> FastAPI:
    app = FastAPI(title="GenAI Scaffolding Pro API", version="0.1.0")

    # CORS (loose now, tighten for prod)
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
        """
        Placeholder invoke. Echoes input and returns structured metadata.
        Later replace with graph execution + verify layers.
        """
        if not req.input.strip():
            raise HTTPException(status_code=400, detail="Empty input")

        run_id = f"{int(time.time())}-{uuid.uuid4().hex[:8]}"

        draft = {
            "message": f"Agent '{name}' received your input",
            "echo": req.input,
            "citations": [],
        }

        meta = {
            "tenant": tenant,
            "model": req.params.get("model") if req.params else "gpt-5-mini",
            "tokens": {"input": len(req.input), "output": 50},
        }

        return InvokeResponse(run_id=run_id, agent=name, output=draft, meta=meta)

    return app
