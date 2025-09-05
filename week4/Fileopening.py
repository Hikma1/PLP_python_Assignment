# week4_file_challenges.py

def read_and_modify_file(input_filename, output_filename):
    """
    Reads a file, modifies its content (uppercase), 
    and writes it to a new file with proper error handling.
    """
    try:
        with open(input_filename, "r") as infile:
            content = infile.read()
        
        # Modify content (example: convert to uppercase)
        modified_content = content.upper()
        
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)
        
        print(f"✅ Successfully written modified content to '{output_filename}'")
    
    except FileNotFoundError:
        print(f"❌ Error: '{input_filename}' does not exist. Please check the filename.")
    except PermissionError:
        print(f"❌ Error: Permission denied for '{input_filename}' or '{output_filename}'.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")


# --- Main Program ---
if __name__ == "__main__":
    input_file = input("Enter the input filename: ")
    output_file = input("Enter the output filename: ")
    read_and_modify_file(input_file, output_file)
