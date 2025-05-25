import torch
from transformers import AutoTokenizer
from auto_compressor import LlamaAutoCompressorModel


def initialize_model():
    """Initialize the model and tokenizer"""
    tokenizer = AutoTokenizer.from_pretrained("princeton-nlp/AutoCompressor-Llama-2-7b-6k")
    model = LlamaAutoCompressorModel.from_pretrained(
        "princeton-nlp/AutoCompressor-Llama-2-7b-6k",
        torch_dtype=torch.bfloat16
    ).eval().cuda()
    return tokenizer, model


def compress_context(tokenizer, model, context_text, summary_length=50):
    # Dynamically set the summary length
    model.config.summary_length = summary_length

    """Generate compressed vector for the text"""
    context_tokens = tokenizer(
        context_text,
        add_special_tokens=False,
        return_tensors="pt"
    ).input_ids.cuda()

    with torch.no_grad():
        outputs = model(context_tokens, output_softprompt=True)

    print(f"Compressed {context_tokens.size(1)} tokens -> {outputs.softprompt.size(1)} vectors")
    return outputs.softprompt


def generate_with_softprompt(tokenizer, model, prompt_text, softprompt):
    """Generate text with soft prompt"""
    prompt_tokens = tokenizer(
        prompt_text,
        add_special_tokens=False,
        return_tensors="pt"
    ).input_ids.cuda()

    generation = model.generate(
        prompt_tokens,
        do_sample=False,
        softprompt=softprompt,
        max_new_tokens=12
    )
    return tokenizer.decode(generation[0])


def generate_without_context(tokenizer, model, prompt_text):
    """Baseline generation without context"""
    prompt_tokens = tokenizer(
        prompt_text,
        add_special_tokens=False,
        return_tensors="pt"
    ).input_ids.cuda()

    generation = model.generate(
        prompt_tokens,
        do_sample=False,
        max_new_tokens=11
    )
    return tokenizer.decode(generation[0])