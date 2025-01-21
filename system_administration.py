import subprocess

def nagios_check(host, service):
    """
    Извършва проверка на услуга на хост с Nagios.

    Args:
        host: Име на хоста.
        service: Име на услугата.

    Returns:
        Резултат от проверката.
    """
    command = ["nagios-plugin-check", host, service]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode()

def splunk_search(query):
    """
    Извършва търсене в Splunk.

    Args:
        query: Търсено изражение.

    Returns:
        Резултат от търсенето (все още не е имплементирано).
    """
    # TODO: Имплементиране на функционалност за Splunk
    return "Функционалността за Splunk все още не е имплементирана."

# Примери за използване:

# result = nagios_check("localhost", "PING")
# print(result)

# result = splunk_search("search index=main error")
# print(result)