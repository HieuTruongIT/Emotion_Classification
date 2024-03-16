from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')

# Access the Emotion database
db = client['Emotion']

# Access the positive and negative Emotion collections
positive_collection = db['positive_Emotion']
negative_collection = db['negative_Emotion']

# Sample data
data = [
    ("Positive Emotions", [
        "joy",
        "happiness",
        "elation",
        "refreshment",
        "optimism",
        "cheerfulness",
        "excitement",
        "happiness",
        "innocence",
        "joie de vivre",
        "delight",
        "full of energy",
        "enthusiasm",
        "confidence",
        "satisfaction",
        "peace",
        "glee",
        "please",
        "tranquility",
        ]),
    ("Negative Emotions", [
        "disappointment",
        "sadness",
        "boredom",
        "desperation",
        "suffering",
        "anger",
        "worry",
        "fear",
        "frustration",
        "disappointment",
        "rage",
        "loneliness",
        "guilt",
        "discomfort",
        "irritation",
        "childish",
        "anxiety",
        "sorrow",
        "disappointment",
        ]),
]

# Insert data into positive and negative collections
for emotion_type, emotions in data:
    if emotion_type == "Positive Emotions":
        for emotion in emotions:
            positive_collection.insert_one({"emotion": emotion})
    elif emotion_type == "Negative Emotions":
        for emotion in emotions:
            negative_collection.insert_one({"emotion": emotion})

# Close the connection
client.close()
