import os
from ocr_module import process_certificate

CLEAN_FOLDER = "dataset/clean"
FAKE_FOLDER = "dataset/tampered"


def evaluate():

    TP = 0  # True Positive (clean detected as authentic)
    TN = 0  # True Negative (fake detected as suspicious)
    FP = 0  # Fake detected as authentic
    FN = 0  # Clean detected as suspicious

    print("\nEvaluating Clean Certificates...\n")

    for file in os.listdir(CLEAN_FOLDER):
        if file.endswith(".jpg"):
            result = process_certificate(os.path.join(CLEAN_FOLDER, file))

            if result["status"] == "Highly Authentic":
                TP += 1
            else:
                FN += 1

    print("Evaluating Fake Certificates...\n")

    for file in os.listdir(FAKE_FOLDER):
        if file.endswith(".jpg"):
            result = process_certificate(os.path.join(FAKE_FOLDER, file))

            if result["status"] == "Suspicious":
                TN += 1
            else:
                FP += 1

    total = TP + TN + FP + FN

    accuracy = (TP + TN) / total if total > 0 else 0
    precision = TP / (TP + FP) if (TP + FP) > 0 else 0
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0

    print("---------- RESULTS ----------")
    print("True Positive (TP):", TP)
    print("True Negative (TN):", TN)
    print("False Positive (FP):", FP)
    print("False Negative (FN):", FN)
    print("-----------------------------")
    print("Accuracy:", round(accuracy * 100, 2), "%")
    print("Precision:", round(precision * 100, 2), "%")
    print("Recall:", round(recall * 100, 2), "%")


if __name__ == "__main__":
    evaluate()