import random
import time
import os

def type_text(text, delay=0.05):
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

clear()
type_text("Booting up terminal...", 0.06)
time.sleep(0.8)

type_text("Hello Agent.\nYour task is to break into the target system without getting caught.\n", 0.05)

password = "delta"
type_text("[LOGIN] Hint: It's a Greek letter that starts with 'd'")

user_try = ""
while user_try.lower() != password:
    user_try = input("Password: ")
    if user_try.lower() != password:
        type_text("Wrong password. Try again.", 0.03)

type_text("Password accepted.\n", 0.03)
time.sleep(0.5)

type_text("Firewall check: Decrypt the code 'khoor' (Caesar shift by 3)")
ans = input("Your answer: ")

if ans.lower() == "hello":
    type_text("Nice! Firewall bypassed.\n", 0.03)
else:
    type_text("Not quite right... running brute-force... done!\nFirewall bypassed.\n", 0.03)

time.sleep(1)


type_text("Scanning network... Guess the open port (1-10)")
open_port = random.randint(1, 10)

while True:
    try:
        port_guess = int(input("Port: "))
    except ValueError:
        type_text("Numbers only!", 0.03)
        continue

    if port_guess == open_port:
        break
    else:
        type_text("No response. Trying again...", 0.03)

type_text(f"Port {open_port} is open. Accessing mainframe...\n", 0.05)

# Final step
type_text("Uploading payload...")
time.sleep(1)
type_text("Activating backdoor...")
time.sleep(1)
type_text("\n✅ ACCESS GRANTED — Target system hacked!\n", 0.03)

type_text("Mission complete, Agent. Returning to base.\n", 0.05)
