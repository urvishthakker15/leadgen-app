# Lead Management System

## Overview

This application is designed to handle lead creation, status updates, and retrieval of all leads. Prospects can submit their information and resumes, and attorneys can update lead statuses and access lead details.

## Assumptions

1. **Email Client**: The program currenlty assumes the email client used in smtp is a gmail based client. 


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

### Testing

1. **Run Tests**:
- Ensure JUnit 5 is in your classpath.
- Run the tests using:
```bash
java -cp "out/production/illumio:out/test/illumio:lib/junit-platform-console-standalone-1.8.2.jar" org.junit.platform.console.ConsoleLauncher --scan-classpath
```

### Configuration

Before running the program, ensure the following files are in the correct locations:
- `src/protocol-numbers.csv`: CSV file containing protocol number mappings
- `src/lookup.txt`: Lookup table for port and protocol to tag mapping
- `src/flow_logs.txt`: Input flow logs to be processed

The program will generate an `output.txt` file in the `src` directory with the results.

### What Would I Have Done With More Time

1. **Enhanced Error Handling**: Implement additional error handling to manage invalid input formats, missing files, and other edge cases more gracefully.
2. **Testing**: I would have added more robust error handling, and covered more edge cases. Also, tested program more comprehensively by testing all functionality (business logic).
3. **Extended Log Format Support**: Implement support for additional log formats or versions if needed.
3. **Optimization**: Optimize the performance of the parsing and processing logic to handle larger files more efficiently.
4. **User Interface**: Develop a user interface (CLI or graphical) to make it easier to interact with the tool and visualize the results.
5. **Documentation**: Add more comprehensive documentation, including detailed descriptions of the configuration options and usage examples.


