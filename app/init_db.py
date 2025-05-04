# app/init_db.py

from app.database import Base, engine
from app.models import Post

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
