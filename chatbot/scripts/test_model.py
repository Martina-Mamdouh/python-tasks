from transformers import MT5Tokenizer, MT5ForConditionalGeneration
import torch

def test_model():
    # Load the fine-tuned model and tokenizer
    model = MT5ForConditionalGeneration.from_pretrained("./fine_tuned_model")
    tokenizer = MT5Tokenizer.from_pretrained("./fine_tuned_model")

    while True:
        # Get input from the user
        input_text = input("User: ")
        if input_text.lower() == "exit":
            break

        # Tokenize the input
        input_ids = tokenizer.encode(input_text, return_tensors="pt")

        # Generate a response
        outputs = model.generate(input_ids)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Print the bot's response
        print(f"Bot: {response}")

if __name__ == "__main__":
    test_model()
