import os

def process_lyrics_file(file_path):
    try:
        with open(file_path, 'r') as file:
            line_number = 1
            while True:
                line = file.readline()
                if not line:
                    break
                line_stripped = line.strip()
                word_count = len(line_stripped.split())
                print(f"{line_number}. {line.strip().upper()}(Words: {word_count})")
                line_number += 1
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError as e:
        print(f"IO error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Get absolute path of the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'lyrics.txt')
    print(f"Trying to open file at: {file_path}")
    process_lyrics_file(file_path)
