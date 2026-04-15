import calendar
import datetime

today = datetime.datetime.now()
cDate = today.day
cMonth = today.month
cYear = today.year
cal_output = calendar.month(cYear, cMonth)

# highlighted = cal_output.replace(f" {target} ", f" \033[7m{target}\033[0m ")
highlighted = cal_output.replace(f" {str(cDate)} ", f" [{str(cDate)}] ")



print(highlighted)




formatted_date = today.strftime("%d/%m/%Y, %H:%M:%S %p")
print(formatted_date)