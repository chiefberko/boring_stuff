import re

reg = re.compile(r'.*', re.DOTALL)
mo = reg.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(mo.group())

