mkdir data

# echo "Please enter a Github API access token: "
read -p "Please enter a Github API access token: " TOKEN
echo "GITHUB_PAT=$TOKEN" > ".env"