 # Proactive Failure Detection using RabbitMQ, Gemini LLM, and Log Analysis

 This project demonstrates a proactive failure detection system that analyzes log messages for critical errors using RabbitMQ, Gemini LLM, and other technologies. The system aims to identify potential failures before they impact the overall application stability.

 ## Technology Stack

 *   **RabbitMQ:** A message broker that facilitates asynchronous communication between different components of the system. Log messages are published to RabbitMQ for processing.
 *   **Gemini LLM:** A large language model used to analyze log messages and identify critical errors based on predefined patterns and severity levels.
 *   **Python:** The primary programming language used for developing the log analysis and failure detection components.
 ## Flow
 1.  **Message Consumption:** A consumer application (written in Python) subscribes to the RabbitMQ exchange and receives log messages.
 2.  **Log Analysis:** The consumer application uses the Gemini LLM to analyze the log message content and identify potential errors or critical events.
 3.  **Failure Detection:** Based on the analysis results, the system determines if a potential failure is detected. This may involve checking for specific keywords, error codes, or patterns in the log message.
 4.  **Alerting:** If a potential failure is detected, the system sends an alert to the appropriate team via an alerting system .
 