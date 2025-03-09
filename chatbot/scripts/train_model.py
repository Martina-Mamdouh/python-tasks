from transformers import Trainer, TrainingArguments
from load_model import load_model
from prepare_data import prepare_data

def train_model():
    # Load model and tokenizer
    model, tokenizer = load_model()

    # Load and preprocess dataset
    tokenized_dataset = prepare_data()

    # Set training arguments
    training_args = TrainingArguments(
        output_dir="./results",                  # Output directory for results             # Evaluate at regular intervals
        eval_steps=500,                          # Evaluate every 500 steps
        save_steps=500,                          # Save checkpoint every 500 steps
        logging_steps=100,                       # Log every 100 steps
        learning_rate=2e-5,                      # Learning rate
        per_device_train_batch_size=8,           # Batch size for training
        per_device_eval_batch_size=8,            # Batch size for evaluation
        num_train_epochs=3,                      # Number of training epochs
        weight_decay=0.01,                       # Weight decay for regularization
        save_total_limit=3,                      # Keep only 3 checkpoints
        load_best_model_at_end=True,             # Load the best model at the end of training
        evaluation_strategy="epoch"              # Evaluate at the end of each epoch
    )

    # Initialize Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset["train"],
        eval_dataset=tokenized_dataset["test"]
    )

    # Train the model
    trainer.train()

    # Save the fine-tuned model and tokenizer
    model.save_pretrained("./fine_tuned_model")
    tokenizer.save_pretrained("./fine_tuned_model")

if __name__ == "__main__":
    train_model()
