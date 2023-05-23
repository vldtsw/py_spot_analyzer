env_variables = {}


# Function to get key-value pairs from user input
def get_env_variables():
    while True:
        key = input("Variable name: ")
        if key.lower() == "q":
            break
        value = input(f"Enter the value for '{key}': ")
        env_variables[key.strip()] = value.strip()


# Function to generate the .env file
def generate_env_file():
    with open(".env", "w") as file:
        for key, value in env_variables.items():
            file.write(f"{key}={value}\n")


# Main execution
if __name__ == "__main__":
    print("Enter the environment variables. 'q' to finish.")
    get_env_variables()
    generate_env_file()
    print(".env file has been generated successfully.")
