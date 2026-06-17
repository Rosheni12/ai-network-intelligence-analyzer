import os

PROJECT_PATH = r"C:\Projects\AI-Network-Intelligence-Analyzer"

def show_tree(path, prefix=""):
    items = sorted(os.listdir(path))

    for i, item in enumerate(items):
        full_path = os.path.join(path, item)
        connector = "└── " if i == len(items) - 1 else "├── "

        if os.path.isdir(full_path):
            print(prefix + connector + "📁 " + item)
            new_prefix = prefix + ("    " if i == len(items) - 1 else "│   ")
            show_tree(full_path, new_prefix)
        else:
            print(prefix + connector + "📄 " + item)

if __name__ == "__main__":
    print("\nAI-NETWORK-INTELLIGENCE-ANALYZER STRUCTURE\n")
    show_tree(PROJECT_PATH)