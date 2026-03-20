import sys

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    archivist_id = input("Input stream active. Enter archivist ID: ")
    status = input("Input stream active. Enter status report: ")

    sys.stdout.write(f"[STANDARD] Archive status "
                     f"from {archivist_id}: {status}\n")
    sys.stdout.flush()
    sys.stderr.write("[ALERT] System diagnostic: Communication "
                     "channels verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n")

    print("Three-channel communication test successful")
