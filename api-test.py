import requests

#Input
gender = input("Enter gender (Male/Female) : ")
age = int(input("Enter age : "))
sal = int(input("Enter salary : "))

x = [gender,age,sal]

# Define input data for prediction
input_data = {'input': x}  # Example input

print(input_data)

# Make a POST request to the API
response = requests.post('https://om1024.pythonanywhere.com/predict', json=input_data)

if response.status_code == 200:
    prediction = response.json()
    y = prediction['prediction'][0]

    if y == 1:
        print("User will not buy from you")

    else:
        print("User will buy from you")

else:
    print("Failed to get prediction from the API")
