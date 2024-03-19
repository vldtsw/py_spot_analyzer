env_variables: dict = {
    "SPOTIPY_CLIENT_ID": "",
    "SPOTIPY_CLIENT_SECRET": "",
    "SPOTIPY_REDIRECT_URI": "",
}


def get_env_variable_values() -> None:
    """
    Get the values for the environment variables from user input
    """
    for key in env_variables:
        value = input(f"'{key}': ")
        env_variables[key] = value


def generate_env_file() -> None:
    """
    Generate the .env file with the environment variables
    """
    with open(".env", "w") as file:
        for key, value in env_variables.items():
            file.write(f"{key.strip()}={value.strip()}\n")


def env_setup() -> None:
    """
    Main function to set up the environment variables
    """
    print("Enter the values for the environment variables:")
    get_env_variable_values()
    generate_env_file()
    print(".env file has been generated successfully.")


if __name__ == "__main__":
    env_setup()
