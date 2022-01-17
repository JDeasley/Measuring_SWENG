# Function to check if required files have been created.
# Specifically, looking for:
#   a '.env' file with Github API access token under the variable name GITHUB_PAT,
#   and a 'data' directory for mongodb to use as a volume.
check_files()
{
    RET=0

    if test -f ".env"; then
    echo ".env file exists."
    else
        echo ".env file does not exist."
        echo "Please create a .env file in the base directory with a Github API access token with the variable name 'GITHUB_PAT'."
        RET=1
    fi

    echo "---"

    if test -d "./data"; then
        echo "data directory exists."
    else
        echo "data directory does not exist."
        echo "Please create a directory named 'data' in the base directory."
        RET=1
    fi

    echo "---"

    return $RET
}

# If check_files function is successful, start application.
if check_files; then
    echo "All files found."
    docker-compose up
else
    echo "Files not found."
    echo "Please create a '.env' file and a 'data' directory as outlined above, then retry this 'run' script."
fi