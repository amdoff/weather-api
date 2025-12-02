text = """A personal computer (PC) is a multi-purpose microcomputer whose size, capabilities, and price make it feasible for individual use.[1] 
Personal computers are intended to be operated directly by an end user, rather than by a computer expert or technician. 
Unlike large, costly minicomputers and mainframes, time-sharing by many people at the same time is not used with personal computers. 
Primarily in the late 1970s and 1980s, the term home computer was also used."""

last_index = text.lower().rfind("computer")

if last_index != -1:
    print(f"Oxirgi 'computer' so‘zi indeksda uchradi: {last_index}")
else:
    print("Matnda 'computer' so‘zi topilmadi.")
