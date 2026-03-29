from fastapi import APIRouter, Depends, HTTPException
from src.schemas.user import UserCreate, UserLogin
from src.dependencias.supabase_client import supabase
from src.dependencias.auth_dependency import get_current_user

auth_router = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.post("/register")
def register(user: UserCreate):
  try:
    response = supabase.auth.sign_up({
      "email": user.email,
      "password": user.password
    })

    return {
      "message": "Usuário registrado com sucesso",
      "user": response.user
    }

  except Exception as e:
    raise HTTPException(status_code=400, detail=str(e))


@auth_router.post("/login")
def login(user: UserLogin):
  try:
    response = supabase.auth.sign_in_with_password({
      "email": user.email,
      "password": user.password
    })

    return {
      "access_token": response.session.access_token,
      "refresh_token": response.session.refresh_token,
      "user": response.user
    }

  except Exception as e:
      raise HTTPException(status_code=401, detail="Credenciais inválidas")


@auth_router.get("/profile")
def profile(user=Depends(get_current_user)):
  return {
    "message": "Usuário autenticado ✅",
    "user": user
  }