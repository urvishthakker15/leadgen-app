# Lead Management System

## Overview

This application is designed to handle lead creation, status updates, and retrieval of all leads. Prospects can submit their information and resumes, and attorneys can update lead statuses and access lead details.

## Assumptions

1. **Email Client**: The program currenlty assumes the email client used in smtp is a gmail based client.
2. **PDF size restrictions**: The program assumes there is no file size limitation (In reality we would like to restrict that).
3. **Scalability and deployment**: The current implementation is does not account for scalability and production deployment usecase in terms of optimising database queries, calls, etc.

## Instructions

### Compiling and Running the Program

1. **Clone the Repository**:
```bash
git clone https://github.com/urvishthakker15/leadgen.git
```

2. **Install poetry dependencies**:
```bash
poetry install
poetry shell
```

3. **Initialize the Database Tables**:
```bash
python app/db/initialize_db.py 
```

4. **Populate the environment variables**:
```bash
DATABASE_URL=sqlite+aiosqlite:///./leads.db
SYNC_DATABASE_URL=sqlite:///./leads.db
API_KEY=8d9f3e4c0e69f0a7d8b3c2198d574f72e7cba563b52fdab3450c2e2a44dca7ff
SMTP_USERNAME="personal-email@gmail.com" (Your gmail email)
SMTP_PASSWORD="app-password" (Create App password in gmail and enter here)
```

5. **Run the Application**:
```bash
uvicorn app.main:app --reload --env-file=app/.env 
```

### What Would I Have Done With More Time

1. **Enhanced Error Handling**: Implement additional error handling to manage invalid input formats, missing files, and other edge cases more gracefully. Return as precise error as possible compared to very generic error being returned in case of any failure or input issue. 
2. **Testing**: I would have added more robust error handling, and covered more edge cases. Also, tested program more comprehensively by adding robust unit tests, integration test.
3. **CI/CD**: I would have introduced linters, code formatters, CI checks and CD pipeline if I had more time. 
4. **Logging**: Implement logging.
5. **Database**: I would have implemented a PostgreSQL instead of sqlite. Also, use Amazon S3 to store resume. 
6. **Tools**: I would have leveraged Amazon SES and alike frameworks for email communication instead of relying on smtp protocol.  
7. **Documentation**: Add more comprehensive documentation, including detailed descriptions of the configuration options and usage examples.


