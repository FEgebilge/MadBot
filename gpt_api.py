"""
import openai
import config

# Set up your OpenAI API credentials
openai.api_key = config.GPT_API_KEY

def generate_text(prompt):
    print(prompt)
    response = openai.Completion.create(
        engine='gpt-3.5-turbo',  # Specify the GPT model to use
        prompt=prompt,
        max_tokens=3000,  # Adjust the desired length of the generated text
        temperature=0.3,
        n=1 # Specify the number of responses to generate
         # Set a custom stop condition if desired
    )

    # Extract the generated text from the API response
    generated_text = response.choices[0].text.strip()
    print(generated_text)
    return generated_text

"""