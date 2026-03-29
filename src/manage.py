import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from src.routes.url import urls_router
from src.routes.auth import  auth_router

app = FastAPI(
  title="Shortify API",
  description=""
)

app.include_router(auth_router)
app.include_router(urls_router)

# --- Rota de Redirecionamento da Raiz para a Documentação ---
@app.get("/", include_in_schema=False)
async def redirect_to_docs():
  return RedirectResponse(url="/docs")

@app.get("/monitor", tags=["Health"])
async def statusaplicacao():
  return True