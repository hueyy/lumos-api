import os
import dotenv

dotenv.load() # remove in deployment

FIREBASE_CONFIG = {
    "apiKey": os.environ.get("FIREBASE_API_KEY"),
    "authDomain": os.environ.get("FIREBASE_AUTH_DOMAIN"),
    "databaseURL": os.environ.get("FIREBASE_DATABASE_URL"),
    "storageBucket": os.environ.get("FIREBASE_STORAGE_BUCKET"),
}