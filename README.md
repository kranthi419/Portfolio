# Kavali Kranthi Kumar Portfolio
![image](https://github.com/user-attachments/assets/f79c112e-a1d5-4779-aa2a-d333f2d6c7ee)

This is a portfolio web application for Kavali Kranthi Kumar, built using Streamlit. The application showcases various sections including an introduction, resume, projects, and a chatbot feature powered by OpenAI's GPT.

## Features

- **Introduction**: A brief introduction about Kavali Kranthi Kumar.
- **Resume**: View the resume of Kavali Kranthi Kumar.
- **Projects**: Display the expertise and projects.
- **Chatbot**: An interactive chatbot powered by OpenAI's GPT for answering questions related to the resume.
- **Email Form**: A form to send emails directly from the application.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/kranthi-jayanth/portfolio.git
    cd portfolio
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add the following environment variables:
    ```dotenv
    OPENAI_API_KEY="your_openai_api_key"
    EMAIL="your_email@example.com"
    EMAIL_PASSWORD="your_email_password"
    ```

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

2. Open your web browser and navigate to `http://localhost:8501`.

## File Structure

- `app.py`: Main application file.
- `utils/email_util.py`: Utility functions for sending emails.
- `chatbot/qa_agent.py`: Functions for handling the chatbot interactions.
- `constants.py`: Contains constant values used in the application.
- `app_pages/`: Directory containing different pages of the application.

## Dependencies

- Python 3.8+
- Streamlit
- OpenAI
- smtplib
- dotenv

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any inquiries, please contact Kavali Kranthi Kumar at:
- Email: kavalikranthikumar3@gmail.com
- Phone: +91-9505530176

---

Feel free to contribute to this project by submitting issues or pull requests.
