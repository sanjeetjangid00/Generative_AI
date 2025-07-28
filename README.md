------------
## Sentiment Analysis with Google Gemini Pro
------------
### App Link - https://sentiment-analysis-with-gemini-flash.streamlit.app/
----------
#### NOTE: At the first time, it will display "This app has gone to sleep due to inactivity. Would you like to wake it back up? Yes, get this app back up!" Then click on the "Yes, get this app back up!" button.

![Sentiment Analysis](https://github.com/user-attachments/assets/feb17c69-08e6-4a7a-a2d0-26e040579345)

This project demonstrates a Sentiment Analysis application using Google's Generative AI (Gemini Pro). Users can input text to receive AI-generated responses indicating whether the sentiment is positive or negative.

#### Features
+ Interactive Interface: Utilizes Streamlit for a user-friendly web interface.
+ Real-time Sentiment Analysis: Analyzes the sentiment of user queries in real-time using the Google Gemini Pro model.
+ Center-aligned Title: A visually appealing title indicating the purpose of the application.

#### Usage
+ Input Query: Type your question or statement in the text input box.
+ Submit: Click the **Response** button to get the sentiment analysis.
+ Results: The app will display the user's input and the AI's sentiment analysis response.

#### Example
+ Input: I love this new phone!
+ Output:
User: I love this new phone!
Gemini: The sentiment is positive.

#### Dependencies
+ google-generativeai
+ streamlit
+ Configuration
Ensure you have a valid API key for Google Generative AI. Replace the placeholder YOUR_GOOGLE_API_KEY in the code with your actual API key.

#### Acknowledgments
+ Google Generative AI: For providing the Gemini Pro model.
+ Streamlit: For the easy-to-use web application framework.
