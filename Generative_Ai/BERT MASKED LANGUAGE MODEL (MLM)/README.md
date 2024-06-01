BERT Mask Language Model
This project demonstrates a Masked Language Model (MLM) using BERT (Bidirectional Encoder Representations from Transformers). It allows users to input sentences with a masked token ([MASK]), and the model predicts the most probable substitutions for the masked word.

Features:-
Interactive Interface: Utilizes Streamlit for a user-friendly web interface.
Real-time Predictions: Predicts masked words in real-time using the BERT model.
Model: Based on bert-base-uncased from Hugging Face's Transformers library.

Usage:-
Input Sentence: Write a sentence with a [MASK] token. For example: How are [MASK]?
Submit: Click the Submit button to see the predictions.
Results: The app will display the top predictions along with their respective scores.

Example:-
Input: The capital of France is [MASK].

Output:
The capital of France is Paris. (Score: 0.95)
The capital of France is Lyon. (Score: 0.02)
