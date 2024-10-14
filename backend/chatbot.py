import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the tokenizer and model
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Create a history to store the conversation
chat_history_ids = None

# List of languages the bot can help with
known_languages = {
    "Spanish": {
        "greetings": {
            "Hola": "Hello",
            "Buenos días": "Good morning",
            "Buenas tardes": "Good afternoon",
            "Buenas noches": "Good evening/night",
            "¿Cómo estás?": "How are you?",
        },
        "common_phrases": {
            "Gracias": "Thank you",
            "Por favor": "Please",
            "Lo siento": "I'm sorry",
            "Sí": "Yes",
            "No": "No",
        },
        "questions": {
            "¿Qué es esto?": "What is this?",
            "¿Dónde está el baño?": "Where is the bathroom?",
            "¿Cuánto cuesta?": "How much does it cost?",
            "¿Puedo ayudarle?": "Can I help you?",
        },
        "useful_vocabulary": {
            "agua": "water",
            "comida": "food",
            "casa": "house",
            "amigo": "friend",
            "trabajo": "work",
        },
    },
    "French": {
        "greetings": {
            "Bonjour": "Good morning/Hello",
            "Bonsoir": "Good evening",
            "Salut": "Hi",
            "Comment ça va?": "How are you?",
            "À bientôt": "See you soon",
        },
        "common_phrases": {
            "Merci": "Thank you",
            "S'il vous plaît": "Please",
            "Je suis désolé": "I'm sorry",
            "Oui": "Yes",
            "Non": "No",
        },
        "questions": {
            "Qu'est-ce que c'est?": "What is this?",
            "Où sont les toilettes?": "Where is the bathroom?",
            "Combien ça coûte?": "How much does it cost?",
            "Puis-je vous aider?": "Can I help you?",
        },
        "useful_vocabulary": {
            "eau": "water",
            "nourriture": "food",
            "maison": "house",
            "ami": "friend",
            "travail": "work",
        },
    },
    "German": {
        "greetings": {
            "Hallo": "Hello",
            "Guten Morgen": "Good morning",
            "Guten Abend": "Good evening",
            "Wie geht's?": "How are you?",
            "Auf Wiedersehen": "Goodbye",
        },
        "common_phrases": {
            "Danke": "Thank you",
            "Bitte": "Please",
            "Es tut mir leid": "I'm sorry",
            "Ja": "Yes",
            "Nein": "No",
        },
        "questions": {
            "Was ist das?": "What is this?",
            "Wo ist die Toilette?": "Where is the bathroom?",
            "Wie viel kostet das?": "How much does it cost?",
            "Kann ich Ihnen helfen?": "Can I help you?",
        },
        "useful_vocabulary": {
            "Wasser": "water",
            "Essen": "food",
            "Haus": "house",
            "Freund": "friend",
            "Arbeit": "work",
        },
    },
    "Italian": {
        "greetings": {
            "Ciao": "Hi/Hello",
            "Buongiorno": "Good morning",
            "Buonasera": "Good evening",
            "Come stai?": "How are you?",
            "Arrivederci": "Goodbye",
        },
        "common_phrases": {
            "Grazie": "Thank you",
            "Per favore": "Please",
            "Mi dispiace": "I'm sorry",
            "Sì": "Yes",
            "No": "No",
        },
        "questions": {
            "Che cos'è?": "What is this?",
            "Dove sono i bagni?": "Where is the bathroom?",
            "Quanto costa?": "How much does it cost?",
            "Posso aiutarti?": "Can I help you?",
        },
        "useful_vocabulary": {
            "acqua": "water",
            "cibo": "food",
            "casa": "house",
            "amico": "friend",
            "lavoro": "work",
        },
    },
    "Chinese": {
        "greetings": {
            "你好 (Nǐ hǎo)": "Hello",
            "早上好 (Zǎoshang hǎo)": "Good morning",
            "晚上好 (Wǎnshàng hǎo)": "Good evening",
            "你好吗? (Nǐ hǎo ma?)": "How are you?",
            "再见 (Zàijiàn)": "Goodbye",
        },
        "common_phrases": {
            "谢谢 (Xièxiè)": "Thank you",
            "请 (Qǐng)": "Please",
            "对不起 (Duìbùqǐ)": "I'm sorry",
            "是 (Shì)": "Yes",
            "不是 (Bù shì)": "No",
        },
        "questions": {
            "这是什么? (Zhè shì shénme?)": "What is this?",
            "厕所在哪里? (Cèsuǒ zài nǎlǐ?)": "Where is the bathroom?",
            "这个多少钱? (Zhège duōshǎo qián?)": "How much does it cost?",
            "我可以帮助你吗? (Wǒ kěyǐ bāngzhù nǐ ma?)": "Can I help you?",
        },
        "useful_vocabulary": {
            "水 (Shuǐ)": "water",
            "食物 (Shíwù)": "food",
            "房子 (Fángzi)": "house",
            "朋友 (Péngyǒu)": "friend",
            "工作 (Gōngzuò)": "work",
        },
    },
    "Japanese": {
        "greetings": {
            "こんにちは (Konnichiwa)": "Hello/Good afternoon",
            "おはようございます (Ohayō gozaimasu)": "Good morning",
            "こんばんは (Konbanwa)": "Good evening",
            "お元気ですか? (Ogenki desu ka?)": "How are you?",
            "さようなら (Sayōnara)": "Goodbye",
        },
        "common_phrases": {
            "ありがとうございます (Arigatou gozaimasu)": "Thank you",
            "お願いします (Onegaishimasu)": "Please",
            "ごめんなさい (Gomen nasai)": "I'm sorry",
            "はい (Hai)": "Yes",
            "いいえ (Iie)": "No",
        },
        "questions": {
            "これは何ですか? (Kore wa nan desu ka?)": "What is this?",
            "トイレはどこですか? (Toire wa doko desu ka?)": "Where is the bathroom?",
            "これはいくらですか? (Kore wa ikura desu ka?)": "How much does it cost?",
            "手伝ってもいいですか? (Tetsudatte mo ii desu ka?)": "Can I help you?",
        },
        "useful_vocabulary": {
            "水 (Mizu)": "water",
            "食べ物 (Tabemono)": "food",
            "家 (Ie)": "house",
            "友達 (Tomodachi)": "friend",
            "仕事 (Shigoto)": "work",
        },
    },
}


