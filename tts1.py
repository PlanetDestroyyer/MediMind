import subprocess

while True:
    text = input("Enter text (or type 'exit' to quit): ")
    if text.lower() == 'exit':
        break
    subprocess.run(["espeak-ng", text])
