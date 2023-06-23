env_variables = {
    "SPOTIPY_CLIENT_ID": "",
    "SPOTIPY_CLIENT_SECRET": "",
    "SPOTIPY_REDIRECT_URI": "",
}


# Function to get values for the environment variables from user input
def get_env_variable_values():
    for key in env_variables:
        value = input(f"Enter the value for '{key}': ")
        env_variables[key] = value


# Function to generate the .env file
def generate_env_file():
    with open(".env", "w") as file:
        for key, value in env_variables.items():
            file.write(f"{key.strip()}={value.strip()}\n")


# Main execution
if __name__ == "__main__":
    print("Enter the values for the environment variables:")
    get_env_variable_values()
    generate_env_file()
    print(".env file has been generated successfully.")
