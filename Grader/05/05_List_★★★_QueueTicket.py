n = int(input())
q = []
ti = []
tf = []
a = 0  # index หลัง new
b = 0  # index หลัง next
d = 0  # index ของ order
alldt = []
command = []

for k in range(n):
    c = input().split()
    if c[0] == "reset":
        command.append(c[0])
        ticket = int(c[1])

    elif c[0] == "new":
        command.append(c[0])
        q.append(ticket)
        ti.append(c[1])
        print("ticket", str(q[a]))
        ticket += 1
        a += 1

    elif c[0] == "next":
        command.append(c[0])
        p = 0
        f = 0
        for i in command:  # ใช้เพื่อเช็คว่ามีคนที่โดนเรียกแล้วไม่มามั้ย ถ้ามีต้องให้ลำดับของการคิดเวลาเลื่อนไปอีก 1 เพื่อให้คำนวณได้ถูกคน
            if i == "next":
                p += 1
            elif i == "order":
                f += 1
        if p > f + 1:
            command.append("order")
            tf.append(int(0))
            d += 1
            print("call", str(q[b]))
            b += 1
        else:
            print("call", str(q[b]))
            b += 1

    elif c[0] == "order":
        command.append(c[0])
        tf.append(c[1])
        dt = int(tf[d]) - int(ti[d])
        alldt.append(dt)
        print("qtime", str(q[d]), str(dt))
        d += 1

    elif c[0] == "avg_qtime":
        command.append(c[0])
        avg = 0
        for m in range(len(alldt)):
            avg += alldt[m]
        avg = avg / len(alldt)
        print("avg_qtime", str(round(avg, 4)))
        pass
