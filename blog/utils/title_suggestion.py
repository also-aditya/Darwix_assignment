from transformers import pipeline
import os

def generate_titles(content):
    try:
        summarizer = pipeline(
            "summarization",
            model="facebook/bart-large-cnn",
            tokenizer="facebook/bart-large-cnn",
            framework="pt"
        )
        
        summary = summarizer(content, max_length=30, min_length=10, do_sample=True, num_return_sequences=3)
        titles = [item['summary_text'] for item in summary]
        return titles
    except Exception as e:
        raise Exception(f"Title generation failed: {str(e)}")