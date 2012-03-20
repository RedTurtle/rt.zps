# -*- coding: utf-8 -*-
from string import Template

REPORT_TEMPLATE = Template("""
CWD:      ${cwd}
User:     ${user}
PID:      ${pid}
Conf:     ${zconf}
Address:  ${address}
Memory:   ${memory}
""".lstrip())
