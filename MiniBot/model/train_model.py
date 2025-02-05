from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments
from datasets import load_dataset
from transformers import DataCollatorForLanguageModeling

# Tải dữ liệu
dataset = load_dataset("json", data_files="data\\csharp_dataset.json")

# Tiền xử lý dữ liệu
def tokenize_function(examples):
    return tokenizer(examples['text'], return_tensors="pt", padding="max_length", truncation=True)

# Load tokenizer và model
tokenizer = GPT2Tokenizer.from_pretrained("tokenizer\\csharp_tokenizer")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Sử dụng phương pháp của datasets để chia dữ liệu thành train và validation
train_dataset = dataset['train'].train_test_split(test_size=0.1)['train']
val_dataset = dataset['train'].train_test_split(test_size=0.1)['test']

# Áp dụng tiền xử lý cho dữ liệu train và validation
train_dataset = train_dataset.map(tokenize_function, batched=True)
val_dataset = val_dataset.map(tokenize_function, batched=True)

# Tạo data collator để chuẩn bị dữ liệu cho huấn luyện
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=False
)

# Thiết lập huấn luyện
training_args = TrainingArguments(
    output_dir="model\\csharp_gpt2", 
    per_device_train_batch_size=8, 
    num_train_epochs=3, 
    remove_unused_columns=False, 
    evaluation_strategy="model\\epoch",  # Đánh giá mô hình sau mỗi epoch
    save_strategy="model\\epoch",  # Lưu mô hình sau mỗi epoch
    logging_dir="model\\logs",  # Lưu log huấn luyện
    logging_steps=500,  # Log mỗi 500 bước huấn luyện
    load_best_model_at_end=True,  # Tải mô hình tốt nhất khi kết thúc huấn luyện
    weight_decay=0.01  # Giảm thiểu overfitting
)

trainer = Trainer(
    model=model, 
    args=training_args, 
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    data_collator=data_collator
)

# Bắt đầu huấn luyện
trainer.train()

# Lưu mô hình và tokenizer
model.save_pretrained("model\\csharp_gpt2")
tokenizer.save_pretrained("model\\csharp_gpt2")
