import subprocess

def run_command(command):
    """
    Изпълнява команда в shell-а и връща резултата.

    Args:
        command: Команда за изпълнение (list).

    Returns:
        Резултат от изпълнението на командата (str).
    """
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode()

def save_output_to_file(output, filename):
    """
    Запазва резултат от програма във файл.

    Args:
        output: Резултат от програма (str).
        filename: Име на файла (str).
    """
    with open(filename, "w") as f:
        f.write(output)

def validate_ip_address(ip_address):
    """
    Проверява дали IP адресът е валиден.

    Args:
        ip_address: IP адрес (str).

    Returns:
        True, ако IP адресът е валиден, False в противен случай.
    """
    # TODO: Имплементиране на валидация на IP адрес
    return True

# Примери за използване:

# result = run_command(["ls", "-l"])
# print(result)

# save_output_to_file("Това е примерен резултат.", "result.txt")

# is_valid = validate_ip_address("192.168.1.1")
# print(is_valid)