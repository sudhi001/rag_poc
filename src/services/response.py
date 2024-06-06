from transformers import AutoTokenizer, AutoModelForCausalLM

gpt_model_name = "gpt2"
gpt_tokenizer = AutoTokenizer.from_pretrained(gpt_model_name)
gpt_model = AutoModelForCausalLM.from_pretrained(gpt_model_name)


def generate_response(query, relevant_docs):
    context = " ".join([doc.text for doc in relevant_docs])
    input_text = f"{context}\n{query}"  # Combine context and query directly
    inputs = gpt_tokenizer(input_text, return_tensors="pt")
    outputs = gpt_model.generate(inputs.input_ids, max_new_tokens=50, num_return_sequences=1, no_repeat_ngram_size=2)
    generated_response = gpt_tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Extract only the generated response without the context and question
    response_lines = generated_response.split("\n")
    return response_lines[-1].strip()  # Return the last line of the generated response


