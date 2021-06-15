import smtplib

my_email = "nicolaecaldarasan1983@gmail.com"
password = "Bogdan&milena1"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()  # a way of securing our connection
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="bogdancaldarasan787@gmail.com",
    msg="Subject:Hello\n\n This is the body of my email")

connection.close()