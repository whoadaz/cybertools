import subprocess

def autopsy_analysis(image_file):
    """
    Извършва форензичен анализ с Autopsy.

    Args:
        image_file: Път до image файл.

    Returns:
        Резултат от анализа (все още не е имплементирано).
    """
    # TODO: Имплементиране на функционалност за Autopsy
    return "Функционалността за Autopsy все още не е имплементирана."

def sleuthkit_analysis(image_file, options=""):
    """
    Извършва форензичен анализ с The Sleuth Kit.

    Args:
        image_file: Път до image файл.
        options: Допълнителни опции за The Sleuth Kit (напр. "img_stat").

    Returns:
        Резултат от анализа.
    """
    command = ["tsk_recover", image_file]
    if options:
        command.extend(options.split())
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode()

def volatility_analysis(image_file, profile, options=""):
    """
    Извършва анализ на паметта с Volatility.

    Args:
        image_file: Път до image файл.
        profile: Профил за Volatility (напр. "Win7SP1x64").
        options: Допълнителни опции за Volatility (напр. "pslist").

    Returns:
        Резултат от анализа.
    """
    command = ["volatility", "-f", image_file, "--profile=" + profile]
    if options:
        command.extend(options.split())
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode()

# Примери за използване:

# result = autopsy_analysis("image.dd")
# print(result)

# result = sleuthkit_analysis("image.dd", "img_stat")
# print(result)

# result = volatility_analysis("memory.dump", "Win7SP1x64", "pslist")
# print(result)