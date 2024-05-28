from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Load the model and tokenizer
model_path = "./version_3"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

# Function to generate corrected text


def generate_text(model, tokenizer, text, num_beams=5, min_length=1, max_length=50):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model.generate(
        inputs["input_ids"],
        num_beams=num_beams,
        min_length=min_length,
        max_length=max_length
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


# Example texts
example_1 = "grammar: Although I was sick but I still went to school."
result_1 = generate_text(model, tokenizer, example_1)
print(result_1)

# example_2 = "grammar: My kids are back in school to. I find their are less things to worry about now that the kids are at school all day. There is plenty of fun things to do in the summer, but by August, I’ve running out of ideas. I’ve excepted the fact that we’ll have to think up brand-new activities next summer; hoping to round up some creative ideas soon."
# result_2 = generate_text(model, tokenizer, example_2)
# print(result_2)

# example_3 = "Between your view or your level(s) does your idea impact?"
# result_3 = generate_text(model, tokenizer, example_3)
# print(result_3)

# example_4 = "grammar: The sates school system in England can be divided into two levels of educated: primary and secondary	"
# result_4 = generate_text(model, tokenizer, example_4)
# print(result_4)

# example_5 = "grammar: Ours brains are incredibly agile machines, and it's hard to think of anything they do more efficient than recognize face	"
# result_5 = generate_text(model, tokenizer, example_5)
# print(result_5)
