
if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    file_name = "lost_archive.txt"
    try:
        with open(f"../{file_name}") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    file_name = "classified_data.txt"
    try:
        with open(f"../{file_name}") as file:
            print(file.read())
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    file_name = "standard_archive.txt"
    try:
        with open(f"../{file_name}") as file:
            print(f"ROUTINE ACCESS: Attempting access to '{file_name}'...")
            print(f"SUCCESS: Archive recovered - '{file.read()}'")
            print("STATUS: Normal operations resumed\n")
    except IOError:
        print("Error file")

    print("All crisis scenarios handled successfully. Archives secure.")
