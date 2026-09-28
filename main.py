import os
import shutil

folder = "Test_Files"

categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Excel": [".xlsx", ".xls", ".csv"],
    "Python": [".py"]
}

for file in os.listdir(folder):

    file_path = os.path.join(folder, file)

    if os.path.isfile(file_path):

        extension = os.path.splitext(file)[1].lower()

        for category, extensions in categories.items():

            if extension in extensions:

                category_folder = os.path.join(folder, category)

                os.makedirs(category_folder, exist_ok=True)

                shutil.move(
                    file_path,
                    os.path.join(category_folder, file)
                )

                print(file, "→", category)
                break

print("Folder organization completed!")