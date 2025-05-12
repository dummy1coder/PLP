def modify_content(content):
    return content.upper()

def main():
    input_filename = input("Enter the filename to read from: ")
    
    try:
        with open(input_filename, "r") as infile:
            content = infile.read()
            print("Original content read successfully.")

        modified_content = modify_content(content)

        output_filename = "modified_" + input_filename
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)
            print(f"Modified content written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"❌ Error: Could not read the file '{input_filename}'.")

if __name__ == "__main__":
    main()
