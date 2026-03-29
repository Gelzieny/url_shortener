import random
import string

from src.dependencias.supabase_client import SUPABASE_URL, SUPABASE_KEY
from supabase import create_client, ClientOptions
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import APIRouter, Depends, HTTPException
from src.dependencias.supabase_client import supabase
from src.schemas.url import URLCreate
from src.dependencias.auth_dependency import get_current_user

urls_router = APIRouter(prefix="/urls", tags=["URLs"])


def generate_short_code(length=6):
  return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


@urls_router.get("/")
def get_urls(user=Depends(get_current_user), credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
  token = credentials.credentials

  supabase_user = create_client(
    SUPABASE_URL,
    SUPABASE_KEY,
    options=ClientOptions(
        headers={
            "Authorization": f"Bearer {token}"
        }
    )
  )

  response = supabase_user.table("urls") \
    .select("*") \
    .eq("codigo_user", user.id) \
    .execute()

  return response.data

@urls_router.post("/")
def create_url(data: URLCreate, user=Depends(get_current_user), credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
  token = credentials.credentials
  short_code = generate_short_code()

  supabase_user = create_client(
    SUPABASE_URL,
    SUPABASE_KEY,
    options=ClientOptions(
      headers={
        "Authorization": f"Bearer {token}"
      }
    )
  )

  response = supabase_user.table("urls").insert({
    "original_url": data.original_url,
    "short_code": short_code,
    "is_active": True,
    "expires_at": data.expires_at,
    "codigo_user": user.id
  }).execute()

  return response.data



@urls_router.put("/{url_id}")
def update_url(
  url_id: int,
  data: URLCreate,
  credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())
):
  token = credentials.credentials

  supabase_user = create_client(
    SUPABASE_URL,
    SUPABASE_KEY,
    options=ClientOptions(
      headers={"Authorization": f"Bearer {token}"}
    )
  )

  update_data = {}

  if data.original_url is not None:
    update_data["original_url"] = data.original_url

  if data.expires_at is not None:
    update_data["expires_at"] = data.expires_at.isoformat()

  response = supabase_user.table("urls") \
    .update(update_data) \
    .eq("id", url_id) \
    .execute()

  if not response.data:
    raise HTTPException(status_code=404, detail="URL não encontrada")

  return response.data


@urls_router.delete("/{url_id}")
def delete_url(
  url_id: int,  
  credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())
):
  token = credentials.credentials

  supabase_user = create_client(
    SUPABASE_URL,
    SUPABASE_KEY,
    options=ClientOptions(
      headers={"Authorization": f"Bearer {token}"}
    )
  )

  response = supabase_user.table("urls") \
    .delete() \
    .eq("id", url_id) \
    .execute()

  if not response.data:
    raise HTTPException(status_code=404, detail="URL não encontrada")

  return {"message": "Deletado com sucesso"}