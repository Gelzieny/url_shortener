from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from src.dependencias.supabase_client import supabase

security = HTTPBearer()


def get_current_user(
  credentials: HTTPAuthorizationCredentials = Depends(security),
):
  token = credentials.credentials

  try:
    user = supabase.auth.get_user(token)

    if not user or not user.user:
      raise HTTPException(status_code=401, detail="Token inválido")

    return user.user

  except Exception:
    raise HTTPException(status_code=401, detail="Não autorizado")