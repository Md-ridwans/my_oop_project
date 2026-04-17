import google.generativeai as genai
from gtts import gTTS

try:
    api_key = st.secrets["Gemini_Api_Key"]
except:
    from dotenv import load_dotenv
    import os
    load_dotenv()
    api_key = os.getenv("Gemini_Api_Key")

if not api_key:
    st.error("Gemini API key not found!")
    raise ValueError("Add your Gemini API key in .env or Streamlit Secrets")

genai.configure(api_key=api_key)


MODEL_NAME = "gemini-3-flash-preview"    

def prescription_generator(select_depend):
    prompt = f"""
You are a qualified medical assistant. Provide a clear and structured response based on the condition: "{select_depend}".

Instructions:
- If "{select_depend}" is an illness:
  Provide a basic prescription, including possible medications, general care advice, and precautions.

- If "{select_depend}" is a surgical procedure:
  Explain:
  1. What to do before and after the operation
  2. What to avoid (do’s and don’ts)
  3. Potential risks and complications

- If "{select_depend}" is an emergency condition:
  Provide step-by-step emergency actions that should be taken immediately.

Requirements:
- Keep the response under 300 words
- Use clear Markdown formatting (headings, bullet points)
- Keep the language simple and professional
- Do NOT provide overly technical or unsafe instructions
"""
    model = genai.GenerativeModel(MODEL_NAME)
    response = model.generate_content([select_depend, prompt])
    return response
