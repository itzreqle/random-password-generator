# Random Password Generator

This Python script generates random passwords based on user-specified criteria. You can customize the length and character sets of the generated passwords.

## How it Works

The `generate_password` function generates a random password based on the following criteria:

- **Length**: You can specify the length of the password using the `--length` argument. By default, the length is set to 12 characters.
    
- **Character Sets**: You can include the following character sets in the password using the corresponding command-line flags:
    
    - `--uppercase`: Include uppercase letters.
    - `--digits`: Include digits (0-9).
    - `--special-chars`: Include special characters (e.g., !@#$%^&*()_+[]{}|;':",.<>?).

The generated password will contain characters from the selected character sets, and it will be randomly generated.

## Installation

Follow these steps to use the Random Password Generator:

1. **Clone the Repository**:
    
    Clone this repository to your local machine using Git:
    
    ```bash
    git clone https://github.com/itzreqle/random-password-generator.git
    ```
    
2. **Navigate to the Directory**:
    
    Change your working directory to the cloned repository:
    
    ```bash
    cd random-password-generator
    ```
    
3. **Run the Script**:
    
    You can use the script with the following command-line arguments:
    
    - `--length`: Specifies the length of the password (default is 12 characters).
    - `--uppercase`: Include uppercase letters (default is False).
    - `--digits`: Include digits (default is False).
    - `--special-chars`: Include special characters (default is False).
    
    Example usage:
    
    ```bash
    python generate_password.py --length 16 --uppercase --digits --special-chars
    ```
    
    This command will generate a 16-character password that includes uppercase letters, digits, and special characters.
        

## License

This project is licensed under the MIT License - see the [LICENSE](https://chat.openai.com/LICENSE) file for details.
