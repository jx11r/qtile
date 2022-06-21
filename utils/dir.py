# --==[ Current Directory ]==--

from subprocess import Popen, PIPE

def get() -> str:
    process = Popen(
        ['pwd'],
        stdout = PIPE,
        text = True,
    )

    return process.communicate()[0].strip()
