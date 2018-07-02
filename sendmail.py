# /usr/bin/python3
import smtplib
le = "\r\n"

def send(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: {0}{1}'.format(from_addr, le)
    header += 'To: {0}{1}'.format(to_addr_list, le)
    header += 'Cc: {0}{1}'.format(cc_addr_list, le)
    header += 'Subject: {0}{1}'.format(subject, le)
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()

def set_font_face(text):
    return text
    #return "<font face=\"verdana\">" + text + "</font>"


lint_file = open("./lint_report.txt", 'r')
lint_report = ""
for line in lint_file.readlines():
    lint_report += line
lint_file.close()



test_file = open("./test_report.txt", 'r')
test_report = ""
for line in test_file.readlines():
    test_report += line
test_file.close()

report = le
report += "Here is your lint report:{0}".format(le*2)
report += lint_report
report += le*2
report += "Here is your test report:{0}".format(le*2)
report += test_report

report = set_font_face(report)


send('skulldarkprince@gmail.com', ['jeuriqueribeiro@gmail.com'], [], 'Quality results', report, 'skulldarkprince@gmail.com', 'fakefakefake')