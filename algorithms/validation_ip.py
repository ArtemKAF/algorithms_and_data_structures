'''Валидация IP-адреса двумя способами.'''
import re


def is_valid_ip(strng):
    ip = strng.split('.')
    if len(ip) != 4:
        return False
    for number in ip:
        if (
            not number.isdigit()
            or int(number) > 255
            or len(number) != len(str(int(number)))
        ):
            return False
    return True


def check_ip(string):
    return re.match(
        "^([1][0-9][0-9].|^[2][5][0-5].|^[2][0-4][0-9].|^[1][0-9][0-9].|^[0-9]"
        "[0-9].|^[0-9].)([1][0-9][0-9].|[2][5][0-5].|[2][0-4][0-9].|[1][0-9]"
        "[0-9].|[0-9][0-9].|[0-9].)([1][0-9][0-9].|[2][5][0-5].|[2][0-4][0-9]."
        "|[1][0-9][0-9].|[0-9][0-9].|[0-9].)([1][0-9][0-9]|[2][5][0-5]|[2]"
        "[0-4][0-9]|[1][0-9][0-9]|[0-9][0-9]|[0-9])$", string
    )


if __name__ == '__main__':
    assert check_ip('127.0.0.1')
    assert check_ip('12.255.56.1')
    assert not check_ip('')
    assert not check_ip('abc.def.ghi.jkl')
    assert not check_ip('123.456.789.0')
    assert not check_ip('12.34.56')
    assert not check_ip('12.34.56 .1')
    assert not check_ip('12.34.56.-1')
    assert not check_ip('123.045.067.089')
    assert check_ip('127.1.1.0')
    assert check_ip('0.0.0.0')
    assert check_ip('0.34.82.53')
    assert not check_ip('192.168.1.300')
