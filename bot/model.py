from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained(r'C:\Users\Ilya K\Desktop\chat_bot_vision\finetuned_model')
model = AutoModelForCausalLM.from_pretrained(r'C:\Users\Ilya K\Desktop\chat_bot_vision\finetuned_model')

def get_unique_response(response):
    sentences = response.split('. ')
    
    seen = set()
    unique_sentences = []
    
    for sentence in sentences:
        clean_sentence = sentence.strip().lower()
        if clean_sentence not in seen:
            unique_sentences.append(sentence)
            seen.add(clean_sentence)
    
    return unique_sentences[0] if unique_sentences else ""


def chat_with_bot(prompt):
    prompt = f"Вопрос: {prompt}\nОтвет:"
    
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, padding=True)
    
    outputs = model.generate(
        inputs.input_ids,
        max_length=35,  
        min_length=10,
        do_sample=True,
        temperature=0.6, 
        top_p=0.9, 
        no_repeat_ngram_size=0,
        num_beams=3,
        early_stopping=True
    )
    

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    response = get_unique_response(response)

    response = response.split("Ответ:")[-1].strip()
    
    return response
