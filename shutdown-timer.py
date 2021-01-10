from os import system

def main():
    command = input("How long do you want to wait until shutdown?\n('a' to abort an existing timer, press ENTER for a one hour timer)\n")
    if command == "a":
        system("shutdown -a")
        return 0
    if command == "":
        system("shutdown -a")
        system("shutdown -s -t 3600")
        return 0
    sentence = command.split(" ")
    total_seconds = 0
    for index, word in enumerate(sentence):
        if word in ("hour", "hours"):
            hours = int(sentence[index - 1])
            total_seconds += hours * 60 * 60
        if word in ("minute", "minutes"):
            minutes = int(sentence[index - 1])
            total_seconds += minutes * 60
        if word in ("second", "seconds"):
            minutes = int(sentence[index - 1])
            total_seconds += minutes
    system("shutdown -a")
    system(f"shutdown -s -t {total_seconds}")

main()
