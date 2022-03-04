export FIREBASE_AUTH_EMULATOR_HOST="localhost:9099"

# curl -H 'Content-Type: application/json' \
#     -H 'Authorization: Bearer owner' \
#     --request POST \
#     --data '{"email":"test@vibe.com","password":"password123"}' \
#     http://localhost:9099/identitytoolkit.googleapis.com/v1/projects/vibe-rate-api/accounts

python -m pytest -srA tests/