import pytest

SYS_VER = 1.2


@pytest.mark.skipif(SYS_VER >= 1.1, reason="Требуется версия >= 1")
def test_sys_version1():
    pass


@pytest.mark.skipif(SYS_VER >= 1.4, reason="Требуется версия >= 1")
def test_sys_version2():
    pass
