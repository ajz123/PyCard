import re

from robobrowser import RoboBrowser

br = RoboBrowser()
br.open("https://www.capitalone.com/")
form = br.get_form()
form['email'] = "FILL_USERNAME_IN"
form['password'] = "FILL_PASSWORD_IN"
br.submit_form(form)

src = str(br.parsed())

start = '<li class="header-bal">Earned: '
end = '</li>'

result = re.search('%s(.*)%s' % (start, end), src).group(1)

print "hi"
print(result)