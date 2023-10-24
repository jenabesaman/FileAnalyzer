def converting(input_text):
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = "text.txt"
    output_path = os.path.join(script_dir, file_path)
    with open(output_path, "w") as file:
        file.write(input_text)



def converting2(input_text):
    user_input = ""
    while True:
        line = input_text
        if line == "":
            break
        user_input += line + "\n"
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = "text.txt"
    output_path = os.path.join(script_dir, file_path)
    with open(output_path, "w") as file:
        file.write(input_text)

converting2(input_text="")

print(converting())
