if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")

    file_name = "new_discovery.txt"
    try:
        print(f"Initializing new storage unit: {file_name}")
        print("Storage unit created successfully...")

        with open(file_name, "a", encoding="utf-8") as f:
            f.write("[FRAGMENT 001] Digital preservation protocols "
                    "established 2087\n")
            f.write("[FRAGMENT 002] Knowledge must survive the entropy wars\n")
            f.write("[FRAGMENT 003] Every byte saved is a "
                    "victory against oblivion\n")

        with open(file_name, "r", encoding="utf-8") as f:
            print(f.read())

        print("Data inscription complete. Storage unit sealed")
        print(f"Archive {file_name} ready for long-term preservation.")
    except OSError:
        print("File error")
