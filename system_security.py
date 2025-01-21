import subprocess

def lynis_audit():
    """
    Извършва одит на сигурността с Lynis.

    Returns:
        Резултат от одита.
    """
    command = ["lynis", "audit", "system"]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode()

def ossec_analysis():
    """
    Анализира логовете на OSSEC за откриване на аномалии.

    Returns:
        Резултат от анализа (все още не е имплементирано).
    """
    # TODO: Имплементиране на функционалност за OSSEC
    return "Функционалността за OSSEC все още не е имплементирана."

def snort_scan(interface, options=""):
    """
    Стартира Snort за откриване на мрежови атаки.

    Args:
        interface: Мрежов интерфейс,  който да се следи (напр. "eth0").
        options: Допълнителни опции за Snort (напр. "-c /etc/snort/snort.conf").

    Returns:
        Съобщение за стартиране на Snort.
    """
    command = ["snort", "-i", interface]
    if options:
        command.extend(options.split())
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode()

# Примери за използване:

# result = lynis_audit()
# print(result)

# result = ossec_analysis()
# print(result)

# result = snort_scan("eth0")
# print(result)
