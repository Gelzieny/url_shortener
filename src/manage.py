import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

app = FastAPI(
  title="Shortify API",
  description=""
)

# --- Rota de Redirecionamento da Raiz para a Documentação ---
@app.get("/", include_in_schema=False)
async def redirect_to_docs():
  return RedirectResponse(url="/docs")

@app.get("/monitor", tags=["Health"])
async def statusaplicacao():
  return True