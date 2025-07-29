from transformers import pipeline

print("✅ Importing...")
generator = pipeline("text2text-generation", model="iarfmoose/t5-base-question-generator")
print("✅ Model loaded")

result = generator("generate question: The sun is the center of the solar system.")
print(result[0]['generated_text'])