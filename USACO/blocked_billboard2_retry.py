f = open('billboard.in')
bill_input = f.readline()
bill_input = bill_input.split()
bill = [int(i) for i in bill_input]

feed_input = f.readline()
feed_input = feed_input.split()
feed = [int(i) for i in feed_input]
f.close()
area = (bill[3] - bill[1]) * (bill[2] - bill[0])
x = [bill[0], bill[2], feed[0], feed[2]]
x.sort()
x_overlap = x[2] - x[1]

y = [bill[1], bill[3], feed[1], feed[3]]
y.sort()
y_overlap = y[2] - y[1]

overlap = x_overlap * y_overlap

points_inside = 0
points = [[bill[0], bill[1]], [bill[2], bill[3]], [bill[0], bill[3]], [bill[1], bill[2]]]
for i in range(4):
    point = points[i]
    if point[0] < feed[2] and point[0] < feed[0] and point[1] < feed[3] and point[1] > feed[1]:
        points_inside = points_inside + 1

if x_overlap < 0 or y_overlap < 0:
    overlap = 0

if points_inside == 0:
    ans = area - overlap
else:
    ans = area

f = open('billboard.out', 'w')
f.write(str(ans))
f.close()