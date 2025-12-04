import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, log_loss 

class TitanicDecesionTree:
    def __init__(self, url, max_depth):
        self.url = url
        self.max_depth = max_depth
        self.data = None
        self.model = None
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None
        self.labels = None

    # Hàm tải dữ liệu
    def load_data(self):
        self.data = pd.read_csv(self.url)
        cols = self.data.shape[1]
        self.data.dropna(subset=['Survived'], inplace=True)

        # Chọn ra các cột để train
        features = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
        self.labels = features

        df = self.data[["Survived"] + features].copy()

        # Xử lý giá trị bị thiếu
        df['Age'].fillna(df['Age'].median(), inplace=True)
        df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

        # Mã hóa các dạng dữ liệu chữ
        labels_encoders = {}
        for col in ["Sex", "Embarked"]:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            labels_encoders[col] = le 

        # Tách dữ liệu train và test
        X = df[features]
        y = df["Survived"]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split (
            X, y, test_size=0.2, random_state=42
        )          
    
    # Hàm huân luyện mô hình
    def train_model(self):
        self.model = DecisionTreeClassifier(max_depth=self.max_depth, random_state=42)
        self.model.fit(self.X_train, self.y_train)

    # Hàm đánh giá mô hình
    def evaluate(self):
        y_pred = self.model.predict(self.X_test)
        y_probability = self.model.predict_proba(self.X_test)


        accuracy = accuracy_score(self.y_test, y_pred)
        loss = log_loss(self.y_test, y_probability)

        print(f"Accuracy: {accuracy:.4f}")
        print(f"Loss: {loss:.4f}") 

    # Hàm vẽ cây quyết định
    def draw_decesion_tree(self):
        plt.figure(figsize=(40, 20)) 

        plot_tree(
            self.model,
            feature_names=self.labels,
            class_names=["Not survived", "Survived"],
            precision=2,
            filled=True,           
            rounded=True,          
            fontsize=12,           
            proportion=True,       
            impurity=False         
        )

        plt.title("Decision Tree - Titanic Dataset", fontsize=20)
        plt.show()