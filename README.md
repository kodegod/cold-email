# [EmailGenie: AI-Powered Cold Email Generator](https://cold-email-sarthi.streamlit.app/)

**[EmailGenie](https://cold-email-sarthi.streamlit.app/)** is a simple yet powerful tool designed to streamline the creation of personalized cold outreach emails for businesses, job seekers, and freelancers. By leveraging OpenAI's GPT-3.5, this project allows users to quickly generate and send professional emails tailored to their specific needs.

---

## Table of Contents
- [Project Structure](#project-structure)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
  - [Backend API](#backend-api)
  - [Frontend Interface](#frontend-interface)
- [Limitations and Future Enhancements](#limitations-and-future-enhancements)

---

## Project Structure

```plaintext
.
├── README.md                # Documentation
├── backend
│   ├── main.py              # FastAPI backend logic
│   └── profiles.db          # SQLite database for storing user profiles
└── frontend
    └── app.py               # Streamlit frontend for user interaction
```

---

## Features

1. **User Profile Management**
   - Collect user details such as name, industry, audience, and background.
   - Persist user profiles using an SQLite database.

2. **Email Generation**
   - Use OpenAI's GPT-3.5 to generate highly personalized emails.
   - Customize templates and placeholders to fit different scenarios.

3. **Email Sending**
   - Use Python’s SMTP library to send emails without relying on external services.

4. **Intuitive Web Interface**
   - Powered by Streamlit, users can manage profiles, generate emails, and send them with ease.

---

## Technologies Used

- **Backend**: FastAPI, SQLite, SQLAlchemy
- **Frontend**: Streamlit
- **AI Integration**: OpenAI's GPT-3.5
- **Email Service**: Python's `smtplib`

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-repo/cold-email.git
cd cold-email
```

### 2. Install Dependencies

- **Backend:**
  ```bash
  cd backend
  pip install fastapi uvicorn openai sqlalchemy python-dotenv
  ```

- **Frontend:**
  ```bash
  cd ../frontend
  pip install streamlit requests
  ```

### 3. Environment Variables

Create a `.env` file in the `backend/` directory with the following:

```env
OPENAI_API_KEY=your-openai-api-key
```

### 4. Run the Application

- **Backend:**
  ```bash
  cd backend
  uvicorn main:app --reload
  ```

- **Frontend:**
  ```bash
  cd ../frontend
  streamlit run app.py
  ```

---

## Usage

### Backend API

#### Base URL
`http://localhost:8000`

#### Endpoints

- **`GET /`**  
  Health check endpoint.  
  **Response:**
  ```json
  {"message": "Welcome to EmailGenie Backend"}
  ```

- **`POST /generate-email/`**  
  Generate a personalized email.  
  **Request Body:**
  ```json
  {
    "profile": {
      "name": "John Doe",
      "industry": "Software",
      "audience": "Tech Startups",
      "background": "Experienced software developer."
    },
    "template": "Sales Pitch",
    "placeholders": {"Name": "John", "Industry": "Software"},
    "custom_message": "Looking forward to collaborating with your team."
  }
  ```
  **Response:**
  ```json
  {
    "email": "Dear Sir/Madam, I am reaching out regarding..."
  }
  ```

- **`POST /send-email/`**  
  Send the generated email.  
  **Request Body:**
  ```json
  {
    "email": "Generated email content",
    "recipient": "recipient@example.com"
  }
  ```
  **Response:**
  ```json
  {
    "status": "Email sent successfully!"
  }
  ```

### Frontend Interface

1. **Profile Setup**
   - Enter name, industry, audience, and background details.
   - Click **Save Profile** to store the information.

2. **Generate Email**
   - Choose a template (e.g., Sales Pitch, Job Application).
   - Add custom placeholders and messages.
   - Click **Generate Email** to see the AI-generated content.

3. **Send Email**
   - Enter the recipient's email address.
   - Click **Send Email** to deliver the generated message.

---
