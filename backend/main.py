from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv
from mailjet_rest import Client

import os

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# OpenAI API Key Setup
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

MAILJET_API_KEY = os.getenv("MAILJET_API_KEY")
MAILJET_API_SECRET = os.getenv("MAILJET_API_SECRET")

mailjet = Client(auth=(MAILJET_API_KEY, MAILJET_API_SECRET), version="v3.1")

# Request Models
class EmailRequest(BaseModel):
    profile: dict  # User details: industry, background, audience
    template: str  # Selected email template
    placeholders: dict  # Dynamic placeholders
    custom_message: str  # Additional content

class SendEmailRequest(BaseModel):
    email: str
    recipient: str

@app.get("/")
def read_root():
    return {"message": "Welcome to EmailGenie Backend"}

@app.post("/generate-email/")
def generate_email(request: EmailRequest):
    try:
        # Prompt engineering for OpenAI LLM
        prompt = f"""
        You are an expert in writing effective cold outreach emails.
        Generate an email using the following profile details:
        {request.profile}. Use this template:
        {request.template}. Fill in placeholders: {request.placeholders}.
        Include this custom message: {request.custom_message}.
        """
        # OpenAI LLM Call
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": prompt}]
        )
        email_content = response["choices"][0]["message"]["content"]
        return {"email": email_content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Database setup
DATABASE_URL = "sqlite:///./profiles.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define User Profile Model
class UserProfile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    industry = Column(String)
    audience = Column(String)
    background = Column(String)

# Create database tables
Base.metadata.create_all(bind=engine)