import os
import streamlit as st
from supabase import create_client

SUPABASE_URL = st.secrets.get("SUPABASE_URL") or os.getenv("SUPABASE_URL")
SUPABASE_KEY = st.secrets.get("SUPABASE_KEY") or os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise RuntimeError("Faltan SUPABASE_URL y SUPABASE_KEY en secrets o variables de entorno.")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
