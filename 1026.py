a, b = list(map(int, input().split()))
delta_time = int((b - a + 50) / 100)  # +50：解决round()函数四舍五入的bug
ss = delta_time % 60
mm = int((delta_time - ss) / 60 % 60)
hh = int((delta_time - ss - mm * 60) / 3600)
print(':'.join(str(i).zfill(2) for i in (hh, mm, ss)))
