import time

GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'


print(GREEN + "\nReading the content of captured data => the TCP packages data fields ad hexadecimal strings extracted with tshark\n" + RESET)
time.sleep(2)
# Read the content of the "captured_data" file
with open("captured_data.txt", "r") as file:
    hex_string = file.read().strip()


time.sleep(2)
print(GREEN + "\nConverting hexadecimal string to bytes...\n" + RESET)
time.sleep(2)

# Convert hexadecimal string to bytes
decoded_bytes = bytes.fromhex(hex_string)

time.sleep(2)
print(GREEN + "\nDecoding bytes using ascii encoding...\n" + RESET)
time.sleep(2)

# Decode bytes using ascii encoding and ignoring the error for not valid ascii characters
decoded_string = decoded_bytes.decode('ascii', errors='ignore')

# Print the decoded string containing the password "ft_wandrNDRelL0L" => still not the good password for accessing flag02
time.sleep(2)
print(YELLOW + "<<<<< RESULT >>>>>" + RESET)
print(decoded_string)
print(YELLOW + "<<<<<        >>>>>" + RESET)
time.sleep(3)
print(GREEN + "\n\nNow we let the DELETE(x7f) char make his job, that is removing the char before...\n\n" + RESET)
time.sleep(2)


decoded_string_with_delete_in_action = []

for i, char in enumerate(decoded_string):
    if char == '\x7f' and i > 0:
        # Remove the last character if it exists
        decoded_string_with_delete_in_action.pop()
    else:
        decoded_string_with_delete_in_action.append(char)

result = ''.join(decoded_string_with_delete_in_action)
print(YELLOW + "<<<<< RESULT >>>>>" + RESET)
print(result)
print(YELLOW + "<<<<<        >>>>>" + RESET)
time.sleep(3)
print(GREEN + "\n\nlet's isolate the password...\n\n" + RESET)
time.sleep(2)

# Find the index of "Password: "
password_index = result.find("Password: ")
if password_index != -1:
    # Find the index of the newline character starting from the position of "Password: "
    newline_index = result.find("\n", password_index)
    print(YELLOW + "<<<<< RESULT >>>>>" + RESET)
    if newline_index != -1:
        # Extract the substring between "Password: " and the newline character
        password_substring = result[password_index + len("Password: "):newline_index]
        # Remove leading and trailing whitespace
        password = password_substring.strip()
        print("Password:", password)
    else:
        print("No newline character found after 'Password:'.")
else:
    print("No password found.")
print(YELLOW + "<<<<<        >>>>>\n" + RESET)
