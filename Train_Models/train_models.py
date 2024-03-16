from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from Data import Datagen


# Chia dữ liệu và huấn luyện mô hình
texts = [' '.join(text_list) for emotion, text_list in Datagen.data]
labels = [emotion for emotion, text_list in Datagen.data]

# Chuyển đổi văn bản thành vector TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Chuẩn hóa nhãn
le = preprocessing.LabelEncoder()
y = le.fit_transform(labels)

# Huấn luyện mô hình SVM
svm_classifier = SVC(kernel='linear')
svm_classifier.fit(X, y)

# Khởi tạo biến đếm
input_count = 0
pos_count = 0
neg_count = 0

# Vòng lặp để người dùng nhập văn bản
while True:
    user_input = input("You: ")
    
    if user_input=='exit':
        exit()
     # Tăng biến đếm sau mỗi lần người dùng nhập vào
    input_count += 1

    # Chuyển đổi văn bản nhập vào thành vector TF-IDF
    user_input_vectorized = vectorizer.transform([user_input])
    
    # Dự đoán cảm xúc
    predicted_label = svm_classifier.predict(user_input_vectorized)

    # Giải mã nhãn thành cảm xúc
    predicted_emotion = le.inverse_transform(predicted_label)

    # Đếm số câu của mỗi loại cảm xúc trong dữ liệu mẫu
    if predicted_emotion[0] == "Positive Emotions":
        pos_count += 1
    elif predicted_emotion[0] == "Negative Emotions":
        neg_count += 1
    

    # Tính phần trăm
    pos_percentage = (pos_count / input_count) * 100
    neg_percentage = (neg_count / input_count) * 100

    # In kết quả
    print(f"Cảm xúc dự đoán: {predicted_emotion[0]}")
    print(f"Phần trăm cảm xúc tích cực: {pos_percentage:.2f}%")
    print(f"Phần trăm cảm xúc tiêu cực: {neg_percentage:.2f}%")
   

