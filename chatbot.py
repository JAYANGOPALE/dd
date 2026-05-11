import math

# ==========================================
# 1. THE KNOWLEDGE BASE
# ==========================================
# Instead of if-statements, we map "Training Phrases" to "Bot Responses"
knowledge_base = [
    {
        "intent": "seeds",
        "training": "buy purchase seeds plant corn wheat soybeans crops",
        "response": "We have high-yield Corn, Soybean, and Winter Wheat seeds in stock."
    },
    {
        "intent": "fertilizer",
        "training": "fertilizer compost soil nitrogen grow health dirt",
        "response": "Healthy soil is key! We stock organic compost and NPK 10-10-10."
    },
    {
        "intent": "pests",
        "training": "pests bugs insects weeds spray herbicide insecticide kill",
        "response": "We recommend Neem Oil for insects and organic herbicides for weeds."
    },
    {
        "intent": "store_info",
        "training": "hours open close time location address where buy",
        "response": "We are at 123 Harvest Road. Open Mon-Sat, 6:00 AM to 5:00 PM."
    }
]

# ==========================================
# 2. THE MATH (NATURAL LANGUAGE PROCESSING)
# ==========================================
def clean_text(text):
    """Removes punctuation and splits the sentence into lower-case words."""
    chars_to_remove = "?.,!;:\"'"
    for char in chars_to_remove:
        text = text.replace(char, "")
    return text.lower().split()

def get_vector(words, vocabulary):
    """Turns a list of words into an array of numbers (1 if word is present, 0 if not)."""
    return [1 if vocab_word in words else 0 for vocab_word in vocabulary]

def cosine_similarity(vec1, vec2):
    """Calculates the geometric similarity between two vectors. Returns 0.0 to 1.0."""
    dot_product = sum(x * y for x, y in zip(vec1, vec2))
    magnitude1 = math.sqrt(sum(x * x for x in vec1))
    magnitude2 = math.sqrt(sum(y * y for y in vec2))
    
    if magnitude1 * magnitude2 == 0:
        return 0.0
    return dot_product / (magnitude1 * magnitude2)

# ==========================================
# 3. THE CHATBOT BRAIN
# ==========================================
def smart_agribot():
    print("==========================================================")
    print("Smart AgriBot: Online. Powered by Vector Math.")
    print("==========================================================\n")

    # Build the master vocabulary from all our training phrases
    master_vocab = set()
    for item in knowledge_base:
        for word in clean_text(item["training"]):
            master_vocab.add(word)
    master_vocab = list(master_vocab)

    while True:
        user_input = input("Customer: ")
        if user_input.lower() in ["quit", "exit"]:
            print("Smart AgriBot: Goodbye!")
            break

        user_words = clean_text(user_input)
        user_vector = get_vector(user_words, master_vocab)

        best_match_score = 0.0
        best_response = "I'm not quite sure I understand. Could you rephrase that?"

        # Compare user input to every known intent
        for item in knowledge_base:
            intent_words = clean_text(item["training"])
            intent_vector = get_vector(intent_words, master_vocab)
            
            score = cosine_similarity(user_vector, intent_vector)
            
            # If this is the highest score so far, save it
            if score > best_match_score:
                best_match_score = score
                best_response = item["response"]

        # If the highest score is greater than 0, we found a match!
        if best_match_score > 0:
            # Uncomment the next line if you want to see the math in action in your terminal
            # print(f"[Debug: Matched intent with {(best_match_score*100):.1f}% confidence]")
            print(f"Smart AgriBot: {best_response}")
        else:
            print(f"Smart AgriBot: {best_response}")

if __name__ == "__main__":
    smart_agribot()