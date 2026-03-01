from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="gpt2"
)

def generate_policy(summary, scenario):

    prompt = f"""
Policy Summary:
{summary}

Scenario:
{scenario}

Write an adapted policy draft suitable for this scenario.
Maintain professional policy tone.
"""

    result = generator(
        prompt,
        max_length=500,
        num_return_sequences=1,
        temperature=0.7
    )

    return result[0]['generated_text']

