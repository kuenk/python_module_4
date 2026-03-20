
if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")

    file_name = "ancient_fragment.txt"
    path = ".."
    file = None
    try:
        file = open(f"{path}/{file_name}")
        print(f"Accessing Storage Vault: {file_name}")
        print("Connection established...\n")

        print("RECOVERED DATA:")
        print(file.read())

        print("\nData recovery complete. Storage unit disconnected")
    except FileNotFoundError:
        print("File not found")
    finally:
        if file:
            file.close()
