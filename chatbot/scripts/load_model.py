from transformers import MT5ForConditionalGeneration, MT5Tokenizer

def load_model():
    # Load pre-trained mT5 model and tokenizer
    model = MT5ForConditionalGeneration.from_pretrained("google/mt5-large", trust_remote_code=True)
    tokenizer = MT5Tokenizer.from_pretrained("google/mt5-large", trust_remote_code=True)
    return model, tokenizer