def get_learned_response(user_input):
    """Check if the user input has a learned response."""
    try:
        with open("learning_data.txt", "r") as f:
            for line in f:
                if line.startswith(user_input):
                    return line.split("->")[1].strip()
    except FileNotFoundError:
        return None

def get_chatbot_response(user_input):
    global chat_history_ids

    # Check for learned response
    learned_response = get_learned_response(user_input)
    if learned_response:
        return learned_response

    # Check if the user wants to learn a language
    if "learn" in user_input.lower() and "language" in user_input.lower():
        return "Sure! Which language would you like to learn? I can help you with Spanish or French."

    # Check if the user specified a language
    for language in known_languages.keys():
        if language.lower() in user_input.lower():
            phrases = known_languages[language]
            phrases_response = "\n".join([f"{k}: {v}" for k, v in phrases.items()])
            return f"I can teach you some {language} phrases:\n{phrases_response}"

    # Encode the new user input, add the eos_token and return a tensor
    new_user_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')

    # Append the new user input to the chat history
    if chat_history_ids is None:
        chat_history_ids = new_user_input_ids
    else:
        chat_history_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1)

    # Generate a response from the model
    bot_output = model.generate(chat_history_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    # Get the bot's response and decode it
    bot_response = tokenizer.decode(bot_output[:, chat_history_ids.shape[-1]:][0], skip_special_tokens=True)

    return bot_response
