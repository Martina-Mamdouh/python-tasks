from datasets import load_dataset
from transformers import MT5Tokenizer
from transformers import AutoTokenizer
from datasets import DownloadConfig
import datasets
import fsspec
def prepare_data():
    # Load the mT5 tokenizer
    fs = fsspec.filesystem('http', timeout=300)

# Now use the filesystem to download the file
    with fs.open('http://example.com/largefile.zip', 'rb') as f:
        data = f.read()
    tokenizer = AutoTokenizer.from_pretrained("google/mt5-small", clean_up_tokenization_spaces=False)
    download_config = DownloadConfig(
    extract_compressed_file=False,
     
)
    # Load CC100 dataset (multilingual)
    dataset_ar = load_dataset('cc100', 'ar', trust_remote_code=True, download_config=download_config,download_mode=datasets.download.DownloadMode.FORCE_REDOWNLOAD)
    dataset_en = load_dataset('cc100', 'en', trust_remote_code=True, download_config=download_config, download_mode=datasets.download.DownloadMode.FORCE_REDOWNLOAD)

    # Combine the datasets into one
    dataset = dataset_ar['train'].add_column("text", dataset_en['train']['text'])

    # Create a conversation dataset from CC100, ensure input-output pairs are structured
    def create_conversational_pairs(dataset):
        conversational_pairs = {
            'input': [],
            'output': []
        }
        for item in dataset:
            # Split dataset into questions (input) and answers (output)
            question = item['text'][:len(item['text']) // 2]  # use the first half as the question
            answer = item['text'][len(item['text']) // 2:]    # use the second half as the answer
            conversational_pairs['input'].append(question)
            conversational_pairs['output'].append(answer)
        return conversational_pairs

    # Process the dataset and generate conversation pairs
    conversational_pairs = create_conversational_pairs(dataset['train'])

    # Tokenization function for input and output pairs
    def tokenize_function(examples):
        # Tokenize inputs (user questions)
        inputs = tokenizer(examples['input'], max_length=128, truncation=True, padding="max_length")
        # Tokenize outputs (bot responses)
        targets = tokenizer(examples['output'], max_length=128, truncation=True, padding="max_length")
        # Add labels (target IDs) to the inputs
        inputs['labels'] = targets['input_ids']
        return inputs

    # Convert to datasets compatible format
    tokenized_dataset = dataset.map(tokenize_function, batched=True)

    # Split dataset into train (80%) and validation (20%) sets
    tokenized_dataset = tokenized_dataset.train_test_split(test_size=0.2)

    return tokenized_dataset
