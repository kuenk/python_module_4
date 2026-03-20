
if __name__ == "__main__":
    try:
        print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")

        print("\nInitiating secure vault access...")
        print("Vault connection established with failsafe protocols\n")
        name_file = "classified_data.txt"
        path = ".."

        with open(f"{path}/{name_file}") as file:
            print("SECURE EXTRACTION:")
            print(file.read())

        name_file = "security_protocols.txt"
        with open(f"{path}/{name_file}") as file:
            print("\nSECURE PRESERVATION:")
            print(file.read())
            print("Vault automatically sealed upon completion\n")

        print("All vault operations completed with maximum security")
    except IOError:
        print("Error files")
