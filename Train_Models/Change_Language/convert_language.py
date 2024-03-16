from googletrans import Translator

def translate_text(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

# Sử dụng hàm để dịch văn bản
text_to_translate = "Xin chào, đây là một ví dụ về chuyển đổi ngôn ngữ trong Python."
translated_text = translate_text(text_to_translate, target_language='en')
print("Translated text:", translated_text)
