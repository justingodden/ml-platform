from metaflow import FlowSpec, step, card, conda_base, current


@conda_base(
    libraries={"scikit-learn": "1.3.1", "pandas": "2.1.1", "matplotlib": "3.8.0"}
)
class ClassificationFlow(FlowSpec):
    @step
    def start(self):
        self.next(self.get_data)

    @step
    def get_data(self):
        from sklearn.datasets import load_breast_cancer

        self.df = load_breast_cancer(as_frame=True)
        self.next(self.feature_engineering)

    @step
    def feature_engineering(self):
        from sklearn.model_selection import train_test_split

        X, y = self.df["data"], self.df["target"]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.33, random_state=42
        )
        self.next(self.train)

    @step
    def train(self):
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.metrics import confusion_matrix, f1_score

        rf = RandomForestClassifier(n_estimators=10)
        rf.fit(self.X_train, self.y_train)
        self.model = rf

        self.classes = rf.classes_
        y_pred = rf.predict(self.X_test)
        self.cm = confusion_matrix(self.y_test, y_pred, labels=self.classes)
        self.f1_score = f1_score(self.y_test, y_pred)

        self.next(self.plot)

    @card
    @step
    def plot(self):
        from metaflow.cards import Image, Markdown
        from sklearn.metrics import ConfusionMatrixDisplay

        current.card.append(Markdown("# Breast Cancer Classification"))
        disp = ConfusionMatrixDisplay(
            confusion_matrix=self.cm, display_labels=self.classes
        )
        disp.plot()
        current.card.append(Image.from_matplotlib(disp.figure_))

        current.card.append(Markdown(f"## F1 Score: {self.f1_score:.3f}"))
        self.next(self.end)

    @step
    def end(self):
        print("Training is done!")


if __name__ == "__main__":
    ClassificationFlow()
