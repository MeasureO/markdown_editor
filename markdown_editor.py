def help_message():
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
    print("Special commands: !help !done")

def header():
    while True:
        level = int(input("Level: "))
        if level < 1 or level > 6:
            print("The level should be within the range of 1 to 6")
            continue
        text = input("Text: ")
        break
    return f"{'#' * level} {text}\n"

def plain():
    text = input("Text: ")
    return text

def bold():
    text = input("Text: ")
    return f"**{text}**"

def italic():
    text = input("Text: ")
    return f"*{text}*"

def inline_code():
    text = input("Text: ")
    return f"`{text}`"

def new_line():
    return '\n'

def link():
    label = input("Label: ")
    url = input("URL: ")
    return f"[{label}]({url})"

def ordered_list():
    while True:
        rows_number = int(input("Number of rows: "))
        if rows_number < 1:
            print("The number of rows should be greater than zero")
            continue
        else:
            break
    rows = [input(f"Row #{i + 1}: ") for i in range(rows_number)]
    new_rows = [f"{i + 1}. " + rows[i] for i in range(len(rows))]
    return '\n'.join(new_rows) + '\n'

def unordered_list():
    while True:
        rows_number = int(input("Number of rows: "))
        if rows_number < 1:
            print("The number of rows should be greater than zero")
            continue
        else:
            break
    rows = [input(f"Row #{i + 1}: ") for i in range(rows_number)]
    new_rows = list(map(lambda x: '* ' + x, rows))
    return '\n'.join(new_rows) + '\n'


def main(func_dict):
    answer = ""
    formatters = "plain bold italic header link inline-code new-line ordered-list unordered-list".split()
    while True:
        command = input("Choose a formatter: ")
        if command in formatters:
            answer += func_dict[command]()
            print(answer)
            continue
        elif command == "!help":
            help_message()
            continue
        elif command == "!done":
            save_to_file(answer)
            break
        else:
            print("Unknown formatter type or command")
            continue

def save_to_file(text):
    with open('output.md', 'w', encoding='utf-8') as file:
        file.write(text)

if __name__ == "__main__":
    func_dict = {
                    "header": header,
                    "plain": plain,
                    "bold": bold,
                    "italic": italic,
                    "inline-code": inline_code,
                    "new-line": new_line,
                    "link": link,
                    "ordered-list": ordered_list,
                    "unordered-list": unordered_list
                }
    main(func_dict)
