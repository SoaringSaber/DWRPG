# public test launcher - a

import os
import b, d, e, f

b.disclaim()
b.mainMenuText()
select = b.selection("Start Map", "Test Dialouge", "Quit")
if select == 1:
    e.mapTesting()
elif select == 2:
    b.demo()
elif select == 3:
    os._exit(0)