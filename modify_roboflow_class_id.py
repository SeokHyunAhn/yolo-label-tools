import os
import sys

def check_and_update_class_id(label_dir, current_class, new_class):
    """
    주어진 디렉토리 내의 모든 .txt 파일을 읽어 class_id를 확인하고 변경합니다.

    :param label_dir: 라벨 파일들이 있는 디렉토리 경로
    :param current_class: 확인할 기존 클래스 ID
    :param new_class: 변경할 새로운 클래스 ID
    :return: class_id가 존재했는지 여부
    """
    class_exists = False  # class_id 존재 여부를 추적
    for root, _, files in os.walk(label_dir):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    lines = f.readlines()

                updated_lines = []
                for line in lines:
                    parts = line.strip().split()
                    if parts[0] == str(current_class):
                        class_exists = True
                        parts[0] = str(new_class)  # class_id 변경
                    updated_lines.append(" ".join(parts))

                # 파일 업데이트
                with open(file_path, "w") as f:
                    f.write("\n".join(updated_lines))

    return class_exists


if __name__ == "__main__":
    # 명령줄 인자 처리
    if len(sys.argv) != 3:
        print("Usage: python3 <script.py> <current_class> <new_class>")
        sys.exit(1)

    current_class = sys.argv[1]
    new_class = sys.argv[2]

    # train/labels와 valid/labels 폴더 경로
    train_labels_dir = "train/labels"
    valid_labels_dir = "valid/labels"

    # 클래스 ID 확인 및 변경
    print(f"Checking and updating class ID {current_class} to {new_class} in train/labels...")
    train_exists = check_and_update_class_id(train_labels_dir, current_class, new_class)

    print(f"Checking and updating class ID {current_class} to {new_class} in valid/labels...")
    valid_exists = check_and_update_class_id(valid_labels_dir, current_class, new_class)

    # 결과 출력
    if not train_exists and not valid_exists:
        print(f"Class ID {current_class} does not exist in train/labels or valid/labels.")
    else:
        print(f"Class ID {current_class} was updated to {new_class}.")

