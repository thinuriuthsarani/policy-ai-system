from transformers import pipeline

# load summarization model
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def summarize_policy(text):

    # split long text into chunks
    max_chunk = 1000
    chunks = [text[i:i+max_chunk] for i in range(0, len(text), max_chunk)]

    summaries = []

    for chunk in chunks:
        summary = summarizer(
            chunk,
            max_length=150,
            min_length=50,
            do_sample=False
        )
        summaries.append(summary[0]['summary_text'])

    final_summary = " ".join(summaries)

    return final_summary

