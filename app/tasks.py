import requests
from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy.orm import Session
from app.database import SessionLocal, get_db
from app import models
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        db = SessionLocal()

        try:
            for item in data:
                #check data in db
                existing = db.query(models.Post).filter_by(id=item["id"]).first()
                if not existing:
                    post = models.Post(
                        # id=item["id"],
                        title=item["title"],
                        body=item["body"],
                        # userId=item["userId"]
                    )
                    db.add(post)
                    db.commit()
  
            logger.info(f"Fetched {len(data)} posts.")
        except Exception as e:
            db.rollback()
            logger.error(f"Error while fetching data: {e}")
        finally:
            db.close()
    else:
         logger.error("Failed to fetch data.")

def schedule_tasks():
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_data, "interval", minutes=1)
    scheduler.start()
    logger.info("Schedular start")


