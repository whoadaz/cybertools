import subprocess

def aircrack_ng_crack(capture_file, wordlist):
    """
    Извършва разбиване на парола за Wi-Fi мрежа с Aircrack-ng.

    Args:
        capture_file: Път до capture файл (.cap или .pcap).
        wordlist: Път до wordlist файл.

    Returns:
        Резултат от разбиването на паролата.
    """
    command = ["aircrack-ng", "-w", wordlist, capture_file]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode()

def kismet_scan():
    """
    Стартира Kismet за сканиране на Wi-Fi мрежи.

    Returns:
        Съобщение за стартиране на Kismet.
    """
    # TODO: Имплементиране на функционалност за Kismet
    return "Kismet е стартиран.  Вижте резултатите в Kismet конзолата."

# Примери за използване:

# result = aircrack_ng_crack("capture.cap", "/usr/share/wordlists/rockyou.txt")
# print(result)

# result = kismet_scan()
# print(result)