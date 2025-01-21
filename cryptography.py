import subprocess

def john_crack(wordlist, hash_file, options=""):
    """
    Извършва разбиване на пароли с John the Ripper.

    Args:
        wordlist: Път до wordlist файл.
        hash_file: Път до файл с хешове.
        options: Допълнителни опции за John the Ripper (напр. "--format=raw-md5").

    Returns:
        Резултат от разбиването на паролите.
    """
    command = ["john"]
    if options:
        command.extend(options.split())
    command.extend(["--wordlist=" + wordlist, hash_file])
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode()

def hashcat_crack(hash_mode, hash_file, wordlist_or_mask, options=""):
    """
    Извършва разбиване на пароли с Hashcat.

    Args:
        hash_mode: Режим на хеширане (напр. "0" за MD5).
        hash_file: Път до файл с хешове.
        wordlist_or_mask: Път до wordlist файл или маска за атака с brute-force.
        options: Допълнителни опции за Hashcat (напр. "-a 3 -m 0").

    Returns:
        Резултат от разбиването на паролите.
    """
    command = ["hashcat", "-m", hash_mode, hash_file, wordlist_or_mask]
    if options:
        command.extend(options.split())
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode()

def hydra_crack(target, service, username, wordlist, options=""):
    """
    Извършва атака с brute-force с Hydra.

    Args:
        target: IP адрес или домейн на целта.
        service: Име на услугата (напр. "ssh", "ftp", "http").
        username: Потребителско име.
        wordlist: Път до wordlist файл.
        options: Допълнителни опции за Hydra (напр. "-t 4 -V").

    Returns:
        Резултат от атаката с brute-force.
    """
    command = ["hydra", "-l", username, "-P", wordlist, target, service]
    if options:
        command.extend(options.split())
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode()

# Примери за използване:

# result = john_crack("/usr/share/wordlists/rockyou.txt", "hashes.txt")
# print(result)

# result = hashcat_crack("0", "hashes.txt", "/usr/share/wordlists/rockyou.txt")
# print(result)

# result = hydra_crack("192.168.1.1", "ssh", "user", "/usr/share/wordlists/rockyou.txt")
# print(result)