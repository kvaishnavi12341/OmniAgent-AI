from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import time

from app.workflows.orchestrator import Orchestrator
from app.utils.rbac import RBAC

# --- APP INIT ---
app = FastAPI(title="OmniAgent AI API", version="1.0.0")

orch = Orchestrator()
rbac = RBAC()

# --- REQUEST MODEL ---
class RequestBody(BaseModel):
    input: str


# --- PROCESS ENDPOINT ---
@app.post("/process")
def process(req: RequestBody):
    try:
        if not rbac.check_access("write"):
            return {"error": "Unauthorized"}

        return orch.process(req.input)

    except Exception as e:
        print("PROCESS ERROR:", e)
        return {"error": str(e)}


# --- RATE LIMIT STORAGE ---
request_log = {}

# --- SECURITY MIDDLEWARE ---
@app.middleware("http")
async def security_middleware(request: Request, call_next):
    try:
        client_ip = request.client.host if request.client else "unknown"

        now = time.time()
        window = 10
        limit = 5

        request_log.setdefault(client_ip, [])
        request_log[client_ip] = [
            t for t in request_log[client_ip] if now - t < window
        ]

        if len(request_log[client_ip]) >= limit:
            return JSONResponse(
                status_code=429,
                content={"error": "Too many requests"}
            )

        request_log[client_ip].append(now)

        if request.method in ["POST", "PUT", "PATCH"]:
            body = await request.body()
            if len(body) > 1000:
                return JSONResponse(
                    status_code=400,
                    content={"error": "Input too large"}
                )

        response = await call_next(request)
        return response

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )


# --- CHAT ENDPOINT ---
@app.post("/chat")
async def chat(data: dict):
    try:
        if not data or "message" not in data:
            return {"error": "Missing 'message'"}

        message = data["message"]

        if not isinstance(message, str) or not message.strip():
            return {"error": "Invalid message"}

        if len(message) > 500:
            return {"error": "Message too long"}

        result = orch.process(message)

        return {
            "status": "success",
            "response": result
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


# --- HEALTH CHECK ---
@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "OmniAgent AI",
        "version": "1.0.0"
    }
'''
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.workflows.orchestrator import Orchestrator
import time
from app.utils.rbac import RBAC
from pydantic import BaseModel

# --- APP INIT ---
app = FastAPI(title="OmniAgent AI API", version="1.0.0")
orch = Orchestrator()
rbac = RBAC()


class RequestBody(BaseModel):
    input: str

@app.post("/process")
def process(req: RequestBody):
    if not rbac.check_access("write"):
        raise Exception("Unauthorized")

    return orch.process(req.input)

# --- RATE LIMIT STORAGE (IN-MEMORY) ---
request_log = {}

# --- SECURITY MIDDLEWARE ---
@app.middleware("http")
async def security_middleware(request: Request, call_next):
    try:
        client_ip = request.client.host if request.client else "unknown"

        # --- RATE LIMIT (5 requests / 10 sec per IP) ---
        now = time.time()
        window = 10
        limit = 5

        request_log.setdefault(client_ip, [])
        request_log[client_ip] = [
            t for t in request_log[client_ip] if now - t < window
        ]

        if len(request_log[client_ip]) >= limit:
            return JSONResponse(
                status_code=429,
                content={"error": "Too many requests"}
            )

        request_log[client_ip].append(now)

        # --- INPUT SIZE VALIDATION ---
        if request.method in ["POST", "PUT", "PATCH"]:
            body = await request.body()
            if len(body) > 1000:
                return JSONResponse(
                    status_code=400,
                    content={"error": "Input too large"}
                )

        response = await call_next(request)
        return response

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e).encode("utf-8", "ignore").decode()}
        )


# --- CHAT ENDPOINT ---
@app.post("/chat")
async def chat(data: dict):
    try:
        # --- VALIDATION ---
        if not data or "message" not in data:
            return {"error": "Missing 'message' field"}

        message = data["message"]

        if not isinstance(message, str) or not message.strip():
            return {"error": "Invalid message"}

        if len(message) > 500:
            return {"error": "Message too long"}

        # --- PROCESS THROUGH ORCHESTRATOR ---
        result = orch.process(message)

        return {
            "status": "success",
            "response": result
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


# --- HEALTH CHECK ---
@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "OmniAgent AI",
        "version": "1.0.0"
    }
'''