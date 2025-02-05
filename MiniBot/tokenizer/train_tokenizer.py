import os
from tokenizers import ByteLevelBPETokenizer

tokenizer = ByteLevelBPETokenizer()
tokenizer.train(["../data/csharp_dataset.json"], vocab_size=50000, min_frequency=2)

# Define the directory path
output_dir = "csharp_tokenizer"

# Create the directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Save the model
tokenizer.save_model(output_dir)