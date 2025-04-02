def read_and_modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
            # Modify the content as needed
            modified_content = content.upper()  # Example modification: convert to uppercase

        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        print(f"File '{input_filename}' has been read and modified content written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read the file '{input_filename}'.")

if __name__ == "__main__":
    input_filename = input("Enter the name of the file to read: ")
    output_filename = input("Enter the name of the file to write the modified content to: ")
    read_and_modify_file(input_filename, output_filename)