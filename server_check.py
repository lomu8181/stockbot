import time
import line_alert

time_info = time.gmtime()

m_hour = time_info.tm_hour+9
m_min = time_info.tm_min

print(m_hour, ":", m_min)

line_alert.SendMessage(f"현재 시간 {m_hour}:{m_min}